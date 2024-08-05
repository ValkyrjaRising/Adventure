import random
from enemies import enemy, enemy_select, boss, generate_enemy, generate_boss, enemy_score_values, boss_score_values
import character_info
import decorator

player_constant_health = character_info.character.health
player_health = character_info.character.health
constant_score = 0

def battlestate(score, health):
    global enemy
    enemy = enemy_select()
    # global player_health
    global player_constant_health
    player_health = player_constant_health
    print(f'A wild {enemy.name} has appeared!')
    while enemy.health > 0:
        print('Choose your action!')
        choice = int((input(f'1. Attack \n2. Magic \n3. Run Away!')))
        if choice == 1:
            print (f'You swing your sword, attacking the {enemy.name}')
            hit_chance = random.randint(1,10)
            if hit_chance > 3:
                attack = character_info.character.attack()
                enemy.health = enemy.health - attack
            else:
                print(f'You try to hit {enemy.name} but miss!')
        if enemy.health > 1:
            enemy_hit_chance = random.randint(1,10)
            if enemy_hit_chance > 3:
                attack = enemy.monster_attack()
                enemy_damage = abs(attack - character_info.character.defense)
                player_health -= enemy_damage
                print(f'The {enemy.name} swings at you! It hits you dealing {enemy_damage}. You have {player_health} HP remaining!')
            else:
                print(f'The {enemy.name} swings at you and misses!')
        else:
            print(f'You have slain the {enemy.name}!!!')
            player_constant_health = player_health
            enemy_dict_value = enemy.name
            score += enemy_score_values[enemy_dict_value]
            print(f'You\'re score is currently {score}')
            global constant_score
            constant_score = score
            print(f'The enemy dropped some loot! ')


# battlestate(constant_score, player_constant_health)
# print(constant_score)
# print(player_constant_health)
# battlestate(constant_score, player_constant_health)