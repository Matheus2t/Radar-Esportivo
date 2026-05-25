from jogos import jogos

def verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido):
    alertas = []

    for jogo in jogos:
        if jogo["odd_casa"] <= valor_odd and jogo["liga"] == liga_escolhida and jogo["status"] == status_escolhido:            
            alertas.append(jogo)
            
    return alertas  

valor_odd = float(input("Qual o valor da odd que você quer: "))
liga_escolhida = input("Qual liga deseja escolher: ")
status_escolhido = input("Qual status deseja filtrar: ")

alertas = verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido)

if len(alertas) == 0:
    print("Não foi encontrado nenhum jogo em nossa base de dados")
else:
    for alerta in alertas:
        print("Radar:", alerta["casa"], "x", alerta["fora"], "-", alerta["odd_casa"])
