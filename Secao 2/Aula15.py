#Introdução à formatação de Strings em Python
nome = "Rosivaldo Rodrigues"
idade = 41
altura = 1.80
e_mario = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imge é {:.2f} '.format(nome, idade, imc))
