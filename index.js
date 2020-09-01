require('dotenv').config()
require('./db.js')
const express = require('express');
const { sequelize } = require('./db.js');
const app = express();

app.listen(3000, function() {
    console.log('listening on 3000')
})

app.get('/', (req, res) => {

  try {
    sequelize.authenticate();
    res.send('Connection has been established successfully.');
  } catch (error) {
    res.send('Unable to connect to the database:', error);
  }  
})