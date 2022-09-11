import PyPDF2
from time import sleep

reader = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(reader.pages)

def encontrarProfessor():
    pag = reader.pages[0]
    texto = pag.extract_text()
    contador = 0
    for c in texto:
        if texto.find():
            contador += 1
arq = []
def mostrarPDF(reader, number_of_pages):
    for c in range(0, number_of_pages):
        paginas = reader.pages[c]
        text = paginas.extract_text()
        arq.append(text)
        print(f'\033[1;31m {c} \033[m')

pagina = reader.pages[0]
texte = pagina.extract_text()
c = 'ACURCIO CASTELO DAVID'
print(texte.filter(c))