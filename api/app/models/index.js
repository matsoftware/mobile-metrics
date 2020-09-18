const sequelize_fixtures = require('sequelize-fixtures');
const dbConfig = require("../config/db.config.js");

const Sequelize = require("sequelize");
const sequelize = new Sequelize({
    database: dbConfig.DATABASE,
    username: dbConfig.USER,
    password: dbConfig.PASSWORD,
    host: dbConfig.HOST,
    dialect: dbConfig.dialect,
    port: dbConfig.PORT,
    encrypt: dbConfig.encrypt,
    pool: dbConfig.pool,
    dialectOptions: dbConfig.dialectOptions
});

const db = {};

db.Sequelize = Sequelize;
// MODELS

db.AppSize = require("./app_size.model.js")(sequelize, Sequelize);
db.CodeMetrics = require("./code_metrics.model.js")(sequelize, Sequelize);
db.User = require("./user.model.js")(sequelize, Sequelize);

// FIXTURES

function loadFixtures() {

    models = {
        'AppSize': db.AppSize,
        'CodeMetrics': db.CodeMetrics
    }    

    sequelize_fixtures.loadFiles([
        // Define here the list of fixture files you want to load
        'app/fixtures/app_size.json',
        'app/fixtures/code_metrics.json'
    
    ], models).then(function(){
        // Post-launch actions, if needed
    });    
}

function sync() {
    sequelize.sync().then(loadFixtures)
}

db.sync = sync

// EXPORTS
module.exports = db;