def mostrar_Todas_Disciplinas():
    with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
        arquivo = txt.readlines()
        txt.close()

    lista_Temporaria = []
    for alterar in range(len(arquivo)):
        if '-' in arquivo[alterar]:
            troca = arquivo[alterar].replace('- ', '\n')
            lista_Temporaria.append(troca)
        else:
            lista_Temporaria.append(arquivo[alterar])

    NomeDisciplica = open(r"NomeDisciplina.txt","w")
    NomeDisciplica.writelines(lista_Temporaria)
    NomeDisciplica.close()

    with open('NomeDisciplina.txt', 'r', encoding='utf-8') as txt:
        lista_Temporaria = txt.readlines()
        txt.close()

    lista_Completa = []
    for nome in range(len(lista_Temporaria)):
        if 'CH' in lista_Temporaria[nome]:
            lista_Completa.append(lista_Temporaria[nome -1])
        
    NomeDisciplica = open(r"NomeDisciplina.txt","w")
    NomeDisciplica.writelines(lista_Completa)
    NomeDisciplica.close()
    print(lista_Completa)
    
    try:
        with open('NomeDisciplina.txt', 'r') as fr:
            lines = fr.readlines()
    
            with open('NomeDisciplina.txt', 'w') as fw:
                for line in lines:
                    if line.find(':') == -1:
                        fw.write(line)
    except:
        print("Oops! existe um erro")

mostrar_Todas_Disciplinas()
