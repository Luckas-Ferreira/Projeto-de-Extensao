from collections import defaultdict
import re
def Nome_e_Disciplinas():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('NomesDisciplina.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()

    juntar_Listas = list(zip(professor, disciplina))  

    Lista_Final = defaultdict(list)
    for k, v in juntar_Listas:
        Lista_Final[k.strip()].append(v)
    sorted(Lista_Final.items())
    
    for k, v in Lista_Final.items():
        for disciplina in v:
            print(disciplina)
        
        
Nome_e_Disciplinas()
