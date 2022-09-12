with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.readlines()


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




