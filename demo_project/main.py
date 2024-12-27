import os

def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            file_list.append(relative_path)
    return file_list

def build_file_tree(files):
    tree = {}
    for file in files:
        parts = file.split(os.sep)
        current_level = tree
        for part in parts:
            if part not in current_level:
                if part == parts[-1]:
                    current_level[part] = None  # File
                else:
                    current_level[part] = {}    # Directory
            current_level = current_level[part]
    
    def build_tree_str(tree, indent='', is_last=True):
        tree_str = ''
        keys = list(tree.keys())
        for idx, key in enumerate(keys):
            connector = '└── ' if is_last else '├── '
            tree_str += indent + connector + key + '\n'
            value = tree[key]
            if isinstance(value, dict):
                new_indent = indent + ('    ' if is_last else '│    ')
                inner_is_last = idx == len(keys) - 1
                tree_str += build_tree_str(value, new_indent, inner_is_last)
        return tree_str
    return build_tree_str(tree)

def compile_context(files, include_tree, directory):
    context = ''
    if include_tree:
        tree = build_file_tree(files)
        context += 'File Tree:\n'
        context += tree + '\n\n'
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            #context += f'--- {file} ---\n{content}\n\n'
            context += f'#{file_path}\n"""\n{content}\n"""\n'
        except Exception as e:
            print(f'Error reading {file_path}: {e}')
    return context

def main():
    folder_path = 'demo_project'  # Replace with the actual path
    include_all_files = True
    include_file_tree = True

    if not os.path.isdir(folder_path):
        print(f'The folder {folder_path} does not exist.')
        return

    if include_all_files:
        files = get_all_files(folder_path)
    else:
        # Specify specific files to include
        files = ['file1.txt', 'subfolder/file2.py']

    context = compile_context(files, include_file_tree, folder_path)
    print(context)

if __name__ == '__main__':
    main()