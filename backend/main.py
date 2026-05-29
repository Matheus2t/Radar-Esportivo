from jogos import jogos
from radar import verificar_odds, listar_ligas, listar_odd, listar_status

print("Odds disponíveis:")
for odd in listar_odd(jogos):
    print("-", odd)
valor_odd = float(input("Qual o valor da odd que você quer: "))
print("Ligas disponíveis:")
for liga in listar_ligas(jogos):
    print("-", liga)
liga_escolhida = input("Qual liga deseja escolher: ")
print("Status disponíveis:")
for status in listar_status(jogos):
    print("-", status)
status_escolhido = input("Qual status deseja filtrar: ")

alertas = verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido)
alertas_ordenados = sorted(alertas, key=lambda alerta: alerta["odd_casa"])

if len(alertas) == 0:
    print("Não foi encontrado nenhum jogo em nossa base de dados, que possui", len(jogos), "jogos")
else:
    print("Foram encontrados", len(alertas) , "jogos")
    for alerta in alertas_ordenados:        
        print("Radar:", alerta["casa"], "x", alerta["fora"], "-", alerta["odd_casa"])