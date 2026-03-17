# 📄 PDF Table Extractor

A Python automation tool that extracts tables from PDF files and saves them as clean CSV files — page by page, automatically.

---

## ✨ Features

- Extracts tables from every page of any PDF automatically
- Saves each table as a separate CSV file
- Skips pages with no tables gracefully
- Clean output folder structure — all CSVs saved in `extracted_tables/`

---

## 🛠 Installation

```bash
git clone https://github.com/samlearnsai2025-ctrl/python-automation-projects.git
cd python-automation-projects/pdf-table-extractor
pip install pdfplumber pandas
```

---

## 🚀 Usage

```bash
python extract_table_from_pdf.py
```

You will be prompted to enter the path to your PDF file:

```
Enter the PDF file path: C:/Users/You/Documents/report.pdf
```

---

## 📋 Example Output

```
Page 1: Saved 6 rows → extracted_tables/extracted_table_page_1.csv
Page 2: No table found
Page 3: Saved 12 rows → extracted_tables/extracted_table_page_3.csv
```

All CSV files are saved inside the `extracted_tables/` folder.

---

## 💡 How It Works

1. Takes a PDF file path as input
2. Opens the PDF using `pdfplumber`
3. Loops through every page
4. Detects tables on each page
5. Converts each table to a pandas DataFrame
6. Saves it as a clean CSV file

---

## ⚠️ Limitations

- Works best with **text-based PDFs** (not scanned/image PDFs)
- Scanned PDFs require OCR (a future enhancement)

---

## 🔧 Requirements

- Python 3.x
- `pdfplumber`
- `pandas`

---

## 👤 Author

Built by Sameera — Python Automation Developer  
🔗 [Contra Profile](https://contra.com/sam_learns_ai_ug48c87x?referralExperimentNid=DEFAULT_REFERRAL_PROGRAM&referrerUsername=sam_learns_ai_ug48c87x) | [GitHub](https://github.com/samlearnsai2025-ctrl)