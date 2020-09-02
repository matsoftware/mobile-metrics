require('dotenv').config()
const express = require('express');
const bodyParser = require("body-parser");
const db = require("./app/models");

// APP INIT
const app = express();

// Parse requests of content-type - application/json
app.use(bodyParser.json());

// Parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// ROUTES

require("./app/routes/app_size.routes")(app);

app.get('/', (req, res) => {
  res.send('<h1>Welcome to mobile-metrics interface</h1>');
})

// START

db.sequelize.sync({ force: true });

const PORT = process.env.SERVER_PORT || 8080;
app.listen(PORT, function() {
    console.log(`listening on ${PORT}`)
})