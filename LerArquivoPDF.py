import PyPDF2
from time import sleep

arq_PDF = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(arq_PDF.pages)

def mostrarPDF(arq_PDF, number_of_pages):
    for c in range(0, number_of_pages):
        arq_PDF   = open('2022.1.pdf', 'rb')
        readerPDF = PyPDF2.PdfFileReader(arq_PDF)
        pageObj   = readerPDF.getPage(c)
        text      = pageObj.extractText()
        arq_PDF.close()

        file1=open(r"Arquivo_TXT.txt","a")
        file1.writelines(text)
        file1.close()
mostrarPDF(arq_PDF, number_of_pages)




def encontrarProfessor():
    pag = arq_PDF.pages[0]
    texto = pag.extract_text()
    contador = 0
    for c in texto:
        if texto.find():
            contador += 1

def mostrarPDF(reader, number_of_pages):
    for c in range(0, number_of_pages):
        paginas = reader.pages[c]
        text = paginas.extract_text()
        arq_PDF.append(text)
        print(f'\033[1;31m {c} \033[m')

pagina = arq_PDF.pages[0]
texte = pagina.extract_text()
c = 'ACURCIO CASTELO DAVID'
