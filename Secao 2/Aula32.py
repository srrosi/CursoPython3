frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

print(frase)
print(tamanho_frase)


contador = 0
n_string = ''

nova_letra = input('Qual letra deseja colocar em maíscula: ')

while contador < tamanho_frase:
    letra = frase[contador]

    if letra == nova_letra:
        n_string += nova_letra.upper()
    else:
        n_string += letra
    contador += 1

print(n_string)