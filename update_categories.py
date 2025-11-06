#!/usr/bin/env python3
"""
Update item categories and remove priority field from all items
"""

import os
import re
from pathlib import Path

# Category mapping based on item content
CATEGORY_MAP = {
    # Kitchen
    'kitchenaid': 'Kitchen',
    'vitamix': 'Kitchen',
    'delonghi': 'Kitchen',
    'sodastream': 'Kitchen',

    # Audio (Sonos)
    'sonos': 'Audio',

    # Music Gear
    'boss_rc505': 'Music Gear',
    'boss_dr202': 'Music Gear',
    'ableton': 'Music Gear',
    'looptimus': 'Music Gear',
    'project_turntable': 'Music Gear',
    'stanton': 'Music Gear',

    # Electronics
    'tplink': 'Electronics',
    'lg_dual': 'Electronics',
    'cricut': 'Electronics',

    # E-Bike Parts
    'ariel_rider': 'E-Bike Parts',
    'rad_power': 'E-Bike Parts',
    'grizzly': 'E-Bike Parts',

    # Other
    'bachetta': 'Other',
    'phish': 'Other',
}

def get_category_for_file(filename):
    """Determine category based on filename"""
    filename_lower = filename.lower()

    for key, category in CATEGORY_MAP.items():
        if key in filename_lower:
            return category

    return 'Other'

def update_item_file(filepath):
    """Update a single item file: change category and remove priority"""
    filename = Path(filepath).name
    category = get_category_for_file(filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update category in front matter
    content = re.sub(
        r'category: "[^"]*"',
        f'category: "{category}"',
        content
    )

    # Remove priority line from front matter
    content = re.sub(
        r'\npriority: "[^"]*"\n',
        '\n',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated {filename}: {category}")
    return category

def main():
    items_dir = Path('/Users/estiens/code/garagesale/friends-sale/content/items')

    if not items_dir.exists():
        print(f"Error: {items_dir} not found")
        return

    print("Updating categories and removing priority field...\n")

    # Track categories
    category_counts = {}

    # Process all markdown files
    for filepath in sorted(items_dir.glob('*.md')):
        category = update_item_file(filepath)
        category_counts[category] = category_counts.get(category, 0) + 1

    print(f"\n✓ Updated {len(list(items_dir.glob('*.md')))} items")
    print("\nCategory distribution:")
    for cat, count in sorted(category_counts.items()):
        print(f"  {cat}: {count} items")

if __name__ == '__main__':
    main()
