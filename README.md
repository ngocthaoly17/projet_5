Ce projet permet de migrer un dataset CSV de patients vers une base MongoDB en utilisant Pandas et PyMongo, le tout orchestré avec Docker Compose.

Fonctionnalités

Chargement d’un CSV contenant des données médicales.

Nettoyage des données (suppression des doublons, gestion des valeurs manquantes).

Mise en forme des noms (Title Case).

Conversion des types (Age → int, Billing Amount → float).

Insertion des données dans MongoDB (base hospital_db, collection patients)."# Migration MongoDB avec Docker" 

projet_5/
│── docker-compose.yml
│── requirements.txt
│── scripts/
│   └── migration.py
│── csv/
│   └── healthcare_dataset.csv


Installation & Lancement

Cloner le projet

git clone https://github.com/ton-compte/projet_5.git
cd projet_5


Lancer les conteneurs

docker-compose up --build


Cela va lancer :

mongodb (base de données)

migrator (script Python qui lit le CSV et alimente MongoDB)

Vérifier les logs
Si tout se passe bien, tu verras :

N documents insérés dans MongoDB


Vérifier la base MongoDB

Se connecter au conteneur MongoDB :

docker exec -it mongodb mongosh


Puis :

show dbs
use hospital_db
show collections
db.patients.findOne()
