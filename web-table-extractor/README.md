# 🌐 Web Table Extractor

A Python automation tool that extracts all tables from any webpage and saves them as clean CSV files automatically.

---

## ✨ Features

- Extracts all tables from any public webpage in one command
- Saves each table as a separate CSV file
- Handles HTTP errors gracefully
- Mimics a real browser request to avoid blocks
- Clean output folder structure — all CSVs saved in `extracted_tables/`

---

## 🛠 Installation

```bash
git clone https://github.com/samlearnsai2025-ctrl/python-automation-projects.git
cd python-automation-projects/web-table-extractor
pip install requests pandas lxml
```

---

## 🚀 Usage

```bash
python extract_csv_and_tables_from_website.py
```

You will be prompted to enter a URL:

```
Enter the URL: https://en.wikipedia.org/wiki/List_of_countries_by_population
```

---

## 📋 Example Output

```
Table 0 saved as extracted_tables/table_0.csv
Table 1 saved as extracted_tables/table_1.csv
Table 2 saved as extracted_tables/table_2.csv
```

All CSV files are saved inside the `extracted_tables/` folder.

---

## 💡 How It Works

1. Takes a URL as input
2. Downloads the webpage using `requests` with a browser User-Agent header
3. Parses all HTML tables using `pandas.read_html()`
4. Saves each table as a clean CSV file
5. Handles errors — invalid URLs, blocked requests, pages with no tables

---

## ⚠️ Limitations

- Only works on **public webpages** (no login required)
- Some websites block automated requests even with headers
- Only extracts HTML `<table>` elements — not dynamic JavaScript-rendered tables

---

## 🔧 Requirements

- Python 3.x
- `requests`
- `pandas`
- `lxml`

---

## 👤 Author

Built by Sameera — Python Automation Developer  
🔗 [Contra Profile](https://contra.com/sam_learns_ai_ug48c87x?referralExperimentNid=DEFAULT_REFERRAL_PROGRAM&referrerUsername=sam_learns_ai_ug48c87x) | [GitHub](https://github.com/samlearnsai2025-ctrl)