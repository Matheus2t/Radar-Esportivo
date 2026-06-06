from jogos import jogos
from radar import verificar_odds, listar_ligas, listar_odd, listar_status, contar_jogos_por_liga

print("jogos por liga:")
contagem_ligas = contar_jogos_por_liga(jogos)

for liga, quantidade in contagem_liga.items():
    print("-", liga + ":", quantidade)

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

    tipo_classificacao = input("Qual o tipo da classificação desejada? [geral], [casa], [fora], [todos]: ").lower()

    if tipo_classificacao not in ["geral", "casa", "fora", "todos"]:
        tipo_classificacao = "todos"

        for alerta in alertas_ordenados:
            print("Radar:", alerta["casa"], "x", alerta["fora"])
            print("Odd:", alerta["odd_casa"])
            print("Liga:", alerta["liga"])
            print("Status:", alerta["status"])

        if tipo_classificacao == "geral":
            print(alerta["casa"], "- Geral:", alerta["classificacao_casa"]["geral"])
            print(alerta["fora"], "- Geral:", alerta["classificacao_fora"]["geral"])
        elif tipo_classificacao == "casa":
            print(alerta["casa"], "- Casa:", alerta["classificacao_casa"]["casa"])
            print(alerta["fora"], "- Casa:", alerta["classificacao_fora"]["casa"])
        elif tipo_classificacao == "fora":
            print(alerta["casa"], "- Fora:", alerta["classificacao_casa"]["fora"])
            print(alerta["fora"], "- Fora:", alerta["classificacao_fora"]["fora"])
        elif tipo_classificacao == "todos":
            print(alerta["casa"], "- Geral:", alerta["classificacao_casa"]["geral"])
            print(alerta["fora"], "- Geral:", alerta["classificacao_fora"]["geral"])      
            print(alerta["casa"], "- Casa:", alerta["classificacao_casa"]["casa"])
            print(alerta["fora"], "- Casa:", alerta["classificacao_fora"]["casa"])
            print(alerta["casa"], "- Fora:", alerta["classificacao_casa"]["fora"])
            print(alerta["fora"], "- Fora:", alerta["classificacao_fora"]["fora"])  
                    
        if "h2h" in alerta:
            print("H2H:")
            for confronto in alerta["h2h"]:
                print("-", confronto["casa"], confronto["placar"], confronto["fora"])