# CV LaTeX

Ce depot contient mon CV en LaTeX, avec compilation automatique en PDF et creation de releases GitHub a chaque modification des fichiers .tex sur la branche principale.

## Pourquoi ce projet

Le but est de rendre mon CV fiable, tracable et facile a partager. Chaque modification genere automatiquement un PDF et une release versionnee, ce qui me permet de garder un historique clair des versions et d'envoyer rapidement le dernier CV a jour, sans manip manuelle.

## Contenu

- CV principal : `lucka_valtriani_cv_short_fr.tex`
- Workflow CI : `.github/workflows/release-cv.yml`
- Fichier de stamp genere par la CI : `cv_updated.inc` (ne pas versionner)

## Prerequis locaux

- TeX Live (ou MikTeX)
- latexmk

Verification rapide :

```bash
latexmk -v
pdflatex -version
```

## Compiler en local

Depuis la racine du depot :

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error lucka_valtriani_cv_short_fr.tex
```

Le PDF est genere a cote du .tex. En local, l indicateur de mise a jour affiche `compilation locale`.

Nettoyer les artefacts :

```bash
latexmk -C
```

## CI / Releases GitHub

Le workflow :

- Se declenche uniquement si un fichier `.tex` change sur la branche `main`.
- Genere un stamp de date/heure Paris : `cv_updated.inc`.
- Compile tous les `.tex` en PDF.
- Cree une release GitHub avec tous les PDFs generes.

Nom de release (exemple) :

```
CV UPDATED: 30/04/2026 18:22 (Paris time)
```

Tag de release (exemple) :

```
cv-20260430-182200-1a2b3c4
```

## Ajouter un nouveau CV (.tex)

1. Ajoute un nouveau fichier `.tex` a la racine (ou adapte le workflow si tu changes de dossier).
2. La CI le compilera automatiquement et attachera le PDF a la release.

## Personnaliser le format de date

Le format est defini dans `.github/workflows/release-cv.yml` via la variable `ts_human`.
Si tu veux un format different (ex: `30 avril 2026 a 18h22`), modifie :

```bash
TZ=Europe/Paris date +"%d/%m/%Y %H:%M"
```

## Problemes courants

- Le workflow echoue en essayant de compiler un fichier non-CV : verifie que seuls tes CV sont en `.tex`.
- Polices manquantes : installe un TeX Live complet ou ajoute les paquets requis.

