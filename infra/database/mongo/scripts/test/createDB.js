db = db.getSiblingDB("fukuauth_test");

db.init.insertOne({
    createdAt: new Date(),
    message: "Hello there"
});
