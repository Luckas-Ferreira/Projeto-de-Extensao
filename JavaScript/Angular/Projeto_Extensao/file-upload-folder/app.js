const express = require('express')
const app = express()
const port = 3000
const bodyParser = require("body-parser");
const multipart = require('connect-multiparty');
const multipartMiddleware = multipart({ uploadDir: './uploads' });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use("/api/upload", function(request, response, next){
    next();
});
  
app.get('/api/upload', (req, res)=>{
    res.json({'message':'hello'});
});

app.post('/api/upload', multipartMiddleware, (req, res)=>{
    res.json({'message':req.files});
});

app.use(function(err, req, res, next) {
    res.json({'error':err.message})
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))