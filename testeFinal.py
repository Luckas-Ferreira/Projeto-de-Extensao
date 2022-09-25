from collections import OrderedDict
with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
    arquivo_TXT = txt.readlines()
    txt.close()

Professores = []
Curso       = []
Disciplina  = []
Horas       = []

for linha in range(len(arquivo_TXT)):
    
    #Encontrar todos os cursos.
    if 'Semestre' in arquivo_TXT[linha]:
        curso = arquivo_TXT[linha].strip().split('-')
        Curso.append(curso[1])

    #Encontrar todos os professores.
    if 'Vagas Oferecidas' in arquivo_TXT[linha]:
        prof = arquivo_TXT[linha - 1].replace('\n', '')
        
        if 'Página' in prof:
            trocar = prof.replace('Página', '-').replace('\n', '')
            separar = trocar.split('-')
            #print(separar[1])
            Professores.append(separar[1])
        else:
            #print(prof)
            Professores.append(prof)

    #Encontrar todas as disciplinas.
    if 'Vagas Ocupadas:' in arquivo_TXT[linha]:
        disciplina = arquivo_TXT[linha].replace('\n', '').split('-')
        #print(disciplina[1].strip())
        Disciplina.append(disciplina[1].strip())

    #Encontrar carga horaria.
    if 'CH:' in arquivo_TXT[linha]:
        horas = arquivo_TXT[linha].replace('CH:', '').split()
        #print(horas[0])
        Horas.append(horas[0])

nome_disciplina = list(zip(Professores, Disciplina))
lorem = list(zip(nome_disciplina, Horas))
print(lorem)