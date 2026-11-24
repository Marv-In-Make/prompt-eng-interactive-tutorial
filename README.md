# Tutoriel interactif de prompt engineering d'Anthropic (version française)

> Traduction française du [tutoriel officiel d'Anthropic](https://github.com/anthropics/prompt-eng-interactive-tutorial). La version originale en anglais est conservée dans [README.en.md](README.en.md).
>
> **Périmètre de la traduction :** le dossier `Anthropic 1P` (API Anthropic directe) est traduit : explications, consignes, commentaires du code et indices (`hints.py`). Le code et les prompts des exemples et des exercices restent en anglais, car les fonctions de correction automatique recherchent des mots anglais précis dans les réponses de Claude. Les indices traduits indiquent, pour chaque exercice, ce que le correcteur attend. Le dossier `AmazonBedrock` n'est pas traduit.

## Présentation et objectifs du cours

Ce cours vise à vous donner une compréhension complète, étape par étape, de la conception de prompts optimaux pour Claude.

**À la fin de ce cours, vous saurez :**
- maîtriser la structure de base d'un bon prompt ;
- reconnaître les erreurs courantes et appliquer les techniques « 80/20 » pour les corriger ;
- comprendre les forces et les faiblesses de Claude ;
- construire de solides prompts de A à Z pour des cas d'usage courants.

## Structure et contenu du cours

Le cours vous donne de nombreuses occasions de vous entraîner à rédiger et corriger des prompts par vous-même. Il se compose de **9 chapitres accompagnés d'exercices**, et d'une annexe consacrée à des méthodes plus avancées. Il est conçu pour être **suivi dans l'ordre des chapitres**.

**Chaque leçon comporte un « Espace de test »** en bas de page, où vous pouvez expérimenter librement avec les exemples et constater par vous-même l'effet d'une modification du prompt sur les réponses de Claude. Un [corrigé](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing) (en anglais) est également disponible.

Note : ce tutoriel utilise notre modèle le plus petit, le plus rapide et le moins cher, Claude 3 Haiku. Anthropic propose [d'autres modèles](https://docs.anthropic.com/claude/docs/models-overview), plus intelligents que Haiku. Vous pouvez modifier la variable `MODEL_NAME` dans le notebook 00 pour utiliser un modèle plus récent.

*Ce tutoriel existe aussi sur [Google Sheets avec l'extension Claude for Sheets d'Anthropic](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing) (en anglais).*

Pour commencer, ouvrez `Anthropic 1P/00_Tutorial_How-To.ipynb`, puis `01_Basic_Prompt_Structure.ipynb`.

## Sommaire

Chaque chapitre comprend une leçon et une série d'exercices.

### Débutant
- **Chapitre 1 :** structure de base d'un prompt

- **Chapitre 2 :** être clair et direct

- **Chapitre 3 :** attribuer un rôle

### Intermédiaire
- **Chapitre 4 :** séparer les données des instructions

- **Chapitre 5 :** formater la sortie et parler à la place de Claude

- **Chapitre 6 :** réfléchir avant de répondre (raisonnement pas à pas)

- **Chapitre 7 :** utiliser des exemples

### Avancé
- **Chapitre 8 :** éviter les hallucinations

- **Chapitre 9 :** construire des prompts complexes (cas d'usage métier)
  - Prompts complexes de A à Z : chatbot
  - Prompts complexes pour les services juridiques
  - **Exercice :** prompts complexes pour les services financiers
  - **Exercice :** prompts complexes pour le code
  - Félicitations et prochaines étapes

- **Annexe :** au-delà du prompt classique
  - Chaîner les prompts
  - Utilisation d'outils (tool use)
  - Recherche et récupération d'informations

## Démarrage rapide

```bash
git clone https://github.com/Marv-In-Make/prompt-eng-interactive-tutorial.git
cd prompt-eng-interactive-tutorial
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic jupyter
export ANTHROPIC_API_KEY="votre_clé"   # ne jamais versionner la clé
jupyter notebook "Anthropic 1P"
```

Dans le notebook 00, remplacez `API_KEY = "your_api_key_here"` par `API_KEY = os.environ["ANTHROPIC_API_KEY"]` (après `import os`) pour lire la clé depuis l'environnement.
