const { Sequelize, Model, DataTypes } = require('sequelize');

const db_config = {
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    server: process.env.DB_HOST,
    database: 'mobile_metrics',
    port: process.env.DB_PORT
}

exports.sequelize = new Sequelize({
    database: db_config.database,
    username: db_config.user,
    password: db_config.password,
    host: db_config.server,
    dialect: 'mssql',
    port: db_config.port,
    encrypt: false,
    dialectOptions: {
        options: {
            encrypt: false,
        },
    }
});