1. Installer Python
Téléchargez la dernière version (3.10+) sur python.org/downloads. Sur Windows, cochez "Add Python to PATH" avant de cliquer sur Installer.
 
python --version
 
2. Installer Git
Téléchargez depuis git-scm.com si vous ne l'avez pas encore.
 
git --version
 
3. Créer le dépôt sur GitHub
Allez sur github.com/new et configurez :
•   	Donnez-lui un nom (ex. groq-project)
•   	Définissez-le en Public ou Privé
•   	Cochez "Add a README"
•   	Cochez "Add .gitignore" → sélectionnez Python  ← ignore automatiquement venv/, __pycache__/, etc.
 
4. Cloner le dépôt en local
git clone [votre lien repo ici]
cd [nom repo]
 
5. Créer et activer un environnement virtuel
python -m venv venv

Windows : venv\Scripts\activate
Mac/Linux : source venv/bin/activate
