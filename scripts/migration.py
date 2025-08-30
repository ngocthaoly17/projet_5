import pandas as pd
from pymongo import MongoClient
import os

class MongoConnector:
    def __init__(self):
        self.user = os.environ.get("MONGO_USER")
        self.password = os.environ.get("MONGO_PASS")
        self.db_name = os.environ.get("MONGO_DB")
        self.host = os.environ.get("MONGO_HOST", "localhost")
        self.mongo_uri = f"mongodb://{self.user}:{self.password}@{self.host}:27017/{self.db_name}"
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]
        print(f"Connecté à MongoDB en tant que {self.user}")

    def get_collection(self, name):
        return self.db[name]

class PatientCleaner:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load_and_clean(self):
        df = pd.read_csv(self.csv_path)
        initial_rows = len(df)

        df = df.drop_duplicates(subset=["Name"])
        df = df.fillna("Unknown")
        df["Name"] = df["Name"].str.title()
        df["Age"] = df["Age"].astype(int)
        df["Billing Amount"] = df["Billing Amount"].astype(float)

        removed = initial_rows - len(df)
        print(f"Lignes supprimées après suppression des doublons dans le CSV : {removed}")

        self.df = df
        return df

class PatientMigrator:
    def __init__(self, df, collection, user):
        self.df = df
        self.collection = collection
        self.user = user

    def filter_existing(self):
        existing_names = set(doc["Name"] for doc in self.collection.find({}, {"Name": 1, "_id": 0}))
        self.df_new = self.df[~self.df["Name"].isin(existing_names)].copy()
        filtered_out = len(self.df) - len(self.df_new)
        print(f"Lignes déjà présentes dans MongoDB et donc non insérées : {filtered_out}")

    def assign_ids(self):
        if self.df_new.empty:
            self.start_id = None
            return
        last_id_doc = self.collection.find_one(sort=[("_id", -1)])
        self.start_id = last_id_doc["_id"] + 1 if last_id_doc else 1
        self.df_new.reset_index(drop=True, inplace=True)
        self.df_new["_id"] = self.df_new.index + self.start_id

    def insert(self):
        if self.df_new.empty:
            print("Aucun nouveau patient à insérer.")
            return
        records = self.df_new.to_dict(orient="records")
        self.collection.insert_many(records)
        print(f"{len(records)} nouveaux documents insérés dans MongoDB par {self.user}, à partir de l'id {self.start_id}")

    def migrate(self):
        self.filter_existing()
        self.assign_ids()
        self.insert()

# ----------------------------
# Usage
# ----------------------------
if __name__ == "__main__":

    connector = MongoConnector()
    collection = connector.get_collection("patients")

    cleaner = PatientCleaner("../csv/healthcare_dataset.csv")
    df_cleaned = cleaner.load_and_clean()

    migrator = PatientMigrator(df_cleaned, collection, connector.user)
    migrator.migrate()
