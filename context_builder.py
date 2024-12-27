from utils.file_utils import read_file
import os
def build_file_tree(folder_path, files):
    """Build a properly formatted file tree structure."""
    tree = {}
    for file in files:
        parts = file.split(os.sep)
        current = tree
        for part in parts:
            current = current.setdefault(part, {})

    def build_tree_str(tree, prefix=""):
        tree_str = ""
        items = list(tree.items())
        
        if not prefix:  # Root level
            root_name = os.path.basename(folder_path)
            tree_str = f"{root_name}/\n"
            if items:
                items = list(items[0][1].items())
        
        for i, (name, subtree) in enumerate(items):
            is_last = i == len(items) - 1
            connector = '└── ' if is_last else '├── '
            tree_str += f"{prefix}{connector}{name}"
            tree_str += '/' if subtree else '\n'
            
            if not subtree:
                continue
                
            tree_str += '\n'
            ext_prefix = prefix + ("    " if is_last else "│   ")
            tree_str += build_tree_str(subtree, ext_prefix)
            
        return tree_str

    return build_tree_str(tree)


def build_context(folder_path, selected_files, include_file_tree, include_file_content):
    context = ""
    
    if include_file_tree:
        context += build_file_tree(folder_path, selected_files)
        context += "\n"

    if include_file_content:
        for file in selected_files:
            full_path = os.path.join(folder_path, file.replace(os.path.basename(folder_path) + os.sep, '', 1))
            try:
                content = read_file(full_path)
                context += f"--- {file} ---\n{content}\n\n"
            except Exception as e:
                context += f"Error reading {file}: {str(e)}\n\n"

    return context