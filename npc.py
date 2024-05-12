from player import player


lista_npcs = []
def criar_npc(level):

    novo_npc = {
        "name": f"Monstro #{level}",
        "level": level,
        "dmg": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }
    return novo_npc


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc_gerar = criar_npc(x + 1)
        lista_npcs.append(npc_gerar)


def exibir_npcs():
    for npc in lista_npcs:
        print(
            f"Nome: {npc['name']} // Level: {npc['level']} // Dano: {npc['dmg']} // HP: {npc['hp']}/{npc['hp_max']} // EXP: {npc['exp']}/{npc['exp_max']}"
        )
        
def atacar_player(npc):
    player["hp"] -= npc["dmg"]
    
 
def reset_npc(npc):
    npc['hp'] = npc['hp_max']