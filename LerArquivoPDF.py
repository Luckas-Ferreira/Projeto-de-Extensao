import PyPDF2, re
from collections import defaultdict

def mostrar_Todos_Os_Nomes():
    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
        arquivo = txt.readlines()
        txt.close()

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

def print_Arquivo_Terminal():
    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as printTerminal:
        mostrar_Na_Tela = printTerminal.readlines()
        printTerminal.close()
    for tela in mostrar_Na_Tela:
        print(tela.replace('\n', ''))

def converter_PDF_para_TXT():
    arq_PDF = PyPDF2.PdfReader('2022.1.pdf', 'rb')
    number_of_pages = len(arq_PDF.pages)
    arq_TXT = []
    for c in range(0, number_of_pages):
        arq_PDF   = open('2022.1.pdf', 'rb')
        readerPDF = PyPDF2.PdfFileReader(arq_PDF)
        pageObj   = readerPDF.getPage(c)
        text      = pageObj.extractText()
        arq_PDF.close()

        arq_TXT = open(r"Arquivo_TXT.txt","a")
        arq_TXT.writelines(text)
        arq_TXT.close()

    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
        arquivo = txt.readlines()
        txt.close()

def quantidade_Vezes_Professores():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.readlines()

    dicionario = defaultdict(int) 
    for c in arquivo:
        dicionario[c] += 1

    for k, v in dicionario.items():
        print(k.replace('\n', '') , '\033[1;31m aparece:\033[m' , v,)

quantidade_Vezes_Professores()


