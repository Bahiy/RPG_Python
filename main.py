from player import *
from npc import *

# Função para ataques entre npc e player
def quebra_pau(npc):
     while npc['hp'] > 0 and player['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_de_batalha(npc)
        
# Mostra quem ganhou a batalha
def log_de_batalha(npc):
    if player['hp'] > 0:
        print(
            f"O {player['name']} venceu a batalha! {npc['exp']} pontos de EXP adquiridos")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['name']} venceu!")

# Inicia a batalha entre NPC e Player, reseta atributos e/ou da up level no player
def inicar_batalha(npc):
    quebra_pau(npc)
    log_de_batalha(npc)
    level_up()
    reset_hp()
    reset_npc(npc)

# Exibe informações sobre como ficou o player e como ficou o NPC após a batalha
def exibir_info_de_batalha(npc):
    print(f"Player: {player['name']} // HP: {player['hp']}/{player['hp_max']}")
    print(f"NPC ATACADO: {npc['name']} // HP: {npc['hp']}/{npc['hp_max']}")
    print("\n", "-"*50, "\n")


gerar_npcs(10)
# exibir_npcs()

npc_selecionado = lista_npcs[1]

inicar_batalha(npc_selecionado)
