import os
import fnmatch
from pathlib import Path

def parse_gitignore(folder_path):
    """Parse the .gitignore file and return a list of patterns."""
    gitignore_path = os.path.join(folder_path, ".gitignore")
    if not os.path.exists(gitignore_path):
        return []
    with open(gitignore_path, "r", encoding="utf-8") as f:
        patterns = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return patterns

def is_ignored(path, patterns):
    """Check if a file or folder matches any .gitignore pattern."""
    relative_path = str(Path(path).relative_to(Path(path).anchor))
    for pattern in patterns:
        if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False