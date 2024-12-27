import os
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from utils.gitignore_utils import parse_gitignore, is_ignored

class FileTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["File Structure"])
        self.setColumnCount(1)

    def populate_tree(self, folder_path):
        """Populate the tree widget with the folder structure, excluding .gitignore patterns."""
        if not os.path.isdir(folder_path):
            QMessageBox.warning(self, "Error", f"The folder {folder_path} does not exist.")
            return
        self.clear()
        gitignore_patterns = parse_gitignore(folder_path)
        folder_name = os.path.basename(folder_path)
        root_item = QTreeWidgetItem(self)
        root_item.setText(0, folder_name)
        root_item.setCheckState(0, Qt.Unchecked)
        self.add_items(root_item, folder_path, gitignore_patterns)
        self.expandAll()

    def add_items(self, parent, path, gitignore_patterns):
        """Recursively add items to the tree widget, excluding .gitignore patterns."""
        for name in sorted(os.listdir(path)):
            full_path = os.path.join(path, name)
            if is_ignored(full_path, gitignore_patterns):
                continue
            item = QTreeWidgetItem(parent)
            item.setText(0, name)
            item.setCheckState(0, Qt.Unchecked)
            if os.path.isdir(full_path):
                self.add_items(item, full_path, gitignore_patterns)
            else:
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

    def set_all_checkboxes(self, state):
        """Set the check state of all items in the tree."""
        self._set_check_state(self.invisibleRootItem(), state)

    def _set_check_state(self, item, state):
        """Recursively set the check state of items."""
        if item is None:
            return
        item.setCheckState(0, state)
        for i in range(item.childCount()):
            child = item.child(i)
            self._set_check_state(child, state)

    def get_selected_files(self):
        """Get the paths of all selected files."""
        selected_files = []
        self._get_selected_files(self.invisibleRootItem(), selected_files)
        return selected_files

    def _get_selected_files(self, item, selected_files, base_path=""):
        """Recursively get selected files."""
        if item is None:
            return
        if item.checkState(0) == Qt.Checked and not item.childCount():
            selected_files.append(os.path.join(base_path, item.text(0)))
        for i in range(item.childCount()):
            child = item.child(i)
            new_base_path = os.path.join(base_path, item.text(0)) if item.text(0) else base_path
            self._get_selected_files(child, selected_files, new_base_path)