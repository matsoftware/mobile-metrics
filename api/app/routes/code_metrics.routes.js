module.exports = app => {
    const codemetrics = require("../controllers/code_metrics.controllers.js");
  
    var router = require("express").Router();
  
    // Create a new CodeMetrics
    router.post("/", codemetrics.create);
  
    // Retrieve all CodeMetricss
    router.get("/", codemetrics.findAll);
    
    // Retrieve a single CodeMetrics with id
    router.get("/:id", codemetrics.findOne);
  
    // Update a CodeMetrics with id
    router.put("/:id", codemetrics.update);
  
    // Delete a CodeMetrics with id
    router.delete("/:id", codemetrics.delete);
    
    app.use('/api/code_metrics', router);
  };