#!/usr/bin/env python3
"""
Fix Hugo content structure - move seller_notes from front matter to content area
"""

import os
import re
from pathlib import Path

def fix_item_file(filepath):
    """Move seller_notes from front matter to markdown content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has seller_notes in front matter
    if 'seller_notes:' not in content:
        print(f"✓ Skipping {Path(filepath).name} (no seller_notes)")
        return

    # Split into front matter and content
    parts = content.split('---\n')
    if len(parts) < 3:
        print(f"⚠ Warning: {Path(filepath).name} has unexpected structure")
        return

    front_matter = parts[1]
    existing_content = '---\n'.join(parts[2:]).strip()

    # Extract seller_notes from front matter
    seller_notes_match = re.search(r'seller_notes:\s*\|\n((?:  .*\n)*)', front_matter)

    if not seller_notes_match:
        print(f"⚠ Warning: Could not extract seller_notes from {Path(filepath).name}")
        return

    seller_notes = seller_notes_match.group(1)
    # Remove the 2-space indentation from each line
    seller_notes = '\n'.join(line[2:] if line.startswith('  ') else line
                             for line in seller_notes.split('\n'))
    seller_notes = seller_notes.strip()

    # Remove seller_notes from front matter
    front_matter = re.sub(r'seller_notes:\s*\|\n((?:  .*\n)*)', '', front_matter)
    front_matter = front_matter.strip()

    # Reconstruct file with content after front matter
    new_content = f"---\n{front_matter}\n---\n\n{seller_notes}\n"

    # Add any existing content that was already after the front matter
    if existing_content:
        new_content += f"\n{existing_content}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Fixed {Path(filepath).name}")

def main():
    items_dir = Path('/Users/estiens/code/garagesale/friends-sale/content/items')

    if not items_dir.exists():
        print(f"Error: {items_dir} not found")
        return

    print("Fixing content structure...\n")

    for filepath in sorted(items_dir.glob('*.md')):
        fix_item_file(filepath)

    print("\n✓ All files processed")

if __name__ == '__main__':
    main()
