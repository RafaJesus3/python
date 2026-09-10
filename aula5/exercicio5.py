base = 1800
com_fixa = 150
total_vendas = 3

nome = input("Digite seu nome aqui: ")
pr_vendidos = int(input("Digite a quantidade de produtos vendidos: "))
valor_total = float(input("Digite o valor total de vendas: "))

comissao = pr_vendidos*com_fixa
vendas = valor_total * (total_vendas/100)
total = comissao + vendas + base

#Resultado

print(f"Óla {nome}, você teve uma comissão de:{comissao}, totalizando {total}")


