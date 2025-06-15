import requests

def Extract(productBarcode: str, apiBaseUrl: str):
    url = f"{apiBaseUrl}/product/{productBarcode}.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") != 1:
            print(f"WARN: Produto {productBarcode} não encontrado na API.")
            return None
        return data.get("product")
    except requests.RequestException as e:
        print(f"ERROR: Falha ao buscar dados da API para {productBarcode}: {e}")
        return None
