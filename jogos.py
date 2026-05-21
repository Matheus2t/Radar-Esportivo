def verificar_odds(jogos):
    
    valor_odd = float(input("Qual o valor da odd que você quer: "))
    
    for jogo in jogos:
        if jogo["odd_casa"] <= valor_odd:
            print("Radar:", jogo["casa"], "x", jogo["fora"], "-", jogo["odd_casa"])

jogos = [
    {
        "casa": "Arsenal",
        "fora": "Chelsea",
        "liga": "Premier League",
        "odd_casa": 1.70,
        "status": "pré-live",
    },
    {
        "casa": "Palmeiras",
        "fora": "Flamengo",
        "liga": "Brasileirão",
        "odd_casa": 1.60,
        "status": "pré-live",
    },
    {
        "casa": "Real Madrid",
        "fora": "Barcelona",
        "liga": "La liga",
        "odd_casa": 2.10,
        "status": "ao vivo",
    },

]

verificar_odds(jogos)