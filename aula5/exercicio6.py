num1= int(input("Digite o seu primeiro numero inteiro (A): "))
num2= int(input("Digite o seu segundo numero inteiro (B): "))

print(f"Variavel A = {num1}")
print(f"Variavel B = {num2}")


auxiliar = num1
num1 = num2
num2 = auxiliar

print(f"Variavel A = {num1}")
print(f"Variavel B = {num2}")