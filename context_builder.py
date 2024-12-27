from utils.file_utils import read_file
import os

def build_context(folder_path, selected_files, include_file_tree, include_file_content):
    """Build the context text based on selected files and options."""
    context = ""

    # Include file tree if requested
    if include_file_tree:
        context += "File Tree:\n"
        for file in selected_files:
            context += f"{file}\n"
        context += "\n\n"

    # Include content of selected files if requested
    if include_file_content:
        for file in selected_files:
            full_path = os.path.join(folder_path, file)
            content = read_file(full_path)
            context += f"--- {file} ---\n{content}\n\n"

    return context