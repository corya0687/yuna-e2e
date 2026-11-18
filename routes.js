// Planted for the threat model: a write route and an admin route with no
// authentication, and no rate limit.
const express = require("express");
const app = express();

app.post("/api/notes", (req, res) => {
  db.insert(req.body);
  res.sendStatus(201);
});

app.get("/admin/users", (req, res) => res.json(listUsers()));

module.exports = app;
