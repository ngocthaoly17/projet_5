import pandas as pd
from pymongo import MongoClient
import os

# Connexion à MongoDB
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/hospital_db")
client = MongoClient(mongo_uri)
db = client["hospital_db"]
collection = db["patients"]

# Charger le CSV
df = pd.read_csv("../csv/healthcare_dataset.csv")

# Nettoyage
df = df.drop_duplicates(subset=["Name"])        
df = df.fillna("Unknown")                       

# Mise en forme des noms (Première lettre en majuscule, reste en minuscule)
df["Name"] = df["Name"].str.title()

# Cast des types
df["Age"] = df["Age"].astype(int)               
df["Billing Amount"] = df["Billing Amount"].astype(float)

# Insérer les documents dans MongoDB
records = df.to_dict(orient="records")
collection.delete_many({})  
collection.insert_many(records)

print(f"{len(records)} documents insérés dans MongoDB")
