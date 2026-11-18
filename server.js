const express = require("express");
const { exec } = require("child_process");
const app = express();
app.get("/calc", (req, res) => res.send(String(eval(req.query.expr))));
app.get("/ping", (req, res) => exec("ping -c 1 " + req.query.host, (e, out) => res.send(out)));
app.get("/go", (req, res) => res.redirect(req.query.next));
app.listen(3000);
