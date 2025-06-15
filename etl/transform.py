from model import TipoNutriEcoScoreDB, TipoNovaScoreDB
import re

def SanitizeEnum(value, enumType):
    try:
        if enumType == TipoNovaScoreDB:
            for member in enumType:
                if member.value == value:
                    return member
            return None
        
        return enumType(value.upper())
    except Exception:
        return None
    
def CleanLanguagePrefix(text: str) -> str:
    match = re.match(r'^[a-z]{2}:(.+)', text)
    if match:
        return match.group(1).strip()
    return text.strip()


def Transform(api_data: dict, product_code: str):
    try:
        cleaned_categories = []

        for c in api_data.get("categories", "").split(","):
            stripped_c = c.strip()
            if stripped_c:
                cleaned_categories.append(CleanLanguagePrefix(stripped_c))

        cleaned_tags = []
        for t in api_data.get("labels_tags", []):
            stripped_t = t.strip()
            if stripped_t:
                cleaned_tags.append(CleanLanguagePrefix(stripped_t))

        transformed = {
            "codigo": product_code,
            "nome": api_data.get("product_name", "NOME_DESCONHECIDO"),
            "nutriscore": SanitizeEnum(api_data.get("nutriscore_grade", ""), TipoNutriEcoScoreDB),
            "ecoscore": SanitizeEnum(api_data.get("ecoscore_grade", ""), TipoNutriEcoScoreDB),
            "novascore": SanitizeEnum(str(api_data.get("nova_group", "")), TipoNovaScoreDB),

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
