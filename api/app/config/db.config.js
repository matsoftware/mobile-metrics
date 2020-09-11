module.exports = {
    HOST: process.env.DB_HOST,
    USER: process.env.DB_USER,
    PASSWORD: process.env.DB_PASS,
    DATABASE: 'mobile_metrics',
    PORT: process.env.DB_PORT,
    dialect: 'mssql',
    encrypt: false,
    pool: {
        max: 5,
        min: 0,
        acquire: 30000,
        idle: 10000
    },
    dialectOptions: {
        options: {
            encrypt: false,
        },
    }
}