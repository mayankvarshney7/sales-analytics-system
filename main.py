from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions, validate_and_filter, generate_sales_report
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data, save_enriched_data

def main():
    raw = read_sales_data("data/sales_data.txt")
    parsed = parse_transactions(raw)
    valid, invalid, _ = validate_and_filter(parsed)
    api_products = fetch_all_products()
    product_map = create_product_mapping(api_products)
    enriched = enrich_sales_data(valid, product_map)
    save_enriched_data(enriched)
    generate_sales_report(valid, enriched)
    print("Process Completed Successfully")

if __name__ == "__main__":
    main()
