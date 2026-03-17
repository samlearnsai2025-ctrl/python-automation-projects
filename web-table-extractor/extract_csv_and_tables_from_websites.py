import os
import requests
import pandas as pd

url = input("Enter the URL: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}
# download the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # parse the webpage content
    tables = pd.read_html(response.text)

    if len(tables) == 0:
        print("No tables found on this page!")
        exit()
        
    # create a directory to save the CSV files
    os.makedirs('extracted_tables', exist_ok=True)

    for i, table in enumerate(tables):
        # save each table as a CSV file in the created directory
        table.to_csv(f'extracted_tables/table_{i}.csv', index=False)
        print(f'Table {i} saved as extracted_tables/table_{i}.csv')
else:
    print(f"Failed to fetch page: {response.status_code}")