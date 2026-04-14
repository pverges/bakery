# Vergés Home Bakery

A minimal, elegant home bakery website with public store and private recipe section.

## Quick Start

```bash
cd verges-bakery
npm install
npm run dev
```

## Build & Deploy

```bash
npm run build
```

Output is in the `dist` folder.

## GitHub Pages Deployment

1. Create a new GitHub repository
2. Push the `dist` folder contents to the `gh-pages` branch, OR
3. In GitHub repo settings, enable GitHub Pages from the `dist` folder

### Option 1: GitHub Actions (Recommended)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

## Updating Products

Edit `src/data/products.json`:

```json
{
  "products": [
    {
      "id": "sourdough",
      "name": "Sourdough Bread",
      "price": 8,
      "ingredients": ["flour", "water", "salt", "sourdough starter"],
      "tags": ["vegan"]
    }
  ]
}
```

## Pre-Order Setup

1. Create a Google Form with fields:
   - Name (text)
   - Email (email)
   - Product (dropdown)
   - Quantity (number)

2. In the confirmation message, add your payment link:
   ```
   Thank you! Please pay 50% deposit ($X) via:
   https://paypal.me/yourusername/X
   ```

3. Update the link in `src/App.vue`:
   ```js
   googleFormUrl: 'YOUR_GOOGLE_FORM_URL'
   ```

## Private Recipes Page

The `/recipes.html` page is:
- Hidden from search engines (noindex meta tag)
- Not linked from the main store
- Only accessible via direct URL

## Files Structure

```
verges-bakery/
├── index.html          # Dev entry (Vue)
├── recipes.html      # Private recipes
├── src/
│   ├── main.js     # Vue entry
│   ├── App.vue     # Public store component
│   ├── style.css   # Design system
│   └── data/
│       └── products.json
├── public/
│   └── robots.txt  # SEO blocking
└── dist/           # Built output
```

## Design

- **Fonts:** Playfair Display (headings), Inter (body)
- **Colors:** Cream (#FDFBF7), Gold accent (#C4A77D)
- **Tags:** Vegan (sage #7A9E7E), Vegetarian (terracotta #D4A574)