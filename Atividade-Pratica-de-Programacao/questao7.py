'''
Questão 7 - Quatro times estão disputando as semifinais de um campeonato de futebol. Leia os gols que cada time marcou em suas partidas e informe qual time saiu vencedor. Em caso de empate em uma das partidas, leia o número de pênaltis cobrados corretamente (valores entre 0 e 5) para cada time. Supondo que haverá dois times vencedores das partidas, exiba-os. Exemplo de mensagem final: “Os times A e B estão na grande final!”.
'''

contador = 1
equipes = []

def equipe(nome,gols):
    return nome,gols

def vencedor_penalty(time1,time2):
        while True:
            time1_gols = int(input(f"Digite o número de gols do time {time1[0]}: "))
            time2_gols = int(input(f"Digite o número de gols do time {time2[0]}: "))
           
            if time1_gols > time2_gols: 
                return time1 
                break
            elif time2_gols > time1_gols:
                return time2
                break

def vencedor_partida(time1,time2):
    if time1[1] > time2[1]:
        return time1
    elif time2[1] > time1[1]:
        return time2
    else:
        return vencedor_penalty(time1,time2)
    
while(contador <= 4):
    nome = input(f"Digite o nome do {contador}º time: ")
    gols = int(input(f"Digite o número de gols do {contador}º time: "))
    equipes.append(equipe(nome,gols))
    contador += 1

timeA = equipes[0]
timeB = equipes[1]
timeC = equipes[2]
timeD = equipes[3]

finalista1 = vencedor_partida(timeA,timeB)
finalista2 = vencedor_partida(timeC,timeD)

print(f"Os times {finalista1[0]} e {finalista2[0]} estão na grande final!")
