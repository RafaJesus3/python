slrFixo = int(input("Digite seu salario aqui: "))
vlrVendas = int(input("Digite o valor de vendas: "))

if slrFixo <= 5000.00:
    comissao = 5000.00 * 0.05 + vlrVendas
    print(f"")
elif slrFixo > 5000.00:
    comissao = 5000.00 * 0.07
