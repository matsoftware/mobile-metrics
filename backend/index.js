require('dotenv').config()
const express = require('express');
const bodyParser = require("body-parser");
const db = require("./app/models");
const passport = require('passport')
const auth = require('./app/config/passport.js')

// APP INIT
const app = express();

// Parse requests of content-type - application/json
app.use(bodyParser.json());

// Parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// Authorization
app.use(passport.initialize())
app.use(auth)

// ROUTES

require("./app/routes/app_size.routes")(app);
require("./app/routes/code_metrics.routes")(app);

app.get('/', (req, res) => {
  res.send(`<h1>Welcome to mobile-metrics interface ${req.body.user}</h1>`);
})

// START

db.sequelize.sync();

const PORT = process.env.SERVER_PORT || 8080;
app.listen(PORT, function() {
    console.log(`listening on ${PORT}`)
})