dia = input("Digite o dia da semana: ").lower()

#função "lower": transformar texto em minusculo


#Operador | (pipe) para substituir o OR
#OR no Match-Case é o | (pipe)
#Não é possível utilizar OR no Match-Case
match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sabado" | "domingo":
        print("Final de semana")