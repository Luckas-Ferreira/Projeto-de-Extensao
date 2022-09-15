import PyPDF2, re
from collections import defaultdict

def mostrar_Todos_Professores():
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
        
    NomesProfessores = open(r"Dados Separados/NomesProfessores.txt","w")
    NomesProfessores.writelines(lista_Completa)
    NomesProfessores.close()


    try:
        with open('Dados Separados/NomesProfessores.txt', 'r') as fr:
            lines = fr.readlines()
    
            with open('Dados Separados/NomesProfessores.txt', 'w') as fw:
                for line in lines:
                    if line.find(':') == -1:
                        fw.write(line)
    except:
        print("Oops! existe um erro")

def mostra_Carga_Horaria():
    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
        arquivoCompleto = txt.readlines()
        txt.close()

    lista_Temporaria = []
    lista_Completa = []
    for horas in arquivoCompleto:
        if 'CH:' in horas:
            lista_Temporaria.append(horas.replace('CH:', ''))

    for remover in lista_Temporaria:  
        if 'horas' in remover:
            lista_Completa.append(remover.replace('horas', ''))

    Carga_Horaria = open(r"Dados Separados/CargaHoraria.txt","w")
    Carga_Horaria.writelines(lista_Completa)
    Carga_Horaria.close()
    
def mostrar_Todas_Disciplinas():
    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
        arquivoCompleto = txt.readlines()
        txt.close()

    lista_Temporaria = []

    for disciplinas in range(0, len(arquivoCompleto)):
        if 'Vagas Ocupadas:' in arquivoCompleto[disciplinas]:
            if '-' in arquivoCompleto[disciplinas]:
                troca = arquivoCompleto[disciplinas].replace('- ', '\n', 1)
                lista_Temporaria.append(troca)

    NomeDisciplica = open(r"Dados Separados/NomesDisciplina.txt","w")
    NomeDisciplica.writelines(lista_Temporaria)
    NomeDisciplica.close()

    try:
        with open('Dados Separados/NomesDisciplina.txt', 'r') as fr:
            lines = fr.readlines()
            with open('Dados Separados/NomesDisciplina.txt', 'w') as fw:
                for line in lines:
                    if line.find('Vagas Ocupadas:') == -1:
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
    mostrar_Todos_Professores()
    with open('Dados Separados/NomesProfessores.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.readlines()

    dicionario = defaultdict(int) 
    for c in arquivo:
        dicionario[c] += 1

    for k, v in dicionario.items():
        print(k.replace('\n', '') , '\033[1;31m aparece:\033[m' , v,)

def Nome_e_Disciplinas():
    mostrar_Todos_Professores()
    mostrar_Todas_Disciplinas()
    with open('Dados Separados/NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('Dados Separados/NomesDisciplina.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()

    juntar_Listas = list(zip(professor, disciplina))  

    Lista_Final = defaultdict(list)
    for k, v in juntar_Listas:
        Lista_Final[k.strip()].append(v)
    sorted(Lista_Final.items())
    
    for k, v in Lista_Final.items():
        print(f'\n\033[1;31m{k}:\033[m ', end='')
        for disciplina in v:
            print(disciplina.strip('\n'), end=', ')


def Nome_e_Carga_Horaria():
    mostrar_Todos_Professores()
    mostra_Carga_Horaria()
    with open('Dados Separados/NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('Dados Separados/CargaHoraria.txt', 'r', encoding='utf-8') as arquivo2:
        horas = arquivo2.readlines()
        arquivo2.close()


    juntar_Listas = list(zip(professor, horas))
    lista_Temporaria = defaultdict(list)
    Lista_Final = []
    for k, v in juntar_Listas:
        lista_Temporaria[k.strip()].append(v)
    sorted(lista_Temporaria.items())
    
    def soma(numero):
        contado = 0
        for i in numero:
            contado += i
        return contado
    
    for k, v in lista_Temporaria.items():
        print(f'\n\033[1;31m{k}:\033[m', end=' ')
        numero = []
        for horas in v:
            numero.append(int(horas))
        print(f'Carga Horaria Total - {sum(numero)} Horas')

converter_PDF_para_TXT()