const { json } = require('express');
const express = require('express');
const app = express();
const multer = require('multer');
app.set('view engine', 'ejs');

const storage = multer.diskStorage({
    destination: function(req, file, cb){
        cb(null, "uploads/")
    },
    filename: function(req, file, cb){
        cb(null, file.originalname);
    }
})

const upload = multer({storage})

app.get('/', (req, res) => {
    res.render("index");
})
 
app.post("/upload",upload.single("file"), (req, res) => {
    path = req.file.path;
    console.log(path)
    jsonstr = pdf_to_json(path, res)
    console.log(jsonstr)
})
app.listen(8080, () => {
    console.log('Servidor rodando!');
});

function pdf_to_json(pdf_path, res){
    var pdfUtil = require('pdf-to-text');

    return pdfUtil.pdfToText(pdf_path, function(err, arquivo) {
        
        if (err) throw(err);
            let arquivo2 = arquivo.split('\n')


            Dados = {}
            Dados['Curso'] = {}

            for (var i = 0; i <= (arquivo2.length - 1); i++){
                if (arquivo2[i].indexOf('Semestre') !== -1){
                    var curso = arquivo2[i].trim().split('-')
                    try{
                        temp = Dados['Curso'][curso[1]]['Professor']
                    }catch{
                        Dados['Curso'][curso[1]] = {}
                        Dados['Curso'][curso[1]]['Professor'] = {}
                    }
                }
                //Pegar nome professor
                if (arquivo2[i].indexOf('Vagas Ocupadas:') !== -1){
                    var prof = arquivo2[i -1].split('  ')
                    var professor = prof[prof.length - 1].trim()
                    try{
                        Temp = Dados['Curso'][curso[1]]['Professor'][professor]['Disciplinas']
                    }catch{
                        Dados['Curso'][curso[1]]['Professor'][professor] = {}
                        Dados['Curso'][curso[1]]['Professor'][professor]['Disciplinas'] = {}
                    }
                    
                }
                //Pegar nome disciplina
                if (arquivo2[i].indexOf('Vagas Ocupadas:') !== -1){
                    var disc = arquivo2[i -1].split('  ')[0].trim()
                    var disciplina = disc.split('- ')[1]
                    Dados['Curso'][curso[1]]['Professor'][professor]['Disciplinas'][disciplina] = {}
                }
                //Pegar carga horaria
                if (arquivo2[i].indexOf('CH:') !== -1){
                    var hor = arquivo2[i].replace('CH:', '').replace(' horas', '').split('  ')
                    var horas = parseInt(hor[hor.length -1].trim())
                    Dados['Curso'][curso[1]]['Professor'][professor]['Disciplinas'][disciplina] = horas
                }
            }
            var json1 = JSON.stringify(Dados);
            res.json(Dados)
            return json1   
            
    })
}


