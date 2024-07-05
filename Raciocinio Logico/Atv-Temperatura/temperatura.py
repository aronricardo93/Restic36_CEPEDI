temperatura = int(input("Digite a temperatura: "))

if temperatura > 32:
   print("Dia quente")
elif temperatura <= 32 and temperatura > 20:
   print("Dia agradável")
else:
   print("Dia Frio")
if temperatura < 3:
   print("Risco de Neve")