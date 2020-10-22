# def ola_mundo():
#     return 'Olá mundo! Eu sou a função um'
#
# def mestre(funcao):
#     return funcao()
#
#
# executando = mestre(ola_mundo)
#
# print(executando)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{nome} {saudacao}'

executar = mestre(fala_oi, 'Rosivaldo')
print(executar)