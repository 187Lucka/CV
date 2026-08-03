import os, sys

phone = os.environ.get('PHONE_NUMBER', '').strip()
if not phone:
    print("No PHONE_NUMBER secret set, skipping.")
    sys.exit(0)

# LaTeX files
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

# HTML file
html_path = 'lucka_valtriani_cv_design.html'
html_marker = '<!-- PHONE_PLACEHOLDER -->'
html_replacement = f'<li><span class="dot"></span>{phone}</li>'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()
if html_marker not in content:
    print(f"ERROR: marker not found in {html_path}")
    sys.exit(1)
content = content.replace(html_marker, html_replacement, 1)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Phone injected into {html_path}.")
