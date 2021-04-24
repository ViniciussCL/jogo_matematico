print('Responda as alternativas abaixo utilizando apenas suas letras correspondentes: ')

perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 5 * 10 ?: ',
        'alternativas': {'a': 25, 'b': 50, 'c': 55, 'd': 40},
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 10 + 10 ?: ',
        'alternativas': {'a': 20, 'b': 30, 'c': 15, 'd': 25},
        'resposta_certa': 'a',
    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 2 * 9 ?: ',
        'alternativas': {'a': 34, 'b': 28, 'c': 12, 'd': 18},
        'resposta_certa': 'd',
    },
}
respostas_corretas = 0
for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das alternativas: ')
    for rk, rv in pv["alternativas"].items():
        print(f'{rk}: {rv}')

    resposta_user = input('Insira sua resposta: ')
    if resposta_user == pv['resposta_certa']:
        print('Parabéns, resposta correta!! ')
        respostas_corretas += 1
    else:
        print('Resposta incorreta' )

qtd_perguntas = len(perguntas)
porcentagem = respostas_corretas / qtd_perguntas * 100
porcentagem = int(porcentagem)

print()
print(f'Você acertou {respostas_corretas} de 3 alternativas')
print(f'Sua porcentagem de acerto foi de: {porcentagem} %')
if respostas_corretas == 3:
    print('Você foi muito bem!')
elif respostas_corretas == 2:
    print('Você pode melhorar')
elif respostas_corretas == 1:
    print('Você precisa estudar mais...')
else:
    print('Você foi muito mal')

