def read_sales_data(filename):
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as f:
                lines = f.readlines()
            return [l.strip() for l in lines[1:] if l.strip()]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            return []
    return []
