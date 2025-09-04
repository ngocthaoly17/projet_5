db = db.getSiblingDB("hospital_db");


db.createUser({
  user: "admin",
  pwd: "admin_password123",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "dbAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" }
  ]
});


db.createUser({
  user: "data_engineer",
  pwd: "de_password123",
  roles: [
    { role: "readWrite", db: "hospital_db" }
  ]
});


db.createUser({
  user: "analyst",
  pwd: "analyst_password123",
  roles: [
    { role: "read", db: "hospital_db" }
  ]
});
