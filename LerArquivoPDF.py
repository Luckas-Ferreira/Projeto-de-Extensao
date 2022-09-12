import PyPDF2, re

arq_PDF = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(arq_PDF.pages)

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

convert_PDF_to_TXT(arq_PDF, number_of_pages)

with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.readlines()

def Mostrar_No_Terminal(arq_PDF, number_of_pages):
    for c in range(0, number_of_pages):
        pag  = arq_PDF.pages[c]
        text = pag.extract_text()
        print(text)

def escrever_Nomes_Professores ():
    lista_Temporaria = []
    lista_Completa   = []
    for linhas in range(len(arquivo)):
        if 'Vagas Oferecidas' in arquivo[linhas]:
            lista_Temporaria.append(arquivo[linhas - 1])

    for pagina in range(len(lista_Temporaria)):
        lista_Temporaria[pagina] = lista_Temporaria[pagina].rstrip('\n')
        if 'Página' in lista_Temporaria[pagina]:
            lista_Completa.append(lista_Temporaria[pagina - 1])

    ordem = sorted(lista_Completa)
    print(ordem)
    '''NomesProfessores = open(r"NomesProfessores.txt","w")
    NomesProfessores.writelines(lista_Completa)
    NomesProfessores.close()'''


convert_PDF_to_TXT(arq_PDF, number_of_pages)

