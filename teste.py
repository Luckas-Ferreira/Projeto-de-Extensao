from collections import defaultdict

def quantidade_Vezes_Professores():
    with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
        professor = arquivo1.readlines()
        arquivo1.close()

    with open('NomeDisciplina.txt', 'r', encoding='utf-8') as arquivo2:
        disciplina = arquivo2.readlines()
        arquivo2.close()
