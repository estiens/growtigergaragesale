# Friends & Family Garage Sale Site

Static Hugo site for giving friends first dibs on your garage sale items before listing publicly.

## Quick Start

```bash
# Navigate to the Hugo site
cd friends-sale

# Start the Hugo development server
hugo server -D

# Open in your browser
# http://localhost:1313
```

The site will auto-reload as you make changes!

## Project Structure

```
friends-sale/
├── content/
│   ├── items/          # All 25 sale items (auto-converted from markdown)
│   └── books/          # Book listings (add your ~500 books here)
├── layouts/
│   ├── _default/       # Base templates
│   ├── items/          # Item listing pages
│   └── books/          # Book listing pages
├── static/
│   └── css/           # Styling
└── hugo.toml          # Site configuration
```

## Adding Photos

To add photos to items:

1. Add images to `friends-sale/static/images/`
2. Edit the item markdown in `friends-sale/content/items/`
3. Add to front matter:
   ```yaml
   image: "/images/your-photo.jpg"
   ```

## Adding Books

Your ~500 books can be added in two ways:

### Option 1: Individual Files (Best for detailed info)

Create individual markdown files in `content/books/`:

```markdown
---
title: "Book Title"
author: "Author Name"
genre: "fiction"  # or non-fiction, tech, music, etc.
price: "$5"
condition: "Good"
---

Optional description or notes about the book.
```

### Option 2: Bulk Import from CSV (Fastest)

If you have a CSV/spreadsheet of books:

1. Create a CSV with columns: `title,author,genre,price,condition`
2. Run the book import script (create similar to convert_to_hugo.py):

```python
# Example: convert_books.py
import csv
from pathlib import Path

with open('books.csv') as f:
    reader = csv.DictReader(f)
    for i, book in enumerate(reader, 1):
        output = Path(f'friends-sale/content/books/{i:03d}_{book["title"].lower().replace(" ", "_")}.md')
        with open(output, 'w') as out:
            out.write(f"""---
title: "{book['title']}"
author: "{book['author']}"
genre: "{book.get('genre', 'other')}"
price: "{book.get('price', '$5')}"
condition: "{book.get('condition', 'Good')}"
---
""")
```

## Deployment Options

### Option 1: Netlify (Recommended - Easiest)

1. Push this repo to GitHub
2. Go to [netlify.com](https://netlify.com)
3. Click "Add new site" → "Import an existing project"
4. Connect to your GitHub repo
5. Build settings:
   - Build command: `hugo`
   - Publish directory: `public`
6. Deploy!

Your site will be live at `https://your-site.netlify.app`

### Option 2: GitHub Pages

```bash
# Build the site
cd friends-sale
hugo

# The site is in public/ directory
# Push public/ to gh-pages branch or use GitHub Actions
```

### Option 3: Simple File Sharing (No Server)

```bash
# Build the site
cd friends-sale
hugo

# Zip the public directory
cd public
zip -r ../friends-sale-site.zip .

# Share the zip file via Dropbox/Google Drive
# Friends extract and open index.html in browser
```

### Option 4: Local Only

Just run `hugo server` and share your local network URL with friends on same WiFi!

## Customization

### Change Colors

Edit `friends-sale/static/css/style.css` (top of file):

```css
:root {
    --primary: #2563eb;      /* Main blue color */
    --secondary: #7c3aed;    /* Purple accents */
    --success: #059669;      /* Price color */
    --warning: #d97706;      /* Warning badges */
}
```

### Update Contact Info

Edit the footer in `friends-sale/layouts/_default/baseof.html`:

```html
<footer>
    <div class="container">
        <p>Text me at (555) 123-4567 or email me@email.com to claim items!</p>
    </div>
</footer>
```

### Modify Welcome Message

Edit `friends-sale/layouts/index.html` hero section.

## Features

- ✅ Clean, mobile-friendly design
- ✅ All 25 items converted with proper metadata
- ✅ Filter by priority (high/medium)
- ✅ Filter by shipping (can ship / local only)
- ✅ Search functionality for books
- ✅ Category badges
- ✅ Fast static site (no database needed)
- ✅ Easy to deploy anywhere

## Next Steps

1. ✅ Site structure created
2. ✅ All 25 items converted
3. ⏭️ Add your photos to items
4. ⏭️ Add your ~500 books
5. ⏭️ Update contact info in footer
6. ⏭️ Test locally with `hugo server`
7. ⏭️ Deploy to Netlify/GitHub Pages
8. ⏭️ Share link with friends!

## Pro Tips

- **Preview before sharing**: Run `hugo server` and check everything looks good
- **Add photos later**: Site works fine with placeholders, add photos as you take them
- **Batch photo updates**: Drop all photos in `static/images/`, then bulk-edit front matter
- **Mark as sold**: Edit item front matter to add `sold: true` and they'll show as sold
- **Time-limited**: After friends get first dibs, just take the site down

---

Have fun! 🎉
