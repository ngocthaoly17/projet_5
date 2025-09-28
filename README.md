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
└── docker-compose.yml
└── mongo-init.js
└── README.md


```

⚡ Installation & Lancement
1. Cloner le projet
```bash
git clone https://github.com/ton-compte/projet_5.git
cd projet_5
```

3. Lancer les conteneurs Docker
```bash
docker-compose build --no-cache

docker-compose up

```

Cela va lancer :

mongodb (base de données)

migrator (script Python qui lit le CSV et alimente MongoDB)

N documents insérés dans MongoDB

3. Se connecter au conteneur MongoDB :

```bash
docker exec -it mongodb mongosh
```

4. Tester un rôle

```bash
docker exec -it mongodb mongosh -u admin -p admin_password123 --authenticationDatabase hospital_db

docker exec -it mongodb mongosh -u data_engineer -p de_password123 --authenticationDatabase hospital_db

docker exec -it mongodb mongosh -u analyst -p analyst_password123 --authenticationDatabase hospital_db

```

Puis dans mongosh :
```bash
show dbs
use hospital_db
show collections
db.patients.findOne()
```

🛠️ Environnement

Python 3.x
Pandas
PyMongo
Docker & Docker Compose
MongoDB

📌 Notes

Assurez-vous que le CSV healthcare_dataset.csv est bien présent dans le dossier csv/.
