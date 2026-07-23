import os
import re

# Update projects.html
projects_file = "projects.html"
with open(projects_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the title and intro
content = content.replace("<h1>Personal Projects</h1>", "<h1>Personal Builds & Experiments</h1>")

intro_old = '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                    Beyond enterprise work, I build personal projects to explore new technologies, solve everyday
                    problems, and
                    experiment with innovative solutions. These projects showcase my passion for creating user-centric
                    applications across mobile and web platforms.
                </p>'''

intro_new = '''<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                    These are personal builds and experiments I have used to explore product ideas, AI workflows, user experience, data models and platform thinking.<br><br>
                    Some are prototypes, some are concepts, and some are live builds. They are included here to show how I think, design and build — not to present them as fully commercial products.
                </p>'''

# Some whitespace issues might occur so regex is better
content = re.sub(r'<p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">\s*Beyond enterprise work.*?</p>', intro_new, content, flags=re.DOTALL)

# Add statuses to cards
# We can use regex to inject `<p class="status-label" style="font-size: 0.8rem; color: var(--color-accent-secondary); margin-top: 4px;">Status: Prototype</p>` before the `</a>`
# For specific ones:
statuses = {
    "lead-generator.html": "Prototype",
    "kinpulse.html": "Prototype",
    "moodpulse.html": "Live build",
    "club-management.html": "Live build",
    "opshandover.html": "Concept",
    "spend-approvals.html": "Concept"
}

def inject_status_projects(match):
    full_match = match.group(0)
    href = match.group(1)
    status = statuses.get(href.split('/')[-1], "Personal experiment")
    
    status_html = f'<p class="status-label" style="font-size: 0.8rem; color: var(--color-accent-secondary); margin-top: 4px; margin-bottom: 0;">Status: {status}</p>'
    
    # insert before the closing </a>
    return full_match.replace("</a>", f"    {status_html}\n                </a>")

content = re.sub(r'<a href="(projects/[^"]+)" class="app-card">.*?</a>', inject_status_projects, content, flags=re.DOTALL)

with open(projects_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated projects.html")

# Now update the individual project files
projects_dir = "projects"
for filename in os.listdir(projects_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(projects_dir, filename)
        status = statuses.get(filename, "Personal experiment")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            proj_content = f.read()
            
        context_block = f'''
                <div class="project-context" style="margin-top: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.05); border-radius: 8px; text-align: left; max-width: 600px; margin-left: auto; margin-right: auto; border: 1px solid rgba(255,255,255,0.1);">
                    <p style="margin-bottom: 0.5rem; color: var(--text-primary);"><strong>Status:</strong> <span style="color: var(--color-accent-secondary);">{status}</span></p>
                    <p style="margin-bottom: 0.5rem; color: var(--text-secondary);"><strong>Built to explore:</strong> AI workflows, product thinking, data models and user experience.</p>
                    <p style="margin-bottom: 0; color: var(--text-secondary);"><strong>My role:</strong> Product strategy, architecture, design and build.</p>
                </div>'''
                
        # Insert context block right after <p class="subtitle">...</p>
        proj_content = re.sub(r'(<p class="subtitle">.*?</p>)', r'\1' + context_block, proj_content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(proj_content)
        print(f"Updated {filename}")
