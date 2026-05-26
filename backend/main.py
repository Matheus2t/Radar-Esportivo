from jogos import jogos
from radar import verificar_odds

print("Ligas disponíveis:")
for jogo in jogos:
    print("-", jogo["liga"])

valor_odd = float(input("Qual o valor da odd que você quer: "))
liga_escolhida = input("Qual liga deseja escolher: ")
status_escolhido = input("Qual status deseja filtrar: ")

alertas = verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido)

if len(alertas) == 0:
    print("Não foi encontrado nenhum jogo em nossa base de dados")
else:
    for alerta in alertas:
        print("Radar:", alerta["casa"], "x", alerta["fora"], "-", alerta["odd_casa"])