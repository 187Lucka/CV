import os, sys

phone = os.environ.get('PHONE_NUMBER', '').strip()
if not phone:
    print("No PHONE_NUMBER secret set, skipping.")
    sys.exit(0)

path = 'lucka_valtriani_cv_other_fr.tex'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = r'\newcommand{\myphone}{}'
replacement = r'\newcommand{\myphone}{' + phone + '}'

if marker not in content:
    print(f"ERROR: marker '{marker}' not found in {path}")
    sys.exit(1)

content = content.replace(marker, replacement, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Phone injected ({len(phone)} chars).")
