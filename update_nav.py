import os
import re

nav_items = [
    ("index.html", "Home"),
    ("experience.html", "Experience"),
    ("case-studies.html", "Case Studies"),
    ("projects.html", "Personal Builds"),
    ("services.html", "Where I Add Value"),
    ("about.html", "About"),
    ("contact.html", "Contact")
]

def update_nav(filepath):
    is_subdir = '\\' in filepath or '/' in filepath
    prefix = "../" if is_subdir else ""
    
    filename = os.path.basename(filepath)
    if is_subdir and "experience" in filepath:
        active_page = "experience.html"
    elif is_subdir and "projects" in filepath:
        active_page = "projects.html"
    else:
        active_page = filename
        
    new_nav = '      <ul class="nav-links" id="navLinks">\n'
    for link, name in nav_items:
        href = prefix + link
        active_str = ' class="active"' if link == active_page else ''
        new_nav += f'        <li><a href="{href}"{active_str}>{name}</a></li>\n'
    new_nav += '      </ul>'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'<ul class="nav-links" id="navLinks">.*?</ul>', re.DOTALL)
    
    # Check if there's a match before replacing
    if not pattern.search(content):
        # some files might have different indentation, let's try broader
        pattern = re.compile(r'<ul class="nav-links" id="navLinks">.*?</ul>', re.DOTALL)
        
    new_content = pattern.sub(new_nav, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav in {filepath}")

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            # Ignore files in .gemini or similar
            if '.gemini' in root or '.git' in root:
                continue
            update_nav(os.path.join(root, f).replace('.\\', ''))
