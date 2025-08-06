db = db.getSiblingDB("fukuauth");

db.init.insertOne({
    createdAt: new Date(),
    message: "Hello there"
});
