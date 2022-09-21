def mostra_Todos_Cursos():
    with open ('Arquivo_TXT.txt', 'r') as arquivo:
        NomeCurso = arquivo.readlines()
        arquivo.close()

    lista_Temporaria = []
    for linha in range(len(NomeCurso)):
        if 'Semestre' in NomeCurso[linha]:
            lista_Temporaria.append(NomeCurso[linha].replace('- ', '\n', 2))

    NomesCurso = open(r"DadosSeparados/NomesCurso.txt","w")
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
    NomesCurso.close()