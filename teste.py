import PyPDF2, re, os
from collections import defaultdict

class converter:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        arq_PDF = PyPDF2.PdfReader(self.arquivo, 'rb')
        paginas = len(arq_PDF.pages)
        arq_TXT = []
        for c in range(0, paginas):
            arq_PDF   = open('2022.1.pdf', 'rb')
            readerPDF = PyPDF2.PdfFileReader(arq_PDF)
            pageObj   = readerPDF.getPage(c)
            texto     = pageObj.extractText()
            arq_PDF.close()

            try:
                os.remove('Arquivo_TXT.txt')
            except:
                pass
            
            arq_TXT = open(r"Arquivo_TXT.txt","a")
            arq_TXT.writelines(texto)
            arq_TXT.close()
            

    def print_Arquivo_Terminal(self):
        with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as printTerminal:
            mostrar_Na_Tela = printTerminal.readlines()
            printTerminal.close()
        for tela in mostrar_Na_Tela:
            print(tela.replace('\n', ''))
teste = converter('2022.1.pdf')
#teste.print_Arquivo_Terminal()
