# FileSearch-Pro
# FileSearch Pro - Cross-Platform File Finder with GUI & CLI Support

**FileSearch Pro** is a desktop utility built for both regular users and power users. It supports **case-insensitive file search**, **date and size filtering**, and **file extension and name filtering**, all accessible through an intuitive GUI and a flexible CLI interface. Whether you're on **Windows**, **Linux**, or **macOS**, FileSearch Pro helps you locate files with precision.

---

## 🚨 Problem Statement

Searching for files using built-in OS tools can be slow, inefficient, and limited:

* **GUI tools** lack advanced filters or are too slow with large file sets.
* **CLI tools** require technical knowledge and offer inconsistent options across platforms.
* **No built-in way to save search results or scroll output easily.**

FileSearch Pro addresses these limitations with a modern, dual-mode solution.

---

## 🧰 Features

* 🔎 **Case-insensitive Partial Filename Search**
* 📅 **Filter by Created/Modified Date** (`DD-MM-YYYY` format)
* 📏 **Filter by File Size** (min/max bytes)
* 🧩 **Filter by File Extension** (e.g. `.txt`, `.pdf`, etc.)
* 📤 **Save Results** to a text file
* 📊 **File Count Display** in GUI mode
* 🖥️ **Graphical User Interface (GUI)**

  * Scrollable results output
  * Icons for better visuals (search, save, folder)
  * Professional, modern layout with theme support
* 🧑‍💻 **Command Line Interface (CLI)**

  * Same powerful features for automation and scripting

---

## 💻 Technology Stack

* **Language:** Python 3.6+
* **GUI:** Tkinter (standard library)
* **Platform Support:** Windows, Linux, macOS

No third-party dependencies required. Just run and search.

---

## 📦 Installation

1. Clone or download the repository:

   ```bash
   git clone https://github.com/Kernel-Freak/FileSearch-Pro.git
   cd FileSearch-Pro
   ```
   
3. Install Depndencies

   ```bash
   pip install tk
   ```
     
2. Run the script:

   ```bash
   python file_search_tool.py
   ```

   > This will launch the GUI by default.

---

## 🧭 Usage Guide

### 🔹 GUI Mode (Default)

```bash
python file_search_tool.py
```

* Browse for a folder
* Select filters (name, extension, date, size)
* View and scroll results
* Save results to a file if desired

### 🔹 CLI Mode

```bash
python file_search_tool.py <directory> [OPTIONS]
```

**Available CLI Options:**

| Option        | Description                       |
| ------------- | --------------------------------- |
| `--start`     | Start date (`DD-MM-YYYY`)         |
| `--end`       | End date (`DD-MM-YYYY`)           |
| `--extension` | File extension (e.g. `.txt`)      |
| `--min-size`  | Minimum file size in bytes        |
| `--max-size`  | Maximum file size in bytes        |
| `--name`      | Filename contains (partial match) |
| `--save`      | Save results to specified file    |

#### Example:

```bash
python file_search_tool.py "/home/user/Downloads" --extension ".pdf" --start 01-01-2024 --name "invoice" --save result.txt
```

---

## 🖼 Screenshots (GUI)

* Main Window with Options
* Search Results Output with Scroll
* Icons on Buttons (Search, Save, Folder)
* Light/Dark Theme Preview

> Screenshots to be added manually in the repository.

---

## 📂 Output Example

```
/home/user/Documents/summary.txt
  Created: 01-04-2024 10:22:31
  Modified: 03-04-2024 14:12:02
  Size: 4536 bytes
```

---

## 📁 Icons

You can place the following PNG icons in the same directory as the script (recommended size: 24x24):

* `search.png`
* `save.png`
* `folder.png`

If not available, fallback text buttons will be used.

---

## 🚀 Future Enhancements

* 🔧 Persistent settings between sessions
* 🌗 More advanced dark/light theming
* 📊 Export to formats like CSV/JSON
* 📅 Presets for common search scenarios

---

## 🤝 Contributing

Want to make this tool even better? PRs and suggestions are welcome!

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0(GPLv3)](LICENSE). 

---

## Contact / Author Info

- **Author**: Samrat Mandal
- **Email**: samratmandal423@gmail.com
- **GitHub**: https://github.com/Kernel-Freak
- **Linkedin**: https://www.linkedin.com/in/samrat7/

For additional questions or further discussion, please feel free to contact the author.
