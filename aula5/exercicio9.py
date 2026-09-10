horas = float(input("Digite as horas: "))


minutos = horas * 60
segundos = horas * 3600


#Resultado

print(f"{horas} hora(s) equivalem a:")
print(f"- {minutos:.2f} minutos")
print(f"- {segundos:.2f} segundos")