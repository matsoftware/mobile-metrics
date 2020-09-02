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
db.sequelize = sequelize;

// MODELS

db.AppSize = require("./app_size.model.js")(sequelize, Sequelize);
db.CodeMetrics = require("./code_metrics.model.js")(sequelize, Sequelize);

module.exports = db;