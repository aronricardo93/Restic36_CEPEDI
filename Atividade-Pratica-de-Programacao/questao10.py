'''Questão 10 - Faça um programa que calcule a conta de energia elétrica, solicitando apenas o número de kW/h e levando em consideração:

a)     O preço do kW/h é R$ 0,56.

b)     O valor da Geração de energia é 41% do valor do consumo.

c)     O valor de imposto é de 22,52% do valor do consumo.

d)     Qual a “bandeira” (acréscimo a cada kWh consumido) tarifária está em vigor:

                        I.         Amarela: R$ 0,015.

                       II.         Bandeira vermelha - Patamar 1: R$ 0,040.

                      III.         Bandeira vermelha - Patamar 2: R$ 0,060.

Informe o valor final da conta de Energia.'''

kw = float(input("Digite o KW/h: "))
consumo_base = kw * 0.56
geracao_energia = consumo_base * 0.41
imposto = consumo_base * 0.2252
    

bandeira = int(input("Escolha a bandeira:\n[1] Amarela\n[2] Vermelha - Patamar 1\n[2] Vermelha - Patamar 2\n"))

if bandeira == 1:
    valor_total = consumo_base + geracao_energia + imposto + (kw * 0.015)
elif bandeira == 2:
      valor_total = consumo_base + geracao_energia + imposto + (kw * 0.040)
else:
      valor_total = consumo_base + geracao_energia + imposto + (kw * 0.060)
      
print("O valor total do consumo de energia é R${:.2f}".format(valor_total))