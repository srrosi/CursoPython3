perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2? ',
        'respostas':{
            'a':'1',
            'b':'4',
            'c':'3',
        },
        'resposta_certa':'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '6',
            'b': '4',
            'c': '3',
        },
        'resposta_certa': 'a',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')


    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Show, acertou')
        respostas_certas += 1
    else:
        print('Vixxe... não é isso não')

    print()