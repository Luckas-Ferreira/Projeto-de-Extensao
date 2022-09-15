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

mostrar_Todos_Professores()