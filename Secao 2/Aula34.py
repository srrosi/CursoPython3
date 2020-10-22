secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh.. apenas uma letra, por favor ')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Muito bem, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Aff, a letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Show, você acertou {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta é {secreto_temporario}')