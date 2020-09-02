module.exports = (sequelize, Sequelize) => {
    const AppSize = sequelize.define("app_size", {
      name: {
        type: Sequelize.STRING,
        allowNull: false
      },
      total_uncompressed_size: {
        type: Sequelize.DOUBLE,
        allowNull: false
      },
      total_universal_size: {
        type: Sequelize.DOUBLE,
        allowNull: false
      },
      metadata: {
        type: Sequelize.STRING,
        allowNull: true
      }
    });
  
    return AppSize;
  };