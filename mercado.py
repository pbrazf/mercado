# lendo nome e preço dos produtos
print('-' * 25)
print('---- MERCADO DO BRAZ ----')
print('-' * 25)

total = maismil = cont = precomenor = 0
barato = ''

while True:
    nome = str(input('nome do produto: ')).title().strip()
    preco = float(input('valor: R$'))
    print('-' * 25)
    total += preco
    cont += 1
    if preco > 1000:
        maismil += 1
    if cont == 1:
        barato = nome
        precomenor = preco
    elif preco < precomenor:
        barato = nome
        precomenor = preco
    while True:
        continuar = str(input('deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'N' or continuar == 'S':
            break
    print('-' * 25)
    if continuar == 'N':
        break
print(f'''total da compra: R${total:.2f}
produtos custando mais de R$1000: {maismil}
o produto mais barato foi {barato} que custou R${precomenor:.2f}''')
