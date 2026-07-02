# 🎵 Data Storytelling — De la donnée à la voix

Un pipeline qui transforme des résultats d'analyse de données en une **narration audio inspirante**, en combinant analyse de données, génération de texte par LLM et synthèse vocale.

## 💡 Le concept

Et si les statistiques d'un dataset musical n'étaient pas de simples chiffres, mais le point de départ d'une histoire ?

Ce projet part d'une analyse de données sur la **musique et les émotions** (valence et énergie de morceaux de 1921 à 2020) et transforme les résultats en un texte narratif profondément humain — dans le ton d'un discours inspirant — avant de le convertir en voix.

**Pipeline en 3 étapes :**
## 🔎 Les données

L'analyse porte sur l'évolution de la musique entre 1921 et 2020, à travers deux métriques :
- **Valence** : la positivité émotionnelle d'un morceau (0 = triste, 1 = joyeux)
- **Énergie** : l'intensité et la puissance perçue d'un morceau

**Principaux résultats (`remarques.txt`) :**
1. L'année la plus triste de l'histoire musicale est 1921 (valence 0.379) ; parmi les années récentes, 2017 détient ce record (0.416)
2. Les années 2010 forment la décennie la plus triste jamais enregistrée (valence moyenne 0.456)
3. L'énergie musicale a augmenté de 172 % entre 1921 et 2020 — la musique est plus intense, mais pas plus joyeuse
4. Le morceau le plus intensément joyeux du dataset : *"Cosmic Surfin'"* de Yellow Magic Orchestra (1979) ; le plus triste : *"The Bat Pt.2"* de Pat Metheny Group (1982)

## 🤖 Génération du récit

Le fichier `context.txt` contient un **prompt système** détaillé qui donne au modèle le rôle d'un narrateur inspirant (registre proche d'un discours d'Oprah Winfrey) : chaleureux, sincère, jamais sensationnaliste, où les statistiques ne sont jamais énoncées telles quelles mais deviennent le support d'une réflexion humaine plus large (nostalgie, joie, mémoire, résilience).

`main.py` orchestre l'appel à l'API **Groq** (modèle `llama-3.3-70b-versatile`) :
- `context.txt` → message système (rôle et règles d'écriture)
- `remarques.txt` → message utilisateur (les 4 findings à intégrer)
- Le modèle retourne un texte narratif fluide de ~500-700 mots, prêt à être lu à voix haute

## 🎙️ Synthèse vocale

Le texte généré est ensuite converti en audio via **[ElevenLabs](https://elevenlabs.io)**, produisant une narration vocale du récit.

## 🛠️ Stack technique

| Composant | Outil |
|---|---|
| Langage | Python |
| Génération de texte | Groq API (Llama 3.3 70B) |
| Synthèse vocale | ElevenLabs |
| Gestion des secrets | `python-dotenv` (`.env`) |
| Dépendances | listées dans `Outils.txt` |

## 📁 Structure du projet
## ⚙️ Installation

```bash
git clone https://github.com/chahrazedAmar/DATA_Ia-summer-cump.git
cd DATA_Ia-summer-cump
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r Outils.txt
```

Créer un fichier `.env` à la racine avec votre clé API Groq :
## ▶️ Utilisation

```bash
python main.py
```

Le script génère un texte narratif à partir des findings du dataset, à copier ensuite sur [ElevenLabs](https://elevenlabs.io) pour obtenir la version audio.

## 🎯 Compétences mises en œuvre

- Prompt engineering (conception d'un prompt système structuré et contraint)
- Intégration d'API LLM (Groq)
- Data storytelling : traduire des résultats analytiques en récit compréhensible et engageant
- Pipeline multi-outils (analyse → texte → audio)

## 🔭 Pistes d'amélioration

- Ajouter la gestion d'erreurs (fichiers manquants, clé API invalide)
- Automatiser l'appel à l'API ElevenLabs directement depuis le script
- Rendre le nombre de *findings* et le persona du narrateur configurables
