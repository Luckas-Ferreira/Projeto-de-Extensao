from collections import defaultdict
with open('DadosSeparados/NomesProfessores.txt', 'r', encoding='utf-8') as arquivo1:
    professor = arquivo1.readlines()
    arquivo1.close()

with open('DadosSeparados/NomesDisciplina.txt',  'r', encoding='utf-8') as arquivo2:
    disciplina = arquivo2.readlines()
    arquivo2.close()

with open('DadosSeparados/CargaHoraria.txt',     'r', encoding='utf-8') as arquivo3:
    horas = arquivo3.readlines()
    arquivo3.close()

with open('DadosSeparados/NomesCurso.txt',       'r', encoding='utf-8') as arquivo4:
    Curso = arquivo4.readlines()
    arquivo4.close()

nome_disciplina = list(zip(professor, disciplina))
nome_horas      = list(zip(professor, horas))

juntar = list(zip(nome_disciplina, horas))

Lista_Final = defaultdict(list)
for k, v in nome_disciplina:
    Lista_Final[k].append(v)
sorted(Lista_Final.items())

Lista_horas = defaultdict(list)
for k, v in nome_horas:
    Lista_horas[k].append(v)
sorted(Lista_horas.items())

c = defaultdict(list)
for k, v in Lista_Final.items():
    c[k] = Lista_horas.keys()
    print(c)