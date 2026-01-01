from collections import defaultdict
from datetime import datetime

def parse_transactions(raw_lines):
    tx = []
    for l in raw_lines:
        p = l.split('|')
        if len(p) != 8:
            continue
        try:
            tx.append({
                'TransactionID': p[0],
                'Date': p[1],
                'ProductID': p[2],
                'ProductName': p[3].replace(',', ''),
                'Quantity': int(p[4]),
                'UnitPrice': float(p[5].replace(',', '')),
                'CustomerID': p[6],
                'Region': p[7]
            })
        except:
            continue
    return tx

def validate_and_filter(transactions):
    valid = []
    invalid = 0
    for t in transactions:
        try:
            if t['Quantity'] <= 0 or t['UnitPrice'] <= 0:
                raise ValueError
            if not t['TransactionID'].startswith('T'):
                raise ValueError
            if not t['ProductID'].startswith('P'):
                raise ValueError
            if not t['CustomerID'].startswith('C'):
                raise ValueError
            valid.append(t)
        except:
            invalid += 1
    return valid, invalid, {}

def generate_sales_report(transactions, enriched_transactions, output_file="output/sales_report.txt"):
    from datetime import datetime
    from collections import defaultdict

    total_records = len(transactions)
    total_revenue = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    avg_order_value = total_revenue / total_records if total_records > 0 else 0

    dates = sorted(t['Date'] for t in transactions)
    date_range = f"{dates[0]} to {dates[-1]}" if dates else "N/A"

    # ---------------- REGION PERFORMANCE ----------------
    region_data = defaultdict(lambda: {"revenue": 0.0, "count": 0})

    for t in transactions:
        if not t.get('Region'):
            continue

        amt = t['Quantity'] * t['UnitPrice']
        region_data[t['Region']]['revenue'] += amt
        region_data[t['Region']]['count'] += 1

    region_stats = []
    for r, d in region_data.items():
        percentage = (d['revenue'] / total_revenue) * 100 if total_revenue > 0 else 0
        region_stats.append((r, d['revenue'], percentage, d['count']))

    region_stats.sort(key=lambda x: x[1], reverse=True)

    # ---------------- TOP PRODUCTS ----------------
    product_data = defaultdict(lambda: {"qty": 0, "revenue": 0.0})
    for t in transactions:
        product_data[t['ProductName']]['qty'] += t['Quantity']
        product_data[t['ProductName']]['revenue'] += t['Quantity'] * t['UnitPrice']

    top_products = sorted(product_data.items(), key=lambda x: x[1]['qty'], reverse=True)[:5]

    # ---------------- TOP CUSTOMERS ----------------
    customer_data = defaultdict(lambda: {"spent": 0.0, "count": 0})
    for t in transactions:
        amt = t['Quantity'] * t['UnitPrice']
        customer_data[t['CustomerID']]['spent'] += amt
        customer_data[t['CustomerID']]['count'] += 1

    top_customers = sorted(customer_data.items(), key=lambda x: x[1]['spent'], reverse=True)[:5]

    # ---------------- API SUMMARY ----------------
    enriched_count = sum(1 for t in enriched_transactions if t.get("API_Match"))
    success_rate = (
        (enriched_count / len(enriched_transactions)) * 100
        if len(enriched_transactions) > 0 else 0
    )

    # ---------------- WRITE REPORT ----------------
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("SALES ANALYTICS REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Records Processed: {total_records}\n")
        f.write("=" * 60 + "\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        f.write(f"Average Order Value: ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range: {date_range}\n\n")

        f.write("REGION-WISE PERFORMANCE\n")
        f.write(f"{'Region':<10}{'Sales':>15}{'% Total':>12}{'Transactions':>15}\n")
        for r, rev, pct, cnt in region_stats:
            f.write(f"{r:<10}₹{rev:>14,.2f}{pct:>11.2f}%{cnt:>15}\n")
        f.write("\n")

        f.write("TOP 5 PRODUCTS\n")
        for i, (p, d) in enumerate(top_products, 1):
            f.write(f"{i}. {p} - {d['qty']} units - ₹{d['revenue']:,.2f}\n")
        f.write("\n")

        f.write("TOP 5 CUSTOMERS\n")
        for i, (c, d) in enumerate(top_customers, 1):
            f.write(f"{i}. {c} - ₹{d['spent']:,.2f} ({d['count']} orders)\n")
        f.write("\n")

        f.write("API ENRICHMENT SUMMARY\n")
        f.write(f"Enriched Records: {enriched_count}\n")
        f.write(f"Success Rate: {success_rate:.2f}%\n")

    print("✓ Detailed sales report generated")
