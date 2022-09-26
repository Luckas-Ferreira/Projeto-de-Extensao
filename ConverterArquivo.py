import os, PyPDF2

class Arquivo:
    def __init__(self, arquivo):
        if os.path.exists('Arquivo_TXT.txt'):
            pass
        else:
            print('\033[1;33m AGUARDE! \033[m')
            self.arquivo = arquivo
            arq_PDF = PyPDF2.PdfReader(self.arquivo, 'rb')
            paginas = len(arq_PDF.pages)
            texto   = []
            for c in range(0, paginas):
                arq_PDF   = open('2022.1.pdf', 'rb')
                readerPDF = PyPDF2.PdfFileReader(arq_PDF)
                pageObj   = readerPDF.getPage(c)
                texto.append(pageObj.extractText())
                arq_PDF.close()
                
            arq_TXT = open(r"Arquivo_TXT.txt","w")
            arq_TXT.writelines(texto)
            arq_TXT.close()

Converter = Arquivo('2022.1.pdf')