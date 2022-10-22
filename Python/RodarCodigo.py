import json, ConverterArquivo
Converter = ConverterArquivo.Arquivo('2022.1.pdf')

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

def PProfesor(Dados, arquivo_TXT, linha):
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
            return curso, professor
        return False
    return False

def DDiciplina(Dados, arquivo_TXT, linha):
    if 'Vagas Ocupadas:' in arquivo_TXT[linha]:
        disciplina = arquivo_TXT[linha].replace('\n', '').split('-')
        DiciName = disciplina[1].strip()
        Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas'][DiciName] = {}
        return DiciName, professor
    return False

def HHora(Dados, arquivo_TXT, linha):
    if 'CH:' in arquivo_TXT[linha]:
        horas = arquivo_TXT[linha].replace('CH:', '').split()
        Dados['Curso'][curso[1]]['Professores'][professor]['Disciplinas'][DiciName] = horas[0]
        return horas
    return False

for linha in range(len(arquivo_TXT)):
    #Encontrar todos os cursos.
    DadosCurso = CCurso(Dados, arquivo_TXT, linha)
    if DadosCurso != False:
        Dados = DadosCurso[0]
        curso = DadosCurso[1]

    #Encontrar todos os professores.
    DadosProfessor = PProfesor(Dados, arquivo_TXT, linha)
    if DadosProfessor != False:
        curso = DadosProfessor[0]
        professor = DadosProfessor[1]

    #Encontrar todas as disciplinas.
    DadosDiciplina = DDiciplina(Dados, arquivo_TXT, linha)
    if DadosDiciplina != False:
        DiciName = DadosDiciplina[0]
        professor = DadosDiciplina[1]

    #Encontrar carga horaria.
    DadosHorario = HHora(Dados, arquivo_TXT, linha)
    if DadosHorario != False:
        hora = DadosHorario[0]

#Salvar arquivo.json
DadosJson = json.dumps(Dados)
arquivoJson = open(r"ArquivoJson.json","w")
arquivoJson.writelines(DadosJson)
arquivoJson.close()
