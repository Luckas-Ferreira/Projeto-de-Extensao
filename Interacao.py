import Codigo_Principal

Opcao = Codigo_Principal.Arquivo('2022.1.pdf') #Adicionar o Arquivo."PDF"


print('=-' * 30, end='')
print('''
[ 1 ]--------- Mostrar informações na tela -----------[ 1 ]
[ 2 ]--------- Ver todo os nomes duplicados ----------[ 2 ]
[ 3 ]-------- Ver quantas vezes aparece o nome -------[ 3 ]
[ 4 ]----------- Mostrar nome e disciplina -----------[ 4 ]
[ 5 ]--------- Mostrar nome e carga horaria ----------[ 5 ]
''', end='')
print('=-' * 30)

opção = int(input('Opção: '))
if opção == 1:
    Opcao.print_Arquivo_Terminal()
elif opção == 2:
    Opcao.mostrar_Todos_Professores()
elif opção == 3:
    Opcao.quantidade_Vezes_Professores()
elif opção == 4:
    Opcao.Nome_e_Disciplinas()
elif opção == 5:
    Opcao.Nome_e_Disciplinas()