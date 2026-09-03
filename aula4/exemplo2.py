nome = input("Digite o seu nome: ")
print(nome, type(nome))

idade = input("Digite sua idade: ")
print(idade, type(idade))

#Toda informação que é enviada ou recuperada do terminal é str (String, mesmo que texto)
#Funções de conversão
#Numeros inteiros int()
#Numeros decimais float()

idade = input(input("Digite sua idade (0 até 100): "))
print(idade, type(idade))

altura = float(input("Digite sua altura: "))
print(altura, type(altura))

situacao = bool(input("Digite 0 para sair ou 1 para manter ativo: "))
print(situacao, type(situacao))
# no bool é esperado 1 - True ou 0 - False

verdadeiro = True
falso = False
print(type(True), type(False))