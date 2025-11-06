#!/usr/bin/env python3
"""
Fix indentation in markdown content after front matter
"""

import re
from pathlib import Path

def fix_file_indentation(filepath):
    """Remove leading indentation from markdown content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into front matter and content
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return False

    front_matter = parts[1]
    body_content = parts[2]

    # Remove leading whitespace from each line in the body
    lines = body_content.split('\n')
    fixed_lines = []
    for line in lines:
        # Remove up to 2 spaces of indentation at the start of each line
        if line.startswith('  '):
            fixed_lines.append(line[2:])
        else:
            fixed_lines.append(line)

    fixed_body = '\n'.join(fixed_lines)

    # Reconstruct file
    new_content = f"---\n{front_matter}---\n{fixed_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    items_dir = Path('/Users/estiens/code/garagesale/friends-sale/content/items')

    print("Fixing indentation...\n")

    count = 0
    for filepath in sorted(items_dir.glob('*.md')):
        if fix_file_indentation(filepath):
            print(f"✓ Fixed {filepath.name}")
            count += 1

    print(f"\n✓ Fixed {count} files")

if __name__ == '__main__':
    main()
