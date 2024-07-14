#Questão 5 - Dê um exemplo de uso da estrutura condicional aninhada (if, elif e else). 

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
soma = num1 + num2

if soma % 2 == 0 and soma > 10:
    print(f"O resultado da soma é {soma}. {soma} é um número PAR e maior do que 10 ")
elif soma % 2 == 1 and soma > 10:
    print(f"O resultado da soma é {soma}. {soma} é um número ÍMPAR e maior do que 10")
elif soma <= 10 and soma > 0:
    print(f"O resultado da soma é {soma}. {soma} é um número positivo, menor ou igual a 10")
elif soma == 0:
    print(f"O resultado da soma é {soma}. {soma} é um número neutro")
else:
    print(f"O resultado da soma é {soma}. {soma} é um número negativo")