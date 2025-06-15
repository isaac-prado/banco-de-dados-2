from model import TipoNutriEcoScoreDB, TipoNovaScoreDB
import re

def sanitize_enum_value(value, enum_cls):
    try:
        if enum_cls == TipoNovaScoreDB:
            for member in enum_cls:
                if member.value == value:
                    return member
            return None
        
        return enum_cls(value.upper())
    except Exception:
        return None
    
def clean_language_prefix(text: str) -> str:
    match = re.match(r'^[a-z]{2}:(.+)', text)
    if match:
        return match.group(1).strip()
    return text.strip()


def transform_api_data(api_data: dict, product_code: str):
    try:
        cleaned_categories = []

        for c in api_data.get("categories", "").split(","):
            stripped_c = c.strip()
            if stripped_c:
                cleaned_categories.append(clean_language_prefix(stripped_c))

        cleaned_tags = []
        for t in api_data.get("labels_tags", []):
            stripped_t = t.strip()
            if stripped_t:
                cleaned_tags.append(clean_language_prefix(stripped_t))

        transformed = {
            "codigo": product_code,
            "nome": api_data.get("product_name", "NOME_DESCONHECIDO"),
            "nutriscore": sanitize_enum_value(api_data.get("nutriscore_grade", ""), TipoNutriEcoScoreDB),
            "ecoscore": sanitize_enum_value(api_data.get("ecoscore_grade", ""), TipoNutriEcoScoreDB),
            "novascore": sanitize_enum_value(str(api_data.get("nova_group", "")), TipoNovaScoreDB),

            "marcas": [m.strip() for m in api_data.get("brands", "").split(",") if m.strip()],
            "categorias": cleaned_categories,
            "ingredientes": api_data.get("ingredients", []),
            "nutrientes": api_data.get("nutriments", {}),
            "tags": cleaned_tags,
        }
        return transformed
    except Exception as e:
        print(f"ERROR: Falha ao transformar os dados do produto {product_code}: {e}")
        return None
