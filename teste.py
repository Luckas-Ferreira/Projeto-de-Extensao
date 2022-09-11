import PyPDF2
 
pdffileobj=open('2022.1.pdf','rb')

pdfreader=PyPDF2.PdfFileReader(pdffileobj)

x=pdfreader.numPages

pageobj=pdfreader.getPage(x+1)

text=pageobj.extract_text()
 
file1=open(r"lorem.txt","a")
file1.writelines(text)