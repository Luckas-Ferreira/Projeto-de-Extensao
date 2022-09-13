from collections import defaultdict

def quantidade_Vezes_Professores():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('NomeDisciplina.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()

    nome = ['ACURCIO CASTELO DAVID']
    disciplina = ['A TEORIAS ORGANIZACIONAIS I']

    s = [('rome', 1), ('paris', 2), ('paris', 'gato'), ('newyork', 3), ('paris', 4), ('delhi', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    sorted(d.items())
   
    print(d)
    
    key_list = ['name', 'age', 'address']
    value_list = ['Johnny', '27', 'New York']

    dict_from_list = {}
    for key in key_list:
        for value in value_list:
            dict_from_list[key] = value
            break

    #print(dict_from_list)
quantidade_Vezes_Professores()