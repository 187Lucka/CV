import os, sys

lettre_type = os.environ.get('LETTRE_TYPE', '').strip()
entreprise  = os.environ.get('ENTREPRISE', '').strip()
poste       = os.environ.get('POSTE', '').strip()

if not lettre_type:
    print("ERROR: LETTRE_TYPE not set"); sys.exit(1)
if not entreprise:
    print("ERROR: ENTREPRISE not set"); sys.exit(1)
if not poste:
    print("ERROR: POSTE not set"); sys.exit(1)

path = f'lucka_valtriani_lettre_{lettre_type}_fr.tex'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "\\newcommand{\\entreprise}{[Nom de l'entreprise]}",
    "\\newcommand{\\entreprise}{" + entreprise + "}"
)
content = content.replace(
    "\\newcommand{\\poste}{[Intitule du poste]}",
    "\\newcommand{\\poste}{" + poste + "}"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Injected into {path}: entreprise='{entreprise}', poste='{poste}'.")
