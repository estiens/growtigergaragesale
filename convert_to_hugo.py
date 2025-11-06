#!/usr/bin/env python3
"""Convert existing markdown listings to Hugo format with front matter"""

import os
import re
from pathlib import Path

# Mapping from original listings to Hugo content
LISTINGS_DIR = Path("listings")
HUGO_CONTENT_DIR = Path("friends-sale/content/items")

# Category and metadata mapping based on item names
ITEM_METADATA = {
    "kitchenaid": {"category": "Kitchen & Home", "priority": "high", "shipping": True},
    "ariel_rider_battery": {"category": "E-Bike Parts", "priority": "high", "shipping": True},
    "rad_power_battery": {"category": "E-Bike Parts", "priority": "high", "shipping": True},
    "boss_rc505": {"category": "Music Production", "priority": "high", "shipping": True},
    "project_turntable": {"category": "Music & Audio", "priority": "high", "shipping": False},
    "tplink_deco": {"category": "Electronics & Tech", "priority": "high", "shipping": True},
    "cricut_maker": {"category": "Crafts & Hobbies", "priority": "high", "shipping": False},
    "ableton_push": {"category": "Music Production", "priority": "high", "shipping": True},
    "vitamix": {"category": "Kitchen & Home", "priority": "high", "shipping": False},
    "lg_dual_inverter": {"category": "Electronics & Tech", "priority": "high", "shipping": False, "local_only": True},
    "sonos_beam_gen2": {"category": "Sonos Audio", "priority": "high", "shipping": True},
    "sonos_sub_mini": {"category": "Sonos Audio", "priority": "high", "shipping": True},
    "sonos_beam_gen1": {"category": "Sonos Audio", "priority": "high", "shipping": True},
    "grizzly_dual_hub": {"category": "E-Bike Parts", "priority": "medium", "shipping": True},
    "looptimus": {"category": "Music Production", "priority": "medium", "shipping": True},
    "boss_dr202": {"category": "Music Production", "priority": "medium", "shipping": True},
    "bachetta_giro": {"category": "Bikes & Transportation", "priority": "medium", "shipping": False, "local_only": True},
    "delonghi": {"category": "Kitchen & Home", "priority": "medium", "shipping": False},
    "stanton_str8100": {"category": "Music & Audio", "priority": "medium", "shipping": False},
    "phish_bakers_dozen": {"category": "Phish Collectibles", "priority": "medium", "shipping": True},
    "phish_curveball": {"category": "Phish Collectibles", "priority": "medium", "shipping": True},
    "sodastream": {"category": "Kitchen & Home", "priority": "medium", "shipping": False},
    "sonos_one_sl": {"category": "Sonos Audio", "priority": "medium", "shipping": True},
    "sonos_five": {"category": "Sonos Audio", "priority": "medium", "shipping": True},
}

def extract_price(content):
    """Extract price from markdown content"""
    match = re.search(r'\*\*\$\[(.*?)\]\*\*', content)
    if match:
        return f"${match.group(1)}"
    return "$[Price TBD]"

def extract_title(content):
    """Extract title from first # heading"""
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if match:
        return match.group(1)
    return "Untitled Item"

def extract_short_description(content):
    """Extract first paragraph after description header"""
    # Find Description section
    desc_match = re.search(r'## Description\s+(.+?)(?=\n\n|\n##)', content, re.DOTALL)
    if desc_match:
        # Get first line/sentence
        desc = desc_match.group(1).strip()
        first_line = desc.split('\n')[0]
        # Remove bold markers
        first_line = re.sub(r'\*\*', '', first_line)
        return first_line[:150]
    return ""

def get_metadata_for_file(filename):
    """Get metadata based on filename"""
    filename_lower = filename.lower()
    for key, metadata in ITEM_METADATA.items():
        if key in filename_lower:
            return metadata
    # Default
    return {"category": "Other", "priority": "medium", "shipping": True}

def convert_markdown_to_hugo(input_path, output_path):
    """Convert a markdown file to Hugo format with front matter"""
    with open(input_path, 'r') as f:
        content = f.read()

    # Extract metadata
    title = extract_title(content)
    price = extract_price(content)
    short_desc = extract_short_description(content)

    # Get category and other metadata
    metadata = get_metadata_for_file(input_path.stem)

    # Remove the first # Title line since it's in front matter
    content = re.sub(r'^# .+\n+', '', content, count=1)

    # Build front matter (no date field - not needed for garage sale)
    front_matter = f"""---
title: "{title}"
price: "{price}"
category: "{metadata['category']}"
priority: "{metadata['priority']}"
shipping: {str(metadata['shipping']).lower()}
"""

    if metadata.get('local_only'):
        front_matter += f"local_only: true\n"

    if short_desc:
        front_matter += f'short_description: "{short_desc}"\n'

    front_matter += "---\n\n"

    # Write Hugo content file
    with open(output_path, 'w') as f:
        f.write(front_matter + content)

    print(f"Converted: {input_path.name} -> {output_path.name}")

def main():
    # Create output directory
    HUGO_CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Convert all numbered markdown files (skip index files)
    for md_file in sorted(LISTINGS_DIR.glob('[0-9]*.md')):
        output_file = HUGO_CONTENT_DIR / md_file.name
        convert_markdown_to_hugo(md_file, output_file)

    print(f"\n✓ Converted {len(list(LISTINGS_DIR.glob('[0-9]*.md')))} items to Hugo format")
    print(f"✓ Output directory: {HUGO_CONTENT_DIR}")

if __name__ == "__main__":
    main()
