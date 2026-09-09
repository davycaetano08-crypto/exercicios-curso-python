cll50 = cll20 = cll10 = cll1 = 0

while True:
    saque = int(input('Valor do saque: '))

    cll50 = saque // 50
    cll20 = (saque % 50) // 20
    cll10 = ((saque % 50) % 20) // 10

    print(cll50, cll20, cll10)
    
    