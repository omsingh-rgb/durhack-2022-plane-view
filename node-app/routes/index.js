var express = require('express');
var router = express.Router();
var path = require('path');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile(path.join(__dirname, 'index.html'));
});

/* GET home page. */
router.get('/image.png', function(req, res, next) {
  res.sendFile(path.join(__dirname, 'image.png'));
});

module.exports = router;
