
# CodeMap 🗺️

**CodeMap** is a powerful Python application designed to help developers **visualize, explore, and document their code repositories** with ease. Whether you're working on a small project or a large codebase, CodeMap provides a **clean and intuitive interface** to explore your folder structure, select files, and generate context-rich documentation. Perfect for **code reviews, onboarding, or sharing project context** with your team!

---

## ✨ Features

- **File Tree Visualization**: Explore your repository's folder structure in a beautifully formatted tree view (`├──`, `└──`, `│`).
- **Selective File Inclusion**: Choose specific files or folders to include in your context.
- **Context Generation**: Generate a **context-rich document** with file content, file paths, and an optional file tree.
- **`.gitignore` Support**: Automatically excludes files and folders based on your `.gitignore` rules.
- **Word Count**: Track the number of words in your generated context.
- **Copy to Clipboard**: Easily copy the generated context to your clipboard with one click.
- **Cross-Platform**: Works seamlessly on **Windows**, **macOS**, and **Linux**.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/xx77yy/codemap.git
   cd codemap
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

---

## 🚀 How to Use

1. **Choose a Folder**:
   - Click the **"Choose or Change Folder"** button to select your project folder.

2. **Explore the File Tree**:
   - The left panel displays your folder structure in a **clean and formatted tree view**.
   - Use the **"Select All"** checkbox to quickly select or deselect all files.

3. **Generate Context**:
   - Toggle the **"Include File Tree"** checkbox to include the folder structure in the context.
   - Toggle the **"Include File Content"** checkbox to include the content of selected files.
   - The generated context will appear in the right panel.

4. **Copy or Save**:
   - Use the **"Copy to Clipboard"** button to copy the context.
   - The **word count** is displayed at the bottom for quick reference.

---

## 🧩 Example

### Folder Structure
```
CodeMap/
│
├── main.py
├── settings.json
├── ui/
│   ├── main_window.py
│   └── file_tree.py
├── utils/
│   ├── file_utils.py
│   ├── settings_utils.py
│   └── gitignore_utils.py
└── context_builder.py
```

### Generated Context
```
folder structure:
CodeMap/
├── main.py
├── settings.json
├── ui/
│   ├── main_window.py
│   └── file_tree.py
├── utils/
│   ├── file_utils.py
│   ├── settings_utils.py
│   └── gitignore_utils.py
└── context_builder.py

--- main.py ---
# Your main.py content here...

--- ui/main_window.py ---
# Your main_window.py content here...
```

---

## 🤝 Contributing

We welcome contributions from the community! Here’s how you can help:

1. **Fork the Repository**:
   - Click the **"Fork"** button at the top right of this page.

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**:
   - Add new features, fix bugs, or improve documentation.

4. **Submit a Pull Request**:
   - Open a pull request and describe your changes. We’ll review and merge it!

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with ❤️ using **Python** and **PyQt5**.
- Inspired by the need for better code documentation tools.

---

## 📬 Contact

Have questions or suggestions? Feel free to reach out:

- **Email**: your-email@example.com
- **GitHub Issues**: [Open an Issue](https://github.com/xx77yy/codemap/issues)

---

## 🌟 Star the Project

If you find this project useful, please **give it a star** on GitHub! ⭐

[![GitHub Stars](https://img.shields.io/github/stars/xx77yy/codemap?style=social)](https://github.com/xx77yy/codemap)

---

Happy coding! 🚀