import PyPDF2
from time import sleep

reader = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(reader.pages)

def mostrarPDF(reader):
    for c in range(1):
        pdffileobj=open('2022.1.pdf','rb')
        pdfreader=PyPDF2.PdfFileReader(pdffileobj)
        x=pdfreader.numPages
        pageobj=pdfreader.getPage(x - 1)
        text=pageobj.extractText()

        file1=open(r"Arquivo_TXT.txt","a")
        file1.writelines(text)
        file1.close()
mostrarPDF(reader)




def encontrarProfessor():
    pag = reader.pages[0]
    texto = pag.extract_text()
    contador = 0
    for c in texto:
        if texto.find():
            contador += 1

def mostrarPDF(reader, number_of_pages):
    for c in range(0, number_of_pages):
        paginas = reader.pages[c]
        text = paginas.extract_text()
        arq.append(text)
        print(f'\033[1;31m {c} \033[m')

pagina = reader.pages[0]
texte = pagina.extract_text()
c = 'ACURCIO CASTELO DAVID'
