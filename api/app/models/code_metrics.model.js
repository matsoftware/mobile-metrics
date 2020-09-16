module.exports = (sequelize, Sequelize) => {
    const CodeMetrics = sequelize.define("code_metrics", {
      name: {
        type: Sequelize.STRING,
        allowNull: false
      },
      deps_test_loc: {
        type: Sequelize.INTEGER,
        allowNull: true
      },
      deps_prod_loc: {
        type: Sequelize.INTEGER,
        allowNull: true
      },
      repo_test_loc: {
        type: Sequelize.INTEGER,
        allowNull: false
      },
      repo_prod_loc: {
        type: Sequelize.INTEGER,
        allowNull: false
      },
      repo_dupl_loc: {
        type: Sequelize.INTEGER,
        allowNull: true
      },
      internal_deps: {
        type: Sequelize.INTEGER,
        allowNull: true
      },
      external_deps: {
        type: Sequelize.INTEGER,
        allowNull: true
      },
      metadata: {
        type: Sequelize.STRING,
        allowNull: true
      }
    });
  
    return CodeMetrics;
  };