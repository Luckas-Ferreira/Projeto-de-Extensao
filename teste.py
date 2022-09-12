lista = ['Vagas Oferecidas: 50 Vagas Ocupadas: 17ZOTA087 - A MICROBIOLOGIA E IMUNOLOGIA\n',' Terça-feira 11:10 - 12:00\n', ' Quinta-feira 07:30 - 08:20\n', ' Quinta-feira 08:20 - 09:10\n', 'OSCAR BOAVENTURA NETO\n', 'Vagas Oferecidas: 50 Vagas Ocupadas: 27ZOTA089 - A ZOOLOGIA GERAL\n', 'CH:56 horas\n', ' Segunda-feira 09:20 - 10:10\n', ' Segunda-feira 10:10 - 11:00\n', ' Segunda-feira 11:10 - 12:00\n', 'OSCAR BOAVENTURA NETO\n', 'Vagas Oferecidas: 50 Vagas Ocupadas: 9ZOTA106 - A PARASITOLOGIA ZOOTÉCNICA\n', 'CH:54 horas\n', ' Quarta-feira 07:30 - 08:20\n', ' Quarta-feira 08:20 - 09:10\n', ' Quarta-feira 09:20 - 10:10\n', 'PATRICK HENRIQUE DA SILVA BRITO\n', 'Vagas Oferecidas: 60 Vagas Ocupadas: 43ZOTA073 - A INTRODUÇÃO À INFORMÁTICA\n', 'CH:54 horas\n', ' Terça-feira 10:10 - 11:00\n', ' Terça-feira 11:10 - 12:00\n', ' Terça-feira 12:00 - 12:50\n', '4 12/08/2022 08:48:39 PáginaTHIAGO ROCHA ARAUJO\n', ]

lista_Temporaria = []
for alterar in range(len(lista)):
    if 'Página' in lista[alterar]:
        troca = lista[alterar].replace('Página', '\n')
        lista_Temporaria.append(troca)
    else:
        lista_Temporaria.append(lista[alterar])


print(lista_Temporaria)