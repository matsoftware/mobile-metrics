const db = require("../models");
const CodeMetrics = db.CodeMetrics;
const Op = db.Sequelize.Op;

// Create and Save a new CodeMetrics
exports.create = (req, res) => {
  // Save CodeMetrics in the database
  CodeMetrics.create(req.body)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the CodeMetrics."
      });
    });
};

// Retrieve all CodeMetricss from the database.
exports.findAll = (req, res) => {
  const name = req.query.name;
  var condition = name ? { name: { [Op.like]: `%${name}%` } } : null;

  CodeMetrics.findAll({ where: condition, order: [ ['createdAt',  'ASC'] ] })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving CodeMetricss."
      });
    });
};

// Find a single CodeMetrics with an id
exports.findOne = (req, res) => {
  const id = req.params.id;

  CodeMetrics.findByPk(id)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message: "Error retrieving CodeMetrics with id=" + id
      });
    });
};

// Update a CodeMetrics by the id in the request
exports.update = (req, res) => {
  const id = req.params.id;

  CodeMetrics.update(req.body, {
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "CodeMetrics was updated successfully."
        });
      } else {
        res.send({
          message: `Cannot update CodeMetrics with id=${id}. Maybe CodeMetrics was not found or req.body is empty`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating CodeMetrics with id=" + id
      });
    });
};

// Delete a CodeMetrics with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.id;

  CodeMetrics.destroy({
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "CodeMetrics was deleted successfully!"
        });
      } else {
        res.send({
          message: `Cannot delete CodeMetrics with id=${id}. Maybe CodeMetrics was not found.`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Could not delete CodeMetrics with id=" + id
      });
    });
};