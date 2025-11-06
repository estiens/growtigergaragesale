#!/usr/bin/env python3
"""
Fix missing closing --- in front matter
"""

from pathlib import Path

def fix_front_matter(filepath):
    """Ensure front matter has proper closing ---"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file starts with ---
    if not content.startswith('---\n'):
        return False

    lines = content.split('\n')

    # Find where front matter should end (first empty line after opening ---)
    closing_index = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '' and i > 1:  # Found empty line
            # Check if next line is already ---
            if i+1 < len(lines) and lines[i+1].strip() == '---':
                return False  # Already fixed
            closing_index = i
            break

    if closing_index:
        # Insert --- before the empty line
        lines.insert(closing_index, '---')

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        return True

    return False

def main():
    items_dir = Path('/Users/estiens/code/garagesale/friends-sale/content/items')

    print("Fixing front matter...\n")

    fixed_count = 0
    for filepath in sorted(items_dir.glob('*.md')):
        if fix_front_matter(filepath):
            print(f"✓ Fixed {filepath.name}")
            fixed_count += 1

    print(f"\n✓ Fixed {fixed_count} files")

if __name__ == '__main__':
    main()
