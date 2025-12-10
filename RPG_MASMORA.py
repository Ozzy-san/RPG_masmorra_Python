import random 
import time

# O Herói (Vida e Poções são mantidas entre as lutas!)
hero = { "nickname": "Schwarzer", "vida": 100, "defesa": 10 }
pocoes = 3 

# A LISTA DE INIMIGOS (A Masmorra)
dungeon = [
    { "nickname": "Goblin Magrelo", "vida": 30, "defesa": 0 },
    { "nickname": "Orc Guerreiro", "vida": 80, "defesa": 5 },
    { "nickname": "CHEFE DRAGÃO", "vida": 150, "defesa": 15 }
]

def receber_dano(alvo, quantidade):
    dano_real = quantidade - alvo['defesa']
    if dano_real < 0: dano_real = 0
    alvo['vida'] -= dano_real
    if alvo['vida'] < 0: alvo['vida'] = 0
    print(f" > {alvo['nickname']} tomou {dano_real} de dano! (Vida: {alvo['vida']})")

print("--- VOCÊ ENTROU NA MASMORRA! ---")

# --- LOOP DA CAMPANHA (Passa por cada inimigo da lista) ---
for inimigo_atual in dungeon:
    
    print(f"\n################################")
    print(f"UM NOVO INIMIGO APARECEU: {inimigo_atual['nickname']}")
    print(f"################################")
    time.sleep(1)

    # --- LOOP DA BATALHA (Acontece enquanto os dois estão vivos) ---
    while hero['vida'] > 0 and inimigo_atual['vida'] > 0:
        print(f"\n---{hero['nickname']} Vs {inimigo_atual['nickname']} (Sua Vida: {hero['vida']} | Poções: {pocoes}) ---")
        print("1. Atacar")
        print("2. Usar Poção")
        # Tirei o fugir pra ficar hardcore!
        
        escolha = input("O que fazer? ")

        if escolha == '1':
            dano = random.randint(20, 30) # Aumentei um pouco seu dano
            # Crítico
            if random.randint(1, 10) == 10:
                dano *= 2
                print("CRÍTICO!!!")
            
            receber_dano(inimigo_atual, dano)

        elif escolha == '2':
            if pocoes > 0:
                hero['vida'] += 40 # Melhorei a poção
                if hero['vida'] > 100: hero['vida'] = 100
                pocoes -= 1
                print(f"Glup! Vida recuperada. Restam {pocoes} poções.")
            else:
                print("SEM POÇÕES! Você perdeu o turno procurando na bolsa.")
        
        else:
            print("Comando errado! Perdeu a vez.")

        # Contra-ataque do inimigo (se ele não morreu)
        if inimigo_atual['vida'] > 0:
            time.sleep(1)
            print("\nO inimigo ataca!")
            # O Chefe bate mais forte que os outros?
            # Podemos fazer um sorteio genérico por enquanto
            receber_dano(hero, random.randint(10, 25))

    # --- FIM DA BATALHA ATUAL ---
    if hero['vida'] == 0:
        print("\nVOCÊ MORREU NA MASMORRA...")
        break # Sai do FOR também, fim de jogo
    else:
        print(f"\n>>> VOCÊ DERROTOU O {inimigo_atual['nickname']}! <<<")
        print("Você respira fundo e avança para a próxima sala...")
        time.sleep(2)

# --- FIM DA MASMORRA ---
if hero['vida'] > 0:
    print("\nPARABÉNS! VOCÊ LIMPOU A MASMORRA E SAIU VIVO!")