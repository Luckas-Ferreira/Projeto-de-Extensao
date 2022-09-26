import json
with open('Arquivo_TXT.txt', 'r', encoding='utf-8') as txt:
    arquivo_TXT = txt.readlines()
    txt.close()

Dados = {}
Dados['Curso'] = {}
def CCurso(Dados, arquivo_TXT, linha):
    if 'Semestre' in arquivo_TXT[linha]:
        curso = arquivo_TXT[linha].strip().split('-')
        try:
            Temp = Dados['Curso'][curso[1]]['Professores']
        except:
            Dados['Curso'][curso[1]] = {}
            Dados['Curso'][curso[1]]['Professores'] = {}
        return Dados, curso
    return False

for linha in range(len(arquivo_TXT)):
    #Encontrar todos os cursos.
    DadosCurso = CCurso(Dados, arquivo_TXT, linha)
    if DadosCurso != False:
        Dados = DadosCurso[0]
        curso = DadosCurso[1]

    #Encontrar todos os professores.
    if 'Vagas Oferecidas' in arquivo_TXT[linha]:
        prof = arquivo_TXT[linha - 1].replace('\n', '')
        professor = None
        if 'Página' in prof:
            trocar = prof.replace('Página', '-').replace('\n', '')
            separar = trocar.split('-')
            professor = separar[1]
            
        else:
            professor = prof
        if professor != None:
            try:
                Temp = Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas']
            except:
                Dados['Curso'][curso[1]]['Professores'][professor] = {}
                Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas'] = {}

    #Encontrar todas as disciplinas.
    if 'Vagas Ocupadas:' in arquivo_TXT[linha]:
        disciplina = arquivo_TXT[linha].replace('\n', '').split('-')
        DiciName = disciplina[1].strip()
        Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas'][DiciName] = {}
        
    #Encontrar carga horaria.
    if 'CH:' in arquivo_TXT[linha]:
        horas = arquivo_TXT[linha].replace('CH:', '').split()
        Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas'][DiciName] = horas[0]


print(json.dumps(Dados))