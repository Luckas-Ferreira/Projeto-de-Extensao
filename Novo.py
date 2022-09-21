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

