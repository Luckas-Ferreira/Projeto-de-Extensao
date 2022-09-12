import PyPDF2, re

def mostrar_Todos_Os_Nomes(arquivo):
    lista_Temporaria = []
    for alterar in range(len(arquivo)):
        if 'Página' in arquivo[alterar]:
            troca = arquivo[alterar].replace('Página', '\n')
            lista_Temporaria.append(troca)
        else:
            lista_Temporaria.append(arquivo[alterar])

    lista_Completa = []
    for nome in range(len(lista_Temporaria)):
        if 'Vagas Oferecidas' in lista_Temporaria[nome]:
            lista_Completa.append(lista_Temporaria[nome -1])
        
    NomesProfessores = open(r"NomesProfessores.txt","w")
    NomesProfessores.writelines(lista_Completa)
    NomesProfessores.close()


    try:
        with open('NomesProfessores.txt', 'r') as fr:
            lines = fr.readlines()
    
            with open('NomesProfessores.txt', 'w') as fw:
                for line in lines:
                    if line.find(':') == -1:
                        fw.write(line)
    except:
        print("Oops! existe um erro")

def print_Arquivo_Terminal(arq_PDF, number_of_pages):
    for c in range(0, number_of_pages):
        pag  = arq_PDF.pages[c]
        text = pag.extract_text()
        print(text)

arq_PDF = PyPDF2.PdfReader('2022.1.pdf', 'rb')
number_of_pages = len(arq_PDF.pages)

for c in range(0, number_of_pages):
    arq_PDF   = open('2022.1.pdf', 'rb')
    readerPDF = PyPDF2.PdfFileReader(arq_PDF)
    pageObj   = readerPDF.getPage(c)
    text      = pageObj.extractText()
    arq_PDF.close()

    arq_TXT = open(r"Arquivo_TXT.txt","a")
    arq_TXT.writelines(text)
    arq_TXT.close()


with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.readlines()






mostrar_Todos_Os_Nomes(arquivo)


