'''
Questão 8 - Faça um programa que leia três números e, em seguida, exiba-os em ordem crescente.
'''

numeros_ordem_crescente = []

for i in range(1,4):
    numero = int(input("Digite o {}º número: ".format(i)))
    numeros_ordem_crescente.append(numero)
    
print("Ordem crescente: ", sorted(numeros_ordem_crescente))
