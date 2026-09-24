v1 = int(input("Digite seu numero: "))
v2 = int(input("Digite seu numero: "))
v3 = int(input("Digite seu numero: "))

if v2 > v1 < v3:
    print(f"O menor número é {v1}")
elif v1 > v2 < v3:
    print(f"O menor número é {v2}")
elif v2 > v3 < v1:
    print(f"O menor número é {v3}")
else:
    print(f"Os números são iguais")