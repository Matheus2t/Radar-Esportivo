def verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido):
    alertas = []

    for jogo in jogos:
        if jogo["odd_casa"] <= valor_odd and jogo["liga"].lower() == liga_escolhida.lower() and jogo["status"].lower() == status_escolhido.lower():
            alertas.append(jogo)

    return alertas

def listar_ligas(jogos):
    
    ligas = set()
    for jogo in jogos:
        ligas.add(jogo["liga"])
    return ligas

def listar_odd(jogos):
    
    odds = set()
    for jogo in jogos:
        odds.add(jogo["odd_casa"])
    return odds

def listar_status(jogos):
    
    status_disponiveis = set()
    for jogo in jogos:
        status_disponiveis.add(jogo["status"])
    return status_disponiveis