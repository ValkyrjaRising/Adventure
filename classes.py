#Hero Classes
import random

import character_info

class Warrior(object):
    health = 50
    strength = 10
    magic = 1
    defense = 10
    evasion = 4
    meva = 4
    def attack(self):
        damage = character_info.character.strength + random.randint(1,10)
        print(f'You hit the enemy causing {damage} damage!')
        return damage


class Thief(object):
    health = 30
    strength = 8
    magic = 1
    defense = 6
    evasion = 8
    meva = 3
class Dragoon(object):
    health = 40
    strength = 9
    magic = 1
    defense = 8
    evasion = 3
    meva = 5
class Sorcerer(object):
    health = 20
    strength = 4
    magic = 10
    defense = 6
    evasion = 4
    meva = 8
class Cleric(object):
    health = 35
    strength = 6
    magic = 8
    defense = 7
    evasion = 5
    meva = 6


def hero_select():
    print('Choose your character class.')
    print('1. Warrior \n2. Thief \n3. Dragoon \n4. Sorcerer \n5. Cleric')
    try:
        choice = int(input('Decision: '))
    except ValueError:
        print('Please enter a valid choice!!')
        hero_select()
    else:
        if choice == 1:
            character = Warrior()
            print(f'You\'re now {character_info.name} the Warrior!')
            print(f'Health: {character.health} \nStrength: {character.strength} \nMagic: {character.magic} \nDefense: {character.defense} \nEvasion: {character.evasion} \nMagic Evasion: {character.meva}')
        elif choice == 2:
            character = Thief()
            print(f'You\'re now {character_info.name} the Thief!')
            print(f'Health: {character.health} \nStrength: {character.strength} \nMagic: {character.magic} \nDefense: {character.defense} \nEvasion: {character.evasion} \nMagic Evasion: {character.meva}')
        elif choice == 3:
            character = Dragoon()
            print(f'You\'re now {character_info.name} the Dragoon!')
            print(f'Health: {character.health} \nStrength: {character.strength} \nMagic: {character.magic} \nDefense: {character.defense} \nEvasion: {character.evasion} \nMagic Evasion: {character.meva}')
        elif choice == 4:
            character = Sorcerer()
            print(f'You\'re now {character_info.name} the Sorcerer!')
            print(f'Health: {character.health} \nStrength: {character.strength} \nMagic: {character.magic} \nDefense: {character.defense} \nEvasion: {character.evasion} \nMagic Evasion: {character.meva}')
        elif choice == 5:
            character = Cleric()
            print(f'You\'re now {character_info.name} the Thief!')
            print(f'Health: {character.health} \nStrength: {character.strength} \nMagic: {character.magic} \nDefense: {character.defense} \nEvasion: {character.evasion} \nMagic Evasion: {character.meva}')
    return character


