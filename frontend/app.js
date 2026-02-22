const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("views"));

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/views/form.html");
});

app.post("/submit", async (req, res) => {
    try {
        const response = await axios.post("http://backend:5000/submittodoitem", req.body);
        res.send(response.data);
    } catch (err) {
        res.status(500).send("Error: " + err.message);
    }
});

app.listen(3000, () => {
    console.log("Frontend running on port 3000");
});