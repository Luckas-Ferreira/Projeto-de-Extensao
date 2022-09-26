from collections import defaultdict
import json

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

Lista_Final = defaultdict(list)
for k, v in nome_disciplina:
    Lista_Final[k].append(v)
sorted(Lista_Final.items())

Lista_horas = defaultdict(list)
for k, v in nome_horas:
    Lista_horas[k].append(v)
sorted(Lista_horas.items())

lfv = {}
print(Lista_horas)
'''for k, v in enumerate(Lista_Final):
    
    d = Lista_Final[v]
    h = Lista_horas[v]
    lfv[v] = {}
    lfv[v]["disciplinas"] = d
    lfv[v]['horas'] = h

txtJson = json.dumps(lfv)

arquivoJson = open(r"DadosSeparados/ArquivoJson.json","w")
arquivoJson.writelines(txtJson)
arquivoJson.close()


with open ('Arquivo_TXT.txt', 'r') as arquivo:
    NomeCurso = arquivo.readlines()
    arquivo.close()
lista_Temporaria = []
for linha in range(len(NomeCurso)):
    if 'Semestre' in NomeCurso[linha]:
        lista_Temporaria.append(NomeCurso[linha].replace('- ', '\n', 2))

NomesCurso = open(r"DadosSeparados/NomesCurso.txt","w")
NomesCurso.writelines(lista_Temporaria)
NomesCurso.close()
with open ('DadosSeparados/NomesCurso.txt', 'r') as arquivo:
    NomeCurso1 = arquivo.readlines()
    arquivo.close()

lista_Completa = []
for linha in range(len(NomeCurso1)):
    if 'Semestre' in NomeCurso1[linha -1]:
        lista_Completa.append(NomeCurso1[linha])



teste = {}
transf = lista_Completa

for linha in range(len(NomeCurso)):
    if 'Semestre' in NomeCurso[linha]:
        for linha2 in transf:
            if linha2.strip() in NomeCurso[linha]:
                teste[linha2]
            

'''

'''d = Lista_Final[v]
h = Lista_horas[v]
lfv[v] = {}
lfv[v]["disciplinas"] = d
lfv[v]['horas'] = h'''