import os
import re

files = [
    'index.html',
    'offering-all-in-one.html',
    'offering-bootcamp.html',
    'offering-live-project.html',
    'offering-case-comp.html',
    'offering-certifications.html'
]

old_font = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />'
new_font = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />'

for file in files:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update font link
    content = content.replace(old_font, new_font)
    
    # 2. Update inline font-family
    content = content.replace("font-family:'Playfair Display',Georgia,serif;", "")
    content = content.replace("font-family: 'Playfair Display', Georgia, serif;", "")
    
    # 3. Update CSS vars in inline styles
    content = content.replace('var(--gold)', 'var(--yellow)')
    content = content.replace('var(--ivory)', 'var(--bg-main)')
    content = content.replace('var(--panel)', 'var(--bg-panel)')
    
    # 4. Clean up index.html specific duplicated CSS
    if file == 'index.html':
        pattern = re.compile(r'/\* ════════════════════════════════════════════════════════════════\s*DESIGN TOKENS.*?/\* ════════════════════════════════════════════════════════════════\s*01 — STICKY NAV', re.DOTALL)
        content = pattern.sub('/* 01 — STICKY NAV', content)
        
        # Remove other duplicated sections if needed, but since shared.css is linked after, it overrides them as long as specificity is same.
        # Let's remove the whole duplicated modal, footer, faq, mentors, testimonials from index.html's inline styles.
        # They exist in shared.css now.
        content = re.sub(r'/\* ════════════════════════════════════════════════════════════════\s*09 — MENTOR CREDIBILITY WALL.*?</style>', '</style>', content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Mass replacements done.')
