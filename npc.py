from player import player

# Lista onde será armazenado os NPCS
lista_npcs = []

# Cria um npc em um dicionario com valores das chaves relacionados com level
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

# Responsável por gerar os NPCS e adicionar a lista de NPCS
def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc_gerar = criar_npc(x + 1)
        lista_npcs.append(npc_gerar)

# Exibe chaves e valores do NPC formatado
def exibir_npcs(npc):
    for npc in lista_npcs:
        print(
            f"Nome: {npc['name']} // Level: {npc['level']} // Dano: {npc['dmg']} // HP: {npc['hp']}/{npc['hp_max']} // EXP: {npc['exp']}/{npc['exp_max']}"
        )
        
# efeito de redução de HP
def atacar_player(npc):
    player["hp"] -= npc["dmg"]
    
#  reset de vida após a batalha
def reset_npc(npc):
    npc['hp'] = npc['hp_max']