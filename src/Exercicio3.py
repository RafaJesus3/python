compra = float(input("Digite o valor da compra: R$ "))

if compra > 100:
    desconto = compra * 0.10
    print("Você ganhou 10% de desconto!")
elif compra <= 100:
    desconto = compra * 0.05
    print("Você ganhou 5% de desconto!")
