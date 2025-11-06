#!/usr/bin/env python3
"""Convert books CSV to Hugo markdown files"""

import csv
import re
from pathlib import Path

# Configuration
BOOKS_CSV = "books.csv"  # Your CSV file
HUGO_BOOKS_DIR = Path("friends-sale/content/books")

def sanitize_filename(text, max_length=60):
    """Create safe filename from book title"""
    # Remove special characters, lowercase, replace spaces with underscores
    safe = re.sub(r'[^\w\s-]', '', text.lower())
    safe = re.sub(r'[-\s]+', '_', safe)
    return safe[:max_length]

def map_genre_to_category(genre):
    """Map specific genre to broad category"""
    genre_lower = genre.lower()

    # Fiction
    if any(term in genre_lower for term in ['fiction', 'novel', 'mystery', 'thriller']):
        return 'Fiction'

    # Sci-Fi/Fantasy
    if any(term in genre_lower for term in ['sci-fi', 'science fiction', 'fantasy', 'cyberpunk', 'dystopian']):
        return 'Sci-Fi/Fantasy'

    # Politics/History
    if any(term in genre_lower for term in ['politics', 'political', 'history', 'historical']):
        return 'Politics/History'

    # Philosophy/Religion
    if any(term in genre_lower for term in ['philosophy', 'religion', 'spiritual', 'theology', 'buddhism', 'meditation']):
        return 'Philosophy/Religion'

    # Memoir/Biography
    if any(term in genre_lower for term in ['memoir', 'biography', 'autobiography']):
        return 'Memoir/Biography'

    # Poetry/Essays
    if any(term in genre_lower for term in ['poetry', 'poems', 'essay', 'short stories']):
        return 'Poetry/Essays'

    # Sociology/Psychology
    if any(term in genre_lower for term in ['sociology', 'psychology', 'anthropology', 'social', 'therapy']):
        return 'Sociology/Psychology'

    # Theory/Critical
    if any(term in genre_lower for term in ['theory', 'critical', 'anarchism', 'marxism']):
        return 'Theory/Critical'

    # Environment/Science
    if any(term in genre_lower for term in ['environment', 'ecology', 'climate', 'science', 'nature']):
        return 'Environment/Science'

    # Default
    return 'Other'

def extract_tags(genre):
    """Extract searchable tags from genre"""
    # Keep the original genre as tags for search
    return genre

def convert_books_csv():
    """Convert books CSV to Hugo markdown files"""

    # Create output directory
    HUGO_BOOKS_DIR.mkdir(parents=True, exist_ok=True)

    # Read CSV
    with open(BOOKS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        books = list(reader)

    print(f"Found {len(books)} books in CSV")

    # Filter out books without prices
    books_with_prices = []
    skipped_books = []

    for book in books:
        price = book.get('Est Market Value', '').strip()
        if price and price != '':
            books_with_prices.append(book)
        else:
            skipped_books.append(book)

    print(f"Books with prices: {len(books_with_prices)}")
    print(f"Books without prices (skipped): {len(skipped_books)}")
    if skipped_books:
        print("\nSkipped books (no price):")
        for book in skipped_books[:5]:
            print(f"  - {book['Title']} by {book['Author']}")
        if len(skipped_books) > 5:
            print(f"  ... and {len(skipped_books) - 5} more")

    # Convert each book (only those with prices)
    for i, book in enumerate(books_with_prices, 1):
        title = book['Title'].strip()
        author = book['Author'].strip()
        genre = book.get('Genre', '').strip() or 'Other'
        notes = book.get('Notes', '').strip()
        price = book.get('Est Market Value', '3').strip()
        status = book.get('Status', 'For Sale').strip()

        # Map genre to category and extract tags
        category = map_genre_to_category(genre)
        tags = extract_tags(genre)

        # Convert price to currency
        if price and price != '':
            price_formatted = f"${price}"
        else:
            price_formatted = "$3"

        # Convert status
        status_lower = status.lower()
        sold = 'true' if 'sold' in status_lower else 'false'
        pending = 'true' if 'pending' in status_lower else 'false'

        # Create filename
        filename = f"{i:03d}_{sanitize_filename(title)}.md"
        output_path = HUGO_BOOKS_DIR / filename

        # Build front matter
        front_matter = f"""---
title: "{title}"
author: "{author}"
category: "{category}"
tags: "{tags}"
price: "{price_formatted}"
sold: {sold}
pending: {pending}
weight: {i}
---
"""

        # Add notes as content if present
        content = ""
        if notes and notes != '':
            content = f"\n{notes}\n"

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(front_matter + content)

    print(f"\n✓ Converted {len(books_with_prices)} books to Hugo format")
    print(f"✓ Output directory: {HUGO_BOOKS_DIR}")
    print(f"\nNext steps:")
    print(f"1. Run: cd friends-sale && hugo server")
    print(f"2. Visit: http://localhost:1313/books/")
    print(f"3. To mark books as sold/pending, edit the front matter in the .md files")

    if skipped_books:
        print(f"\nNote: {len(skipped_books)} books without prices were skipped (list elsewhere)")

if __name__ == "__main__":
    convert_books_csv()
