# 🏥 Migration MongoDB avec Docker

Ce projet permet de **migrer un dataset CSV de patients vers une base MongoDB** en utilisant **Pandas** et **PyMongo**, le tout orchestré avec **Docker Compose**.

---

## ✨ Fonctionnalités

- Chargement d’un CSV contenant des données médicales.  
- Nettoyage des données :  
  - Suppression des doublons  
  - Gestion des valeurs manquantes  
- Mise en forme des noms (**Title Case**)  
- Conversion des types :  
  - `Age` → int  
  - `Billing Amount` → float  
- Insertion des données dans **MongoDB** :  
  - Base `hospital_db`  
  - Collection `patients`

---

## 📂 Structure du projet

```text
projet_5/
├── docker-compose.yml
├── requirements.txt
├── scripts/
│   └── migration.py
└── csv/
    └── healthcare_dataset.csv
```

⚡ Installation & Lancement
1. Cloner le projet
git clone https://github.com/ton-compte/projet_5.git
cd projet_5

2. Lancer les conteneurs Docker
docker-compose up --build


Cela va lancer :

mongodb (base de données)

migrator (script Python qui lit le CSV et alimente MongoDB)

3. Vérifier les logs

Si tout se passe bien, tu verras :

N documents insérés dans MongoDB

🧐 Vérifier la base MongoDB

Se connecter au conteneur MongoDB :

docker exec -it mongodb mongosh


Puis dans mongosh :

show dbs
use hospital_db
show collections
db.patients.findOne()

🛠️ Environnement

Python 3.x

Pandas

PyMongo

Docker & Docker Compose

MongoDB

📌 Notes

Assurez-vous que le CSV healthcare_dataset.csv est bien présent dans le dossier csv/.

Le script supprime toutes les données existantes dans la collection patients avant d’insérer les nouvelles données.
