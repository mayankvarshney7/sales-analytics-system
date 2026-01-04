# Sales Analytics System

## Project Description
The Sales Analytics System is a Python-based application that reads raw sales transaction data, cleans and validates it, performs analytical processing, enriches the data using an external API, and generates a comprehensive text-based sales report.

This project is developed as part of **`Module 3: Python Programming Assignment`** and demonstrates practical usage of:
* **File handling with encoding support**
* **Data cleaning and validation**
* **Lists, dictionaries, and functions**
* **API integration** (DummyJSON)
* **Data enrichment**
* **Report generation**
* **Error handling and modular programming**

---

## Project Directory Structure
```text
sales-analytics-system/
│
├── main.py                     # Main program (entry point)
├── README.md                   # Project documentation
├── requirements.txt            # Required Python libraries
├── utils/
│   ├── file_handler.py         # Reads sales data with encoding handling
│   ├── data_processor.py       # Data parsing, validation, analytics & report
│   └── api_handler.py          # API integration & data enrichment
├── data/
│   ├── sales_data.txt          # Input sales data (provided)
│   └── enriched_sales_data.txt # Generated after execution
└── output/
    └── sales_report.txt        # Generated sales analytics report
```
## System Requirements

Before running the project, ensure the following requirements are met:

- **Python version: 3.8 or higher**

- **Operating System: Windows / macOS / Linux**

- **Internet connection: Required (for DummyJSON API)**

Required Python Library

- **`requests`**

## Installation Instructions
### Step 1: Clone or Extract the Project

If using GitHub:
```bash
git clone <your-github-repository-url>
cd sales-analytics-system
```

If using ZIP:

- **Extract the ZIP file**

- **Open the extracted `sales-analytics-system` folder**
  

### Step 2: Install Dependencies

Install required libraries using:
```bash
pip install -r requirements.txt
```

This installs the `requests` library required for API integration.

## Input Data Setup (IMPORTANT)

Ensure the file `sales_data.txt` is placed inside the `data/` folder:
```bash
data/sales_data.txt
```

The input file:

- **Uses pipe (`|`) as delimiter**

- **May contain encoding issues**

- **May include invalid or missing values**

- **May include commas in numeric fields**

All such data quality issues are handled automatically by the program.


## How to Run the Code (Step-by-Step)
### Step 1: Open Terminal / Command Prompt

Navigate to the project root directory:
```bash
cd sales-analytics-system
```

### Step 2: Run the Main Program

Execute the application using:
```bash
python main.py
```

## Program Execution Flow

1. When `main.py` is executed, the application performs the following steps in order:

2. Reads the sales data file with encoding handling

3. Parses and cleans raw transaction data

4. Validates transactions based on business rules

5. Displays available filtering options (region & amount range)

6. Applies optional user-selected filters

   - **Performs sales analytics:**

   - **Total revenue**

   - **Region-wise sales**

   - **Top-selling products**

   - **Top customers**

   - **Daily sales trends**

7. Fetches product data from the DummyJSON API

8. Enriches sales transactions with API information

9. Saves enriched data to a new file

10. Generates a comprehensive sales analytics report
    

## Sample Console Output
```text
SALES ANALYTICS SYSTEM
========================================
[1/10] Reading sales data...
✓ Successfully read 80 transactions

[2/10] Parsing and cleaning data...
✓ Parsed 71 records

[3/10] Filter Options Available:
Regions: East, North, South, West
Amount Range: ₹500 - ₹79,000

[4/10] Validating transactions...
✓ Valid: 71  Invalid: 0

[5/10] Analyzing sales data...
✓ Analysis complete

[6/10] Fetching product data from API...
✓ Fetched 30 products

[7/10] Enriching sales data...
✓ Enriched 71/71 transactions (100.00%)

[8/10] Saving enriched data...
✓ Saved to data/enriched_sales_data.txt

[9/10] Generating report...
✓ Report saved to output/sales_report.txt

[10/10] Process Complete!
```

## Output Files Generated

After successful execution, the following files are created automatically:

### 1. Enriched Sales Data
```bash
data/enriched_sales_data.txt
```

- **Pipe-delimited format**

- **Includes original fields and API enrichment fields**

### 2. Sales Analytics Report
```bash
output/sales_report.txt
```

The report includes:

- **Header with timestamp**

- **Overall sales summary**

- **Region-wise performance**

- **Top products**

- **Top customers**

- **API enrichment summary**

## Error Handling

- **Handles file encoding issues safely**

- **Skips invalid or malformed records**

- **Prevents division-by-zero errors**

- **Handles API failures gracefully**

- **Application does not crash on errors**
  

## Submission Instructions

- **Repository name must be `sales-analytics-system`**

- **The repository must be public**

- **Submit only the root GitHub repository URL**

- **Do not submit individual file links**

- **Keep the repository accessible until grades are released**
  

## Conclusion

This project fulfills all requirements of the assignment and follows the prescribed marking scheme. It demonstrates an end-to-end implementation of a real-world sales analytics workflow using Python.
