import os, sys

phone = os.environ.get('PHONE_NUMBER', '').strip()
if not phone:
    print("No PHONE_NUMBER secret set, skipping.")
    sys.exit(0)

# LaTeX files — replace \newcommand{\myphone}{} placeholder
latex_files = [
    'lucka_valtriani_cv_other_fr.tex',
    'lucka_valtriani_cv_backend_fr.tex',
    'lucka_valtriani_cv_short_fr.tex',
    'lucka_valtriani_cv_long_fr.tex',
]

latex_marker = r'\newcommand{\myphone}{}'
latex_replacement = r'\newcommand{\myphone}{' + phone + r'\quad--\quad}'

for path in latex_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if latex_marker not in content:
        print(f"ERROR: marker not found in {path}")
        sys.exit(1)
    content = content.replace(latex_marker, latex_replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Phone injected into {path}.")

# cv_design.html — replace <!-- PHONE_PLACEHOLDER --> with a contact list item
design_path = 'lucka_valtriani_cv_design.html'
design_marker = '<!-- PHONE_PLACEHOLDER -->'
design_replacement = f'<li><span class="dot"></span>{phone}</li>'

with open(design_path, 'r', encoding='utf-8') as f:
    content = f.read()
if design_marker not in content:
    print(f"ERROR: marker not found in {design_path}")
    sys.exit(1)
content = content.replace(design_marker, design_replacement, 1)
with open(design_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Phone injected into {design_path}.")

# cv_web.html — replace <!-- PHONE_CHIP_PLACEHOLDER --> with a contact chip link
phone_clean = phone.replace(' ', '').replace('.', '').replace('-', '')
phone_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.62 12 19.79 19.79 0 0 1 1.54 3.24 2 2 0 0 1 3.52 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.63a16 16 0 0 0 6.29 6.29l.61-.61a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 17"/></svg>'
web_path = 'lucka_valtriani_cv_web.html'
web_marker = '<!-- PHONE_CHIP_PLACEHOLDER -->'
web_replacement = f'<a href="tel:{phone_clean}" class="contact-chip">{phone_svg}{phone}</a>'

with open(web_path, 'r', encoding='utf-8') as f:
    content = f.read()
if web_marker not in content:
    print(f"ERROR: marker not found in {web_path}")
    sys.exit(1)
content = content.replace(web_marker, web_replacement, 1)
with open(web_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Phone injected into {web_path}.")
