import os
from PyQt5.QtWidgets import (
    QMainWindow, QSplitter, QTextEdit, QCheckBox, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QPushButton, QLabel,
    QApplication
)
from PyQt5.QtCore import Qt
from ui.file_tree import FileTreeWidget
from context_builder import build_context
from utils.settings_utils import load_settings, save_settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Repo Prompt Tool")
        self.setGeometry(100, 100, 800, 600)

        # Load last folder from settings
        self.settings = load_settings()
        self.folder_path = self.settings.get("last_folder", "")

        # Main splitter
        self.splitter = QSplitter()
        self.setCentralWidget(self.splitter)

        # Left side: File tree and checkboxes
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()

        # File Picker Button
        self.file_picker_button = QPushButton("Choose or Change Folder")
        self.file_picker_button.clicked.connect(self.open_folder_dialog)
        self.left_layout.addWidget(self.file_picker_button)

        # Select All Checkbox
        self.select_all_checkbox = QCheckBox("Select All")
        self.select_all_checkbox.stateChanged.connect(self.toggle_select_all)
        self.left_layout.addWidget(self.select_all_checkbox)

        # File Tree Widget
        self.file_tree = FileTreeWidget()
        self.file_tree.itemChanged.connect(self.update_context)
        self.left_layout.addWidget(self.file_tree)

        # Include File Tree Checkbox
        self.include_file_tree_checkbox = QCheckBox("Include File Tree")
        self.include_file_tree_checkbox.setChecked(True)
        self.include_file_tree_checkbox.stateChanged.connect(self.update_context)
        self.left_layout.addWidget(self.include_file_tree_checkbox)

        # Include File Content Checkbox
        self.include_file_content_checkbox = QCheckBox("Include File Content")
        self.include_file_content_checkbox.setChecked(True)  # ADD THIS LINE
        self.include_file_content_checkbox.stateChanged.connect(self.update_context)
        self.left_layout.addWidget(self.include_file_content_checkbox)

        self.left_widget.setLayout(self.left_layout)
        self.splitter.addWidget(self.left_widget)

        # Right side: Context Text Edit
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.right_layout.addWidget(self.text_edit)

        # Word Count Label
        self.word_count_label = QLabel("Words: 0")
        self.right_layout.addWidget(self.word_count_label)

        # Copy Button
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.right_layout.addWidget(self.copy_button)

        self.right_widget.setLayout(self.right_layout)
        self.splitter.addWidget(self.right_widget)

        # Load folder if it exists
        if self.folder_path and os.path.isdir(self.folder_path):
            self.file_tree.populate_tree(self.folder_path)

    def open_folder_dialog(self):
        """Open a folder selection dialog."""
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_path = folder_path
            self.settings["last_folder"] = folder_path
            save_settings(self.settings)
            self.file_tree.populate_tree(self.folder_path)

    def toggle_select_all(self, state):
        """Toggle the selection of all files in the tree."""
        self.file_tree.set_all_checkboxes(state)

    def update_context(self):
        """Update the context text based on selected files and options."""
        selected_files = self.file_tree.get_selected_files()
        include_file_tree = self.include_file_tree_checkbox.isChecked()
        include_file_content = self.include_file_content_checkbox.isChecked()
        context = build_context(self.folder_path, selected_files, include_file_tree, include_file_content)
        self.text_edit.setPlainText(context)
        self.update_word_count(context)

    def update_word_count(self, text):
        """Update the word count label."""
        word_count = len(text.split())
        self.word_count_label.setText(f"Words: {word_count}")

    def copy_to_clipboard(self):
        """Copy the context text to the clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_edit.toPlainText())
        QMessageBox.information(self, "Copied", "Context text copied to clipboard.")