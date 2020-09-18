const db = require("../models");
const AppSize = db.AppSize;
const Op = db.Sequelize.Op;

// Create and Save a new AppSize
exports.create = (req, res) => {
  // Save AppSize in the database
  AppSize.create(req.body)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the AppSize."
      });
    });
};

// Retrieve all AppSizes from the database.
exports.findAll = (req, res) => {
  const name = req.query.name;
  var condition = name ? { name: { [Op.like]: `%${name}%` } } : null;

  AppSize.findAll({ where: condition, order: [ ['createdAt',  'ASC'] ] })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving AppSizes."
      });
    });
};

// Find a single AppSize with an id
exports.findOne = (req, res) => {
  const id = req.params.id;

  AppSize.findByPk(id)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message: "Error retrieving AppSize with id=" + id
      });
    });
};

// Update a AppSize by the id in the request
exports.update = (req, res) => {
  const id = req.params.id;

  AppSize.update(req.body, {
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "AppSize was updated successfully."
        });
      } else {
        res.send({
          message: `Cannot update AppSize with id=${id}. Maybe AppSize was not found or req.body is empty`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating AppSize with id=" + id
      });
    });
};

// Delete a AppSize with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.id;

  AppSize.destroy({
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "AppSize was deleted successfully!"
        });
      } else {
        res.send({
          message: `Cannot delete AppSize with id=${id}. Maybe AppSize was not found.`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Could not delete AppSize with id=" + id
      });
    });
};