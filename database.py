from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

# ALTERE PARA ACESSAR O SEU BANCO DE DADOS:
DATABASE_URL = "postgresql://isaac:isaac@localhost:5432/ApresentacaoProjeto1"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def GetDBSession():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def CreateDatabaseTables():
    Base.metadata.create_all(bind=engine)
    print("Tabelas verificadas/criadas com sucesso.")
