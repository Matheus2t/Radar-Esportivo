from jogos import jogos
from radar import verificar_odds

valor_odd = float(input("Qual o valor da odd que você quer: "))
liga_escolhida = input("Qual liga deseja escolher: ")

alertas = verificar_odds(jogos, valor_odd, liga_escolhida)

if len(alertas) == 0:
    print("Não foi encontrado nenhum jogo em nossa base de dados")
else:
    for alerta in alertas:
        print("Radar:", alerta["casa"], "x", alerta["fora"], "-", alerta["odd_casa"])