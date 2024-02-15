

xp_jogador = int(input("Digite o XP do jogador: "))
Nome_jogador = input("Digite o Nome do jogador: ")

def classificar_jogador(xp):
    if 0 > xp:
        return "CORROMPIDO"
    
    elif 0<= xp <= 1000:
        return "FERRO"
    
    elif 1001 <= xp <=2000:
        return "BRONZE"
    
    elif 2001 <= xp <=5000:
        return "PRATA"
    
    elif 5001 <= xp <= 7000:
        return "OURO"
    
    elif 7001 <= xp <= 8000:
        return "PLATINA"
    
    elif 8001 <= xp <=9000:
        return "ASCENDENTE"
    
    elif 9001 <= xp <=10000:
        return "IMORTAL"
    
    elif xp >= 10001:
        return"RADIANTE"
    

print("O Herói de nome",Nome_jogador,"está no nível ", classificar_jogador(xp_jogador))    