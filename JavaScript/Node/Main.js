const fs = require('fs');
const arquivo = fs.readFileSync('Arquivos/Arquivo_TXT.txt').toString()
let teste = arquivo.split()

for (var i = 0; i <= 5; i++){
    if ('Semestre' == teste[i]){
        console.log('Tem essa porra!')
    }else {
        console.log(teste[i])
        console.log('não tem esse caralho')
    }
}


