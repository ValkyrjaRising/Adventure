import random

import enemies
from enemies import enemy_select, enemy_score_values
import character_info


def battlestate(score, character, enemy):
    print(f'A wild {enemy.name} has appeared!')

    while enemy.health > 0:
        print('Choose your action!')
        try:
            choice = int(input('1. Attack \n2. Magic \n3. Run Away! \n'))
        except ValueError:
            print('Please enter a valid choice!')
            continue

        if choice == 1:
            print(f'You swing your sword, attacking the {enemy.name}')
            if random.randint(1, 10) > 3:
                attack = character.attack()
                enemy.health -= attack
            else:
                print(f'You try to hit {enemy.name} but miss!')

        if enemy.health > 0:
            if random.randint(1, 10) > 3:
                attack = enemy.monster_attack()
                enemy_damage = abs((attack - character.defense))
                character.health -= enemy_damage
                print(f'The {enemy.name} swings at you! It hits you dealing {enemy_damage}. You have {character.health} HP remaining!')
                print('xxxxxxxxx!!!!!!!!!xxxxxxxxxx')
            else:
                print(f'The {enemy.name} swings at you and misses!')
        else:
            print(f'You have slain the {enemy.name}!!!')
            score += enemy_score_values.get(enemy.name, 0)
            print(f'You\'re score is currently {score}')
            print('The enemy dropped some loot!')
            enemy = enemies.generate_enemy()
            return score, character, enemy
