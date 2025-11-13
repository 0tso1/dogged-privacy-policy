# Dogged: Raw Dogging Practise - Privacy Policy Site

Privacy policy website for the Dogged app, built with Hugo and the Shibui theme.

## Quick Start

### Local Development

```bash
hugo server -D
```

Visit http://localhost:1313/

### Build for Production

```bash
hugo
```

Output will be in the `public/` directory.

## Deployment to GitHub Pages

This site is configured to automatically deploy to GitHub Pages when you push to the `master` branch.

### Setup Instructions

1. **Push this repository to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   git push -u origin master
   ```

2. **Enable GitHub Pages in Repository Settings**
   - Go to your repository on GitHub
   - Click **Settings** > **Pages**
   - Under "Build and deployment" > "Source", select **GitHub Actions**
   - The workflow will automatically run and deploy your site

3. **Your site will be live at:**
   ```
   https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/
   ```

4. **Update baseURL in hugo.toml**
   After you know your GitHub Pages URL, update the `baseURL` in `hugo.toml`:
   ```toml
   baseURL = 'https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/'
   ```

## Site Structure

- `content/` - Markdown content files
  - `_index.md` - Homepage
  - `privacy.md` - Privacy Policy page
- `static/images/` - Static images (app icon)
- `assets/css/` - Custom CSS
- `layouts/_partials/` - Custom layout overrides
- `themes/shibui/` - Shibui theme (git submodule)

## Customization

### Colors
App colors are defined in `assets/css/custom.css` to match the Dogged app theme:
- Background: `#fff6e8` (sandy)
- Text: `#3b0014` (dark red)
- Brutalist design with bold borders and heavy typography

### Header Icon
The app icon in the header is at `static/images/app-icon.png`

## Theme

Using [Shibui](https://github.com/ntk148v/shibui) - a minimalist Hugo theme.

## License

Privacy policy content is specific to Dogged app.
