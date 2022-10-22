const fs = require('fs');
var pdfUtil = require('pdf-to-text');
var pdf_path = "Arquivos/2022.1.pdf";


pdfUtil.pdfToText(pdf_path, function(err, data) {
  if (err) throw(err);
    
});
console.log(arquivo)