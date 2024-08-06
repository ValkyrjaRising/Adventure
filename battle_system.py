import random

import enemies
from enemies import enemy_select, enemy_score_values
import character_info


def battlestate(score, character, enemy, battle_continue):
    print(f'A wild {enemy.name} has appeared!')

    while enemy.health > 0:
        print('Choose your action!')
        try:
            choice = int(input('1. Attack \n2. Magic \n3. Item \n4. Use Skill \n5. Run Away! \n'))
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
        elif choice == 2:
            print(f'You cast a spell at {enemy.name}')
        elif choice == 3:
            print(f'You use an item. #enter item name and effect here')
        elif choice == 4:
            print(f'You use your skill. #enter skill name and effect here')
        elif choice == 5:
            print(f'You run away from {enemy.name}')

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
            print('The enemy dropped some loot!')
            print(f'You\'re score is currently {score}')
            enemy = enemies.generate_enemy()
            while True:
                new_challenge = input("Do you want to continue fighting? \n(Yes/No): ").strip()
                if new_challenge.capitalize() in ['Yes', 'Y']:
                    battle_continue = True
                    break
                elif new_challenge.capitalize() in ['No', 'N']:
                    battle_continue = False
                    break
                else:
                    print('Please enter a valid option')
            return score, character, enemy, battle_continue
