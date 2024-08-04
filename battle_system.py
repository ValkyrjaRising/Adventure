import random
from enemies import enemy, boss, generate_enemy, generate_boss
import character_info

player_health = character_info.character.health

def battlestate(score):
    enemy
    global player_health
    player_health = character_info.character.health
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
            print(f'The enemy dropped some loot! ')
            score = 


battlestate(score=0)