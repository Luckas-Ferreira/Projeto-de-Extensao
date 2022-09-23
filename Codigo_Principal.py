with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
    arquivo_TXT = txt.readlines()
    txt.close()
    

for line in range(0, len(arquivo_TXT)):
    lista_Temporaria = {}
    if 'Presencial' in arquivo_TXT[line]:
        #Adicionar o nome do curso ao dicionário 
        example = {'Administração': []}
        
        if 'Página' in arquivo_TXT[line]:
            troca = arquivo_Temporario[alterar].replace('Página', '\n')
            lista_Temporaria["Curso"] = troca
        else:
            pass
            '''lista_Temporaria["Curso"] = arquivo_TXT[line]'''
    print(lista_Temporaria)
        
    lista_Temporaria2 = []
    if 'Vagas Oferecidas' in arquivo_TXT[line]:
        lista_Temporaria2.append(lista_Temporaria)
        
    
    '''lista_Temporaria3 = [] 
        try:
            if lines.find(':') == -1:
                lista_Temporaria3.append(lines)
        except:
            print("Oops! existe um erro")
            

    lista_diciplina1 = []
    if 'Vagas Ocupadas:' in arquivo_TXT[line]:
        if '-' in arquivo_TXT[line]:
            troca = arquivo_TXT[line].replace('- ', '\n', 1)
            lista_diciplina1.append(troca)

    try:
    
        if lines.find('Vagas Ocupadas:') == -1:
            fw.write(lines)
    except:
        print("Oops! existe um erro")'''