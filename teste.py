import PyPDF2, re
from collections import defaultdict

class converter:
    def __init__(self, arquivo):
        self.arquivo = arquivo

        arq_PDF = PyPDF2.PdfReader(self.arquivo, 'rb')
        paginas = len(arq_PDF.pages)
        arq_TXT = []
        for c in range(0, number_of_pages):
            arq_PDF   = open('2022.1.pdf', 'rb')
            readerPDF = PyPDF2.PdfFileReader(arq_PDF)
            pageObj   = readerPDF.getPage(c)
            texto     = pageObj.extractText()
            arq_PDF.close()

            arq_TXT = open(r"Arquivo_TXT.txt","a")
            arq_TXT.writelines(text)
            arq_TXT.close()

teste = converter('2022.1.pdf')
