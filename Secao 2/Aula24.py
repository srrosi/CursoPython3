num1 = input('Digite um número ')
num2 = input('Digite outro número ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
else:
    print('Não dá para converter os números')