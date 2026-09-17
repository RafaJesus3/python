dia = int(input("Digite o dia da semana (1 a 7): "))


#Operador | (pipe) para substituir o OR

match dia:
    case 7 | 1:
        print("Final de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")