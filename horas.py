def Nome_e_Disciplinas():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('cargaHoraria.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()

    juntar_Listas = list(zip(professor, disciplina))  

    Lista_Final = defaultdict(list)
    for k, v in juntar_Listas:
        Lista_Final[k.strip()].append(v)
    sorted(Lista_Final.items())
    
    for k, v in Lista_Final.items():
        print(f'\n\033[1;31m{k}:\033[m ', end='')
        for disciplina in v:
            print(disciplina.strip('\n'), end=', ')