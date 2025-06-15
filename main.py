import traceback
import json
from pathlib import Path
from sqlalchemy.orm import Session

from database import GetDBSession, CreateDatabaseTables
from etl import extract, transform, load

BASE_URL_API = "https://world.openfoodfacts.net/api/v2"

def RunETL(productBarcode: str, db: Session, apiBaseUrl: str):
    print(f"INFO: Iniciando ETL para o código: {productBarcode}")
    
    data = extract.Extract(productBarcode, apiBaseUrl)
    if not data:
        print(f"ERROR: Falha na extração para {productBarcode}")
        return False

    transformedData = transform.Transform(data, productBarcode)
    if not transformedData:
        print(f"ERROR: Falha na transformação para {productBarcode}")
        return False

    try:
        load.Load(db, transformedData)
        return True
    except Exception as e: 
        print(f"ERROR: Erro ao carregar dados do produto {productBarcode}: {e}")
        traceback.print_exc()
        return False

def Main():
    CreateDatabaseTables()

    jsonPath = Path("product_codes_dict.json")

    with open(jsonPath, "r", encoding="utf-8") as f:
        product_codes_json = json.load(f)
        product_codes = [str(item["code"]) for item in product_codes_json]

    db_session = GetDBSession()
    db: Session = next(db_session)

    for code in product_codes:
        try:
            success = RunETL(code, db, BASE_URL_API)
            if success:
                db.commit()
                print(f"INFO: COMMIT realizado com sucesso para o produto: {code}")
            else:
                db.rollback()
                print(f"WARNING: ROLLBACK realizado para o produto: {code}")
        except Exception as e:
            print(f"ERROR: Erro inesperado com o produto {code}: {e}")
            traceback.print_exc()
            db.rollback()
        finally:
            print(f"INFO: Finalizado o ETL para o código: {code}")

    try:
        next(db_session)
    except StopIteration:
        pass

if __name__ == "__main__":
    Main()
