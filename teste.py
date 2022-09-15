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

    Carga_Horaria = open(r"CargaHoraria.txt","w")
    Carga_Horaria.writelines(lista_Completa)
    Carga_Horaria.close()
