with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
    arquivo_TXT = txt.readlines()
    txt.close()

lista_Temporaria = []
dicio = {}
for linha in range(len(arquivo_TXT)):
    if 'Semestre' in arquivo_TXT[linha]:
        split = arquivo_TXT[linha].split('-')
        lista_Temporaria.append(split[1])
        print(split[1])

    if 'Vagas Oferecidas' in arquivo_TXT[linha]:
        prof = arquivo_TXT[linha - 1]
        if 'Página' in prof:
            trocar = prof.replace('Página', '-')
            separar = trocar.split('-')
            separar[1]
        else:
            print(prof)

    '''if 'Vagas Ocupadas:' in arquivo_TXT[linha]:'''




























'''NomesCurso = open(r"DadosSeparados/NomesCurso.txt","w")
NomesCurso.writelines(lista_Temporaria)
NomesCurso.close()
with open ('DadosSeparados/NomesCurso.txt', 'r') as arquivo:
    NomeCurso1 = arquivo.readlines()
    arquivo.close()

lista_Completa = []
for linha in range(len(NomeCurso1)):
    if 'Semestre' in NomeCurso1[linha -1]:
        lista_Completa.append(NomeCurso1[linha])
NomesCurso = open(r"DadosSeparados/NomesCurso.txt","w")
NomesCurso.writelines(lista_Completa)
NomesCurso.close()'''