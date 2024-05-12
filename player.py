player = {
    "name": "Victor",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dmg": 25
}

def exibir_player():
        print(
            f"Nome: {player['name']} // Level: {player['level']} // Dano: {player['dmg']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
        )
        
def atacar_npc(npc):
    npc["hp"] -= player["dmg"]
        
def reset_hp():
    player['hp'] = player['hp_max']
    
def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= round(1.6, 0)
        player['hp_max'] *= round(1.5, 0)