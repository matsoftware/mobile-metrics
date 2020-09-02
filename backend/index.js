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

const PORT = process.env.SERVER_PORT || 8080;
app.listen(PORT, function() {
    console.log(`listening on ${PORT}`)
})

// ROUTES

app.get('/', (req, res) => {

  try {
    db.sequelize.sync();
    res.send('Connection has been established successfully.');
  } catch (error) {
    res.send('Unable to connect to the database:', error);
  }  
})