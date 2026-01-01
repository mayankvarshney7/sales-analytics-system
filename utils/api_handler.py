import requests

def fetch_all_products():
    try:
        r = requests.get("https://dummyjson.com/products?limit=100", timeout=10)
        return r.json().get("products", [])
    except:
        return []

def create_product_mapping(products):
    return {p['id']: p for p in products}

def enrich_sales_data(transactions, mapping):
    enriched = []
    for t in transactions:
        e = t.copy()
        try:
            pid = int(t['ProductID'][1:]) - 100
            if pid in mapping:
                e['API_Match'] = True
            else:
                e['API_Match'] = False
        except:
            e['API_Match'] = False
        enriched.append(e)
    return enriched

def save_enriched_data(data, filename="data/enriched_sales_data.txt"):
    if not data:
        return
    with open(filename, "w") as f:
        f.write("|".join(data[0].keys()) + "\n")
        for r in data:
            f.write("|".join(str(r[k]) for k in r.keys()) + "\n")
