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

    NomeDisciplica = open(r"NomesDisciplina.txt","w")
    NomeDisciplica.writelines(lista_Temporaria)
    NomeDisciplica.close()

    try:
        with open('NomesDisciplina.txt', 'r') as fr:
            lines = fr.readlines()
            with open('NomesDisciplina.txt', 'w') as fw:
                for line in lines:
                    if line.find('Vagas Ocupadas:') == -1:
                        fw.write(line)
    except:
        print("Oops! existe um erro")

mostrar_Todas_Disciplinas()