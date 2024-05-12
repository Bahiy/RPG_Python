from player import *
from npc import *

def quebra_pau(npc):
     while npc['hp'] > 0 and player['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_de_batalha(npc)
        
def log_de_batalha(npc):
    if player['hp'] > 0:
        print(
            f"O {player['name']} venceu a batalha! {npc['exp']} pontos de EXP adquiridos")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['name']} venceu!")

def inicar_batalha(npc):
    quebra_pau(npc)
    log_de_batalha(npc)
    level_up()
    reset_hp()
    reset_npc(npc)


def exibir_info_de_batalha(npc):
    print(f"Player: {player['name']} // HP: {player['hp']}/{player['hp_max']}")
    print(f"NPC ATACADO: {npc['name']} // HP: {npc['hp']}/{npc['hp_max']}")
    print("\n", "-"*50, "\n")


gerar_npcs(10)
# exibir_npcs()

npc_selecionado = lista_npcs[1]

inicar_batalha(npc_selecionado)
