print("Create default service user");
db.getSiblingDB("fukuauth").runCommand({
  createUser: "fuku_api",
  pwd: "<CHANGEME>",
  roles: [
    { role: "readWrite", db: "fukuauth" },
  ],
});
