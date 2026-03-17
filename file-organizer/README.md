# 📁 File Organizer

A Python automation tool that instantly organizes messy folders by sorting files into categorized subfolders — with a full undo feature to reverse everything safely.

---

## ✨ Features

- Automatically sorts files into folders by type (Images, Documents, Videos, Code, Others)
- Records every move in a log for full traceability
- **Undo feature** — reverses all changes and removes created folders cleanly
- Handles edge cases — skips subfolders, safely handles non-empty folders on undo

---

## 📂 Supported File Types

| Extension | Category |
|---|---|
| `.jpg`, `.png` | Images |
| `.pdf`, `.docx` | Documents |
| `.mp4` | Videos |
| `.py` | Code |
| Everything else | Others |

---

## 🛠 Installation

No external libraries needed — uses Python's built-in modules only.

```bash
git clone https://github.com/samlearnsai2025-ctrl/python-automation-projects.git
cd python-automation-projects/file-organizer
```

---

## 🚀 Usage

```bash
python file_organizer.py
```

You will be prompted to:
1. Enter the folder path you want to organize
2. Optionally undo the organization after it completes

---

## 📋 Example Output

```
Moved: resume.pdf -> Documents
Moved: photo.jpg -> Images
Moved: script.py -> Code
Organization complete!

Do you want to undo the organization? (yes/no): yes

Moved back: resume.pdf -> C:/Users/You/Desktop/JobFiles
Moved back: photo.jpg -> C:/Users/You/Desktop/JobFiles
Moved back: script.py -> C:/Users/You/Desktop/JobFiles
Removed empty folder: Documents
Removed empty folder: Images
Removed empty folder: Code
Undo complete!
```

---

## 💡 How It Works

1. Scans the target folder for files (skips subfolders)
2. Matches each file's extension to a category
3. Creates category subfolders if they don't exist
4. Moves each file and logs the move
5. On undo — reverses all moves and deletes empty folders

---

## 🔧 Customization

You can easily add more file types by editing the `categories` dictionary:

```python
categories = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.mp4': 'Videos',
    '.py': 'Code',
    '.xlsx': 'Documents',  # add more here
    '.mp3': 'Music',       # add more here
}
```

---

## 👤 Author

Built by Sameera — Python Automation Developer  
🔗 [Contra Profile](https://contra.com/yourprofile) | [GitHub](https://github.com/samlearnsai2025-ctrl)