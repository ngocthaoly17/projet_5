db = db.getSiblingDB("hospital_db");

// Création admin
db.createUser({
  user: "admin",
  pwd: "admin_password123",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "dbAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" }
  ]
});

// Création data engineer
db.createUser({
  user: "data_engineer",
  pwd: "de_password123",
  roles: [
    { role: "readWrite", db: "hospital_db" }
  ]
});

// Création analyst (read-only)
db.createUser({
  user: "analyst",
  pwd: "analyst_password123",
  roles: [
    { role: "read", db: "hospital_db" }
  ]
});
