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
    'lucka_valtriani_cv_web_fr.tex',
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
