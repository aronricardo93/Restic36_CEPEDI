'''
Questão 3 - Elabore um programa que lê o nome e a nota de um aluno, depois exibe esses dados, mas com a nota formatada para exibir apenas uma casa decimal.
'''

nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = float(input("Digite a nota do aluno: "))

print("Nome do aluno: ", nome_aluno)
print(f"Nota do aluno: {nota_aluno:.1f}") 

#outra forma de exibir a nota com uma casa decimal usando o .format()
#print("Nota do aluno: {:.1f}".format(nota_aluno))
