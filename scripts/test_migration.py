from pymongo import MongoClient
import os

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/hospital_db")
client = MongoClient(mongo_uri)
db = client["hospital_db"]
collection = db["patients"]

# Test 1 : vérifier le nombre de documents
count = collection.count_documents({})
print(f"Nombre de documents dans la collection: {count}")

# Test 2 : vérifier doublons sur le champ Name
pipeline = [
    {"$group": {"_id": "$Name", "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}
]
duplicates = list(collection.aggregate(pipeline))
print(f"Doublons détectés: {len(duplicates)}")

# Test 3 : vérifier que toutes les colonnes sont présentes
expected_fields = [
    "Name","Age","Gender","Blood Type","Medical Condition",
    "Date of Admission","Doctor","Hospital","Insurance Provider",
    "Billing Amount","Room Number","Admission Type","Discharge Date",
    "Medication","Test Results"
]
sample_doc = collection.find_one()
missing_fields = [f for f in expected_fields if f not in sample_doc]
print(f"Champs manquants dans la collection: {missing_fields}")

# Test 4 : vérifier types
if isinstance(sample_doc["Age"], int) and isinstance(sample_doc["Billing Amount"], float):
    print("Les types Age et Billing Amount sont corrects.")
else:
    print("Erreur de typage détectée.")
