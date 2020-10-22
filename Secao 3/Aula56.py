# Diciários

# d1 = {'chave1':'valor da chave', 'chave2':'valor da chave 2'}
# d1['chave3'] = 'Valor da chave 3'
#
#
# d2 = dict(chave='Chave um',chave1='Chave dois',chave2='Chave tres')
#
# print(d1['chave3'])
#
# print(d2)

d3 = {
    'chave1': 'valor da chave',
    'chave2': 'Outro valor de chave',
    'chave3': 'Valores em tupla'
}

d3['chave4'] = "Chave existe"

# print('str' in d3)
# print(d3)
#
# if d3.get('nomes') is None:
#     print('Nonesssss')
# else:
#     print(d3.get('nomes'))
#

# print('Valores em tupla' in d3.keys())
#
# print(len(d3))
#
# for k in d3:
#     print(k)
#
# for v in d3.values():
#     print(v)
#
# for i in d3.items():
#     print(i)

#
# for m in d3.items():
#     print(m[0], m[1])


# clientes = {
#     'cliente1':{
#         'nome':'Luiz',
#         'sobrenome': 'Maria'
#     },
#     'cliente2':{
#         'nome':'Carla',
#         'sobrenome':'Silva'
#     }
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')


d1 = {1: 'a', 2: 'b', 3:'c'}
v = d1

v[1] = 'Teste'

print(d1)
print(v)