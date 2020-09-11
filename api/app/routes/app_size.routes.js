module.exports = app => {
    const appsize = require("../controllers/app_size.controllers.js");
  
    var router = require("express").Router();
  
    // Create a new AppSize
    router.post("/", appsize.create);
  
    // Retrieve all AppSizes
    router.get("/", appsize.findAll);
    
    // Retrieve a single AppSize with id
    router.get("/:id", appsize.findOne);
  
    // Update a AppSize with id
    router.put("/:id", appsize.update);
  
    // Delete a AppSize with id
    router.delete("/:id", appsize.delete);
    
    app.use('/api/app_size', router);
  };