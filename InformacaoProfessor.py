with open('NomesProfessores.txt', 'r', encoding='utf-8') as arquivo2:
    nomes = arquivo2.readlines()
    arquivo2.close()

a = []
contador = 0
nomes_Sem_Duplicatas = []

for nome in nomes:
    if nome not in nomes_Sem_Duplicatas:
        nomes_Sem_Duplicatas.append(nome)
print(nomes_Sem_Duplicatas)
'''for todosNomes in range(0, len(nomes)):
    for SemDuplicatas in range(0, len(nomes_Sem_Duplicatas)):
        if nomes[todosNomes].count(SemDuplicatas):
            a.append(nomes[todosNomes])

for SemDuplicatas in  range(len(nomes_Sem_Duplicatas)):
    nomes_Sem_Duplicatas[SemDuplicatas].count(str('ADRIANO CESAR ROSA DA COSTA'))'''
 
'''
tes = {}
for pos, nome in enumerate(nomes_Sem_Duplicatas):
    print(pos, nome)
    if nome.count(nomes_Sem_Duplicatas):
        contador += 1

print(contador)'''