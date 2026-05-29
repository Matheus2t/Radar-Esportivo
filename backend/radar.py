def verificar_odds(jogos, valor_odd, liga_escolhida, status_escolhido):
    alertas = []

    for jogo in jogos:
        odd_ok = jogo["odd_casa"] <= valor_odd 
        liga_ok = jogo["liga"].lower() == liga_escolhida.lower() or liga_escolhida.lower() == "todos" 
        status_ok = jogo["status"].lower() == status_escolhido.lower() or status_escolhido.lower() == "todos"
        
        if odd_ok and liga_ok and status_ok:
            alertas.append(jogo)

    return alertas

def listar_ligas(jogos):
    
    ligas = set()
    for jogo in jogos:
        ligas.add(jogo["liga"])
    return sorted(ligas)

def listar_odd(jogos):
    
    odds = set()
    for jogo in jogos:
        odds.add(jogo["odd_casa"])
    return sorted(odds)

def listar_status(jogos):
    
    status_disponiveis = set()
    for jogo in jogos:
        status_disponiveis.add(jogo["status"])
    return sorted(status_disponiveis)