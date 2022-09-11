import PyPDF2

arq_PDF = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(arq_PDF.pages)

def show_on_screen(arq_PDF, number_of_pages):
    for c in range(0, number_of_pages):
        pag  = arq_PDF.pages[c]
        text = pag.extract_text()
        print(text)

def convert_PDF_to_TXT (arq_PDF, number_of_pages):
    for c in range(0, number_of_pages):
        arq_PDF   = open('2022.1.pdf', 'rb')
        readerPDF = PyPDF2.PdfFileReader(arq_PDF)
        pageObj   = readerPDF.getPage(c)
        text      = pageObj.extractText()
        arq_PDF.close()

        arq_TXT = open(r"Arquivo_TXT.txt","a")
        arq_TXT.writelines(text)
        arq_TXT.close()

#convert_PDF_to_TXT(arq_PDF, number_of_pages)
contador = 0
with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.readlines()

for line in arquivo:
    if 'ACURCIO CASTELO DAVID' in line:
        contador += 1

file = open("Arquivo_TXT.txt") 

for pos, l_num in enumerate(file): 
    specified_lines = [11] 
    if pos in specified_lines: 
        print(l_num)
        specified_lines.append(6)


#show_on_screen(arq_PDF, number_of_pages)

