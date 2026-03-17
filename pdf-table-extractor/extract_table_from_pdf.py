import pdfplumber
import pandas as pd
import os

file_path = input("Enter the PDF file path: ")

# create a directory to save the CSV files
os.makedirs("extracted_tables", exist_ok=True) 

# open the PDF file
with pdfplumber.open(file_path) as pdf:
    # loop through each page in the PDF
    for i, page in enumerate(pdf.pages):
        # extract tables from the page
        table = page.extract_table()

        if table:
            df = pd.DataFrame(table[1:], columns=table[0]) # convert the table to a DataFrame, using the first row as column headers
            df.to_csv(f"extracted_tables/extracted_table_page_{i+1}.csv", index=False)
            print(f"Page {i+1}: Saved {len(df)} rows")
        else:
            print(f"Page {i+1}: No table found")