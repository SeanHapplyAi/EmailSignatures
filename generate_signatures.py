
import os
import re

template_path = '/Users/seanmuir/Code/EmailSignatures/signature.html'
with open(template_path, 'r') as f:
    template_content = f.read()

employees = [
    {"name": "Thierry Lindor", "title": "Co-Founder // CEO"},
    {"name": "Sean Muir", "title": "Co-Founder // CPO"},
    {"name": "Dinesh Pushparajah", "title": "Co-Founder // CTO"},
    {"name": "Anthony Nuoci", "title": "Senior Developer // Partner"},
    {"name": "Rosie Farokhi", "title": "Senior Product Manager"},
    {"name": "Yevgeniy Akimenko", "title": "Software Engineer"},
    {"name": "Amal El Guendouz", "title": "Marketing & Operations Lead"},
    {"name": "Syranda Raffoul", "title": "Grant & Funding Strategist"},
    {"name": "Arman Rokni", "title": "Product Designer"},
    {"name": "Ravitha Loganathan", "title": "Operations Coordinator"},
    {"name": "Ahmaad Ansari", "title": "Full Stack Engineer"}
]

def sanitize_filename(name):
    return name.lower().replace(" ", "-")

for emp in employees:
    name = emp["name"]
    title = emp["title"]
    
    filename = f"esign-{sanitize_filename(name)}.html"
    
    # Replace Name (matches line 22)
    # We look for the div containing "Sean Anthony Muir"
    new_content = re.sub(
        r'(<div[^>]*style="[^"]*font-size: 12px;[^"]*">)\s*Sean Anthony Muir\s*(</div>)',
        r'\1' + name + r'\2',
        template_content
    )
    
    # Replace Title (matches line 25)
    # We look for the div containing "CPO & Co-founder"
    new_content = re.sub(
        r'(<div[^>]*style="[^"]*font-size: 11px;[^"]*">)\s*CPO & Co-founder\s*(</div>)',
        r'\1' + title + r'\2',
        new_content
    )
    
    output_path = os.path.join('/Users/seanmuir/Code/EmailSignatures', filename)
    with open(output_path, 'w') as f:
        f.write(new_content)
    print(f"Generated: {filename}")
