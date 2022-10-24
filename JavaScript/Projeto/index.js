const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send("Bem Vind!");
})

app.listen(8080, () => {
    console.log('Servidor rodando!');
});