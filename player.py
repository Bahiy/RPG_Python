# Player unico com valores que serão trabalhados durante o jogo
player = {
    "name": "Victor",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dmg": 25
}

# exibe informações do Player
def exibir_player():
        print(
            f"Nome: {player['name']} // Level: {player['level']} // Dano: {player['dmg']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
        )
        
# função para decrementar a vida do player com base no dano do NPC
def atacar_npc(npc):
    npc["hp"] -= player["dmg"]
        
#  Reset de vida para ser usado após a batalha
def reset_hp():
    player['hp'] = player['hp_max']
    
# Verificação para level up e incremento dos atributos
def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= round(1.6, 0)
        player['hp_max'] *= round(1.5, 0)