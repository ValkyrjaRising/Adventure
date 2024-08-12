import random

import classes
import decorator
from loot import loot
import enemies
from enemies import enemy_select, enemy_score_values
import character_info


@decorator.victory_text
def victory(score, character, enemy):
    score += enemy_score_values.get(enemy.name, 0)
    enemy_loot = loot()
    print(f'The {enemy.name} dropped a {enemy_loot}!')
    character.add_inventory(enemy_loot)
    print(f'You\'re score is currently {score}')
    enemy = enemies.generate_enemy()
    return score, character, enemy, enemy_loot, loot


def battlestate(score, character, enemy, battle_continue):
    print(f'A wild {enemy.name} has appeared!')
    skip_enemy_combat = False
    turn_counter = 0
    invulnerable = False
    defend_status = False
    #Player Turn
    while enemy.health > 0:
        print('Choose your action!')
        try:
            choice = int(input('1. Attack \n2. Magic \n3. Item \n4. Use Skill \n5. Defend \n6. Run Away! \n'))
        except ValueError:
            print('Please enter a valid choice!')
            continue

        if choice == 1:
            print(f'You swing your sword, attacking the {enemy.name}')
            if random.randint(1, 10) > 3:
                attack = character.attack()
                enemy.health -= attack
                skip_enemy_combat = False
            else:
                print(f'You try to hit {enemy.name} but miss!')
                skip_enemy_combat = False
        elif choice == 2:
            print(f'{character.spells}')
            spell_choice = input(f'Select the spell you want to use: \n').strip().capitalize()
            continue_use_skill = True
            while continue_use_skill:
                if spell_choice in character.spells:
                    spell_method = getattr(character, spell_choice, None)
                    if callable(spell_method):
                        attack = spell_method()
                        continue_use_skill = False
                        enemy.health -= attack
                        skip_enemy_combat = False
                else:
                    print(f'You don\'t know that spell or have not entered a valid choice!')
                    print(f'Returning to the Action Menu')
                    skip_enemy_combat = True
                    break
        elif choice == 3:
            continue_use_item_input = True
            while continue_use_item_input:
                print(character.inventory)
                use_inventory = input('Enter the name of the item you want to use.\n').capitalize().strip()
                if use_inventory == 'Hi-Potion' or use_inventory == 'Hi-potion' or use_inventory == 'Hipotion':
                    use_inventory = 'Hi-Potion'
                elif use_inventory == 'Super-Potion' or use_inventory == 'Super-potion' or use_inventory == 'Superpotion':
                    use_inventory = 'Super-Potion'
                elif use_inventory == 'Armor +1':
                    use_inventory = 'Armor+1'
                elif use_inventory == 'Sword +1':
                    use_inventory = 'Sword+1'
                if use_inventory in character.inventory:
                    if use_inventory == 'Potion':
                        character.health += 10
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your hp rose by 10 and is now {character.health}')
                        break
                    elif use_inventory == 'Ether':
                        character.mp += 10
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your mp rose by 10 and is now {character.mp}')
                        break
                    elif use_inventory == 'Hi-Potion':
                        character.health += 15
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your hp rose by 15 and is now {character.health}')
                        break
                    elif use_inventory == 'Super-Potion':
                        character.health += 25
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your hp rose by 25 and is now {character.health}.')
                        break
                    elif use_inventory == 'Armor':
                        character.defense += 2
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your defense has risen by 2 and is now {character.defense}!')
                        break
                    elif use_inventory == 'Armor+1':
                        character.defense += 4
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your defense has risen by 4 and is now {character.defense}!')
                        break
                    elif use_inventory == 'Sword':
                        character.strength += 2
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your attack has risen by 2 and is now {character.strength}!')
                        break
                    elif use_inventory == 'Sword+1':
                        character.strength += 4
                        character.remove_inventory(use_inventory)
                        print(f'You use the {use_inventory}! Your attack has risen by 4 and is now {character.strength}!')
                        break
                else:
                    print('That item does not exist in your inventory.')
                    print('Returning to the Action Menu.')
                    skip_enemy_combat = True
                    continue_use_item_input = True
                    break
        elif choice == 4:
            print(f' {character.skills}')
            skill_choice = input(f'Select the skill you want to use: \n').strip().capitalize()
            continue_use_skill = True
            while continue_use_skill:
                if skill_choice in character.skills:
                    skill_method = getattr(character, skill_choice, None)
                    if callable(skill_method):
                        skill_method()
                        continue_use_skill = False
                else:
                    print(f'You don\'t know that skill or have not entered a valid choice!')
                    print(f'Returning to the Action Menu')
                    skip_enemy_combat = True
                    break
        elif choice == 5:
            if not defend_status:
                defend_status = True
            regain_health = int(character.health * 0.20)
            character.health += regain_health
            print(f'You defend against the next attack and gain {regain_health} health, putting you at {character.health}!')
            if character.has_mp:
                regain_mp = int(character.mp * 0.35)
                character.mp += regain_mp
                print(f'You replenish {regain_mp} MP, putting you at {character.mp}!')
        elif choice == 6:
            print(f'You defend against the next attack and regain some health and mp')

        if skip_enemy_combat:
            continue

        #Enemy Turn
        if enemy.health > 0:
            if defend_status:
                if random.randint(1, 10) > 3:
                    attack = enemy.monster_attack() // 2
                    enemy_damage = abs((attack - character.defense))
                    character.health -= enemy_damage
                    print(f'The {enemy.name} swings at you! It hits you dealing {enemy_damage}. You have {character.health} HP remaining!')
                    print('xxxxxxxxx!!!!!!!!!xxxxxxxxxx')
                    defend_status = False
                else:
                    print(f'The {enemy.name} swings at you and misses!')
                    defend_status = False
            elif invulnerable:
                if random.randint(1, 10) > 3:
                    attack = enemy.monster_attack()
                    enemy_damage = 0
                    character.health -= enemy_damage
                    print(f'The {enemy.name} swings at you! You are invulnerable and take no damage!')
                    print('xxxxxxxxx!!!!!!!!!xxxxxxxxxx')
                    invulnerable = False
                else:
                    print(f'The {enemy.name} swings at you and misses!')
                    invulnerable = False
            elif random.randint(1, 10) > 3:
                attack = enemy.monster_attack()
                enemy_damage = abs((attack - character.defense))
                character.health -= enemy_damage
                print(
                    f'The {enemy.name} swings at you! It hits you dealing {enemy_damage}. You have {character.health} HP remaining!')
                print('xxxxxxxxx!!!!!!!!!xxxxxxxxxx')
            else:
                print(f'The {enemy.name} swings at you and misses!')

        #End Combat
        else:
            score, character, enemy, enemy_loot, loot = victory(score, character, enemy)
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
        skip_enemy_combat = False
        turn_counter += 1
        print(f'Turn {turn_counter} completed!')

#   item_effects = {
        #             'Potion': (10, 'Potion'),
        #             'Hi-Potion': (15, 'Hi-Potion'),
        #             'Super-Potion': (25, 'Super-Potion')
        #         }
        #
        #   if use_inventory in character.inventory:
        #     heal_amount, item_name = item_effects[item]
        #     character.health += heal_amount
        #     character.remove_inventory(item_name)
        #     print(f'You use the {item_name}! Your HP rose by {heal_amount} and is now {character.health}')
        #   else:
        #     print('Item not found or not usable.')


# score += enemy_score_values.get(enemy.name, 0)
# enemy_loot = loot()
# print(f'The enemy dropped a {enemy_loot}')
# character.add_inventory(enemy_loot)
# print(f'You\'re score is currently {score}')
# enemy = enemies.generate_enemy()

