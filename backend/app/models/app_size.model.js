module.exports = (sequelize, Sequelize) => {
    const AppSize = sequelize.define("app_size", {
      name: {
        type: Sequelize.STRING
      },
      total_uncompressed_size: {
        type: Sequelize.NUMERIC
      },
      total_universal_size: {
        type: Sequelize.NUMERIC
      }
    });
  
    return AppSize;
  };