# Everyday Systems

A modern portfolio landing page showcasing creative and innovative solutions for businesses and individuals.

## 🚀 Features

- Modern, responsive design with neutral color palette
- Smooth animations and micro-interactions
- SEO optimized
- Fast loading and performance optimized
- Mobile-first approach
- Accessible and semantic HTML

## 🛠️ Tech Stack

- **HTML5** - Semantic markup
- **CSS3** - Custom design system with CSS variables
- **JavaScript** - Vanilla JS for interactions
- **No frameworks** - Pure, lightweight code

## 📦 Project Structure

```
EverydaySystems/
├── index.html          # Main HTML file
├── styles.css          # Complete design system and styles
├── script.js           # JavaScript functionality
├── assets/             # Images and visual assets
│   ├── hero-visual.png
│   ├── project-1.png
│   ├── project-2.png
│   └── project-3.png
├── package.json        # Project metadata
└── README.md          # This file
```

## 🌐 Local Development

### Option 1: Open directly in browser
Simply open `index.html` in your web browser.

### Option 2: Use a local server (recommended)

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Then visit: http://localhost:8000
```

**Using Node.js:**
```bash
npx serve
```

**Using VS Code:**
Install the "Live Server" extension and right-click on `index.html` → "Open with Live Server"

## 🚀 Deploy to Vercel

### Method 1: Using Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   cd C:\Apps\Fam\EverydaySystems
   vercel
   ```

4. **Follow the prompts:**
   - Set up and deploy? **Yes**
   - Which scope? Select your account
   - Link to existing project? **No**
   - What's your project's name? **everyday-systems** (or your choice)
   - In which directory is your code located? **./** (current directory)
   - Want to override the settings? **No**

5. **Deploy to production:**
   ```bash
   vercel --prod
   ```

### Method 2: Using Vercel Dashboard (Recommended for beginners)

1. **Push to GitHub:**
   ```bash
   cd C:\Apps\Fam\EverydaySystems
   git init
   git add .
   git commit -m "Initial commit: Everyday Systems website"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/everyday-systems.git
   git push -u origin main
   ```

2. **Import to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Click "Deploy"
   - Done! Your site will be live at `https://your-project.vercel.app`

### Method 3: Drag and Drop

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Drag and drop the `EverydaySystems` folder
4. Click "Deploy"

## 🌍 Configure Custom Domain (GoDaddy)

After deploying to Vercel, you'll get a URL like `https://everyday-systems.vercel.app`

### Add Custom Domain in Vercel:

1. Go to your project in Vercel Dashboard
2. Click "Settings" → "Domains"
3. Add your domain (e.g., `yourdomain.com`)
4. Vercel will provide DNS records

### Configure DNS in GoDaddy:

1. **Login to GoDaddy**
2. **Go to "My Products" → "DNS"**
3. **Add the following records:**

   **For root domain (yourdomain.com):**
   - Type: `A`
   - Name: `@`
   - Value: `76.76.21.21` (Vercel's IP)
   - TTL: `600`

   **For www subdomain:**
   - Type: `CNAME`
   - Name: `www`
   - Value: `cname.vercel-dns.com`
   - TTL: `600`

4. **Save changes**
5. **Wait for DNS propagation** (can take up to 48 hours, usually much faster)

### Verify Domain:

1. Back in Vercel, click "Verify" next to your domain
2. Once verified, your site will be live at your custom domain!

## 📝 Customization

### Update Content:
- Edit `index.html` to change text, sections, or structure
- Modify `styles.css` to adjust colors, spacing, or design
- Update `script.js` to add new interactions

### Change Colors:
All colors are defined as CSS variables in `styles.css`. Update the `:root` section:

```css
:root {
  --color-accent-primary: #2d2d2d;  /* Change this */
  --color-accent-secondary: #5a5a5a; /* And this */
  /* etc. */
}
```

### Add New Sections:
Follow the existing HTML structure and use the predefined CSS classes.

## 📧 Contact

For inquiries: hello@everydaysystems.com

## 📄 License

MIT License - feel free to use this template for your own projects!

---

Built with ❤️ by Everyday Systems
