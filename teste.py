from collections import defaultdict

def quantidade_Vezes_Professores():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('NomeDisciplina.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()

    
    def Disciplina():
        discionario = {'luckas': 'pote', 'lorem': 'gato'}
        for c in range(0, 4):
            print(discionario.keys(c))
        

    '''dicionario = defaultdict(str) 
    for c in professor:
        dicionario[c] += Disciplina()

    for k, v in dicionario.items():
        print(k.replace('\n', '') , '\033[1;31m aparece:\033[m' , v,)'''

quantidade_Vezes_Professores()