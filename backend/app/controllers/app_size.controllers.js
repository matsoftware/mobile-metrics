const db = require("../models");
const AppSize = db.AppSize;

// Create and Save a new AppSize
exports.create = (req, res) => {
  // Validate request
  if (!req.body.name) {
    res.status(400).send({
      message: "Content can not be empty!"
    });
    return;
  }

  // Create a AppSize
  const appSize = {
    name: req.body.name,
    total_uncompressed_size: req.body.total_uncompressed_size,
    total_universal_size: req.body.total_universal_size
  };

  // Save AppSize in the database
  AppSize.create(appSize)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the Tutorial."
      });
    });
};

// Retrieve all AppSizes from the database.
exports.findAll = (req, res) => {
  
};

// Find a single AppSize with an id
exports.findOne = (req, res) => {
  
};

// Update a AppSize by the id in the request
exports.update = (req, res) => {
  
};

// Delete a AppSize with the specified id in the request
exports.delete = (req, res) => {
  
};

// Delete all AppSizes from the database.
exports.deleteAll = (req, res) => {
  
};

// Find all published AppSizes
exports.findAllPublished = (req, res) => {
  
};