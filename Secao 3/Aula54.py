lista = [
    ['P1',1],
    ['P2',2],
    ['P3',3],
    ['P4',25],
    ['P5',5],
    ['P6',15],
    ['P7',10],
    ['P8',8],
]



# lista.sort(key=lambda item: item[1], reverse=False)
print(sorted(lista, key=lambda i: i[1], reverse=True))