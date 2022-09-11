import PyPDF2

arquivo = open('2022.1.pdf', 'rb')
lerPDF  = PyPDF2.PdfFileReader(arquivo)
pageObj = lerPDF.getPage(1)
texto   = pageObj.extractText()
arquivo.close()

file1=open(r"Arquivo_TXT.txt","a")
file1.writelines(texto)
file1.close()