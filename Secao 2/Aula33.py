texto = 'Python'

# for letra in texto:
#     print(letra)


# for numero in range(10):
#     print(numero)


texto = 'Python'
n_texto = ''

for letra in texto:
    if letra =='t':
        n_texto = n_texto + letra.upper()
    elif letra =='h':
        n_texto += letra.upper()
    else:
        n_texto += letra

print(n_texto)