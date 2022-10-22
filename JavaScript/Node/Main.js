const fs = require('fs');
const { stringify } = require('querystring');
const arquivo = fs.readFileSync('Arquivos/Arquivo_TXT.txt').toString()
let arquivo2 = arquivo.split('\n')

Dados = {}
Dados['Curso'] = {}

for (var i = 0; i <= (arquivo2.length - 1); i++){
    //Pegar Curso
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
console.log(Dados)