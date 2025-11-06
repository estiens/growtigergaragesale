# Quick Start Guide - Friends Sale Site

## 🚀 Get Your Site Running (2 minutes)

### Step 1: Convert Your Books CSV

```bash
# Make sure your books CSV is named "books.csv" in the main directory
# Or edit convert_books.py to point to your CSV filename

python3 convert_books.py
```

This will convert all your books from the CSV into individual markdown files in `friends-sale/content/books/`.

### Step 2: Start the Hugo Server

```bash
cd friends-sale
hugo server
```

Open your browser to: **http://localhost:1313**

Your site is live! 🎉

---

## 📝 What You Have Now

- ✅ **25 sale items** (all high & medium priority)
- ✅ **~450 books** (from your CSV)
- ✅ Clean, mobile-friendly design
- ✅ Search & filter functionality
- ✅ Sold/Pending status tracking

---

## 🖼️ Adding Photos to Items

1. Put photos in `friends-sale/static/images/`
2. Edit any item file in `friends-sale/content/items/`
3. Add to the front matter (top section):

```yaml
image: "/images/kitchenaid-mixer.jpg"
```

---

## 📚 Managing Books

### Mark a Book as Sold
Edit the book's `.md` file in `friends-sale/content/books/` and change:

```yaml
sold: false
```

to:

```yaml
sold: true
```

### Mark a Book as Pending
```yaml
pending: true
```

The site will automatically:
- Gray out sold books
- Add orange border to pending books
- Show SOLD/PENDING badges
- Filter sold/pending/available books

---

## 🌐 Sharing With Friends

### Option 1: Deploy to Netlify (Recommended)

1. Push this repo to GitHub
2. Go to [netlify.com](https://netlify.com) (free account)
3. "Add new site" → "Import from GitHub"
4. Set build command: `hugo`
5. Set publish directory: `public`
6. Deploy!

You'll get a URL like: `https://your-sale.netlify.app`

**Update books live:** Edit book files in GitHub, commit, and Netlify auto-updates!

### Option 2: Share Local Network

If friends are on your WiFi:

```bash
cd friends-sale
hugo server --bind 0.0.0.0
```

Share the URL shown (like `http://192.168.1.100:1313`)

### Option 3: GitHub Pages

```bash
cd friends-sale
hugo
# Push the 'public' folder to your GitHub repo's gh-pages branch
```

---

## ⚙️ Customization

### Update Contact Info

Edit `friends-sale/layouts/_default/baseof.html` footer section:

```html
<footer>
    <div class="container">
        <p>Text me at (555) 123-4567 or email me@email.com to claim items!</p>
    </div>
</footer>
```

### Change Welcome Message

Edit `friends-sale/layouts/index.html` hero section.

### Change Colors

Edit `friends-sale/static/css/style.css` top section (`:root` variables).

---

## 📋 Book CSV Format Reference

Your CSV should have these columns:
- **Title** (required)
- **Author** (required)
- **Genre** (optional, defaults to "Other")
- **Est Market Value** (becomes price, defaults to $3)
- **Notes** (optional)
- **Status** (optional, "For Sale", "Sold", "Pending")

Other columns (like "Shelf") are ignored.

---

## 🎯 Workflow Tips

1. **Share early:** Share the link even without all photos - friends can text you about items
2. **Update as you go:** Add photos gradually, mark books as pending/sold in real-time
3. **Take it down when done:** After a few days, just stop the server or remove the Netlify site

---

## 🆘 Troubleshooting

**Books not showing up?**
- Check that books.csv is in the main directory
- Run `python3 convert_books.py` again
- Restart hugo server

**Changes not appearing?**
- Hugo auto-reloads but sometimes needs a restart
- Press Ctrl+C and run `hugo server` again

**CSS looks broken?**
- Clear your browser cache (Cmd+Shift+R or Ctrl+Shift+R)

---

## 📁 Project Structure

```
garagesale/
├── books.csv                          # Your books CSV
├── convert_books.py                   # Books converter script
├── convert_to_hugo.py                 # Items converter script
├── listings/                          # Original markdown listings
└── friends-sale/                      # Hugo site
    ├── content/
    │   ├── items/                     # 25 sale items
    │   └── books/                     # ~450 books
    ├── layouts/                       # Templates
    ├── static/
    │   ├── css/style.css              # Styling
    │   └── images/                    # Put photos here
    └── hugo.toml                      # Config
```

---

## ✨ That's It!

You're ready to share with friends. Questions? Check the main README.md for more details.

**Share the link, let friends claim stuff, mark items as sold, done!** 🎉
