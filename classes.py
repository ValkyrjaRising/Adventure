import random
import decorator

class Character:
    def __init__(self, health, strength, magic, defense, evasion, meva):
        self.health = health
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.evasion = evasion
        self.meva = meva

    @decorator.attack_text
    def attack(self):
        damage = int(self.strength + random.randint(1, 10))
        print(f'You hit the enemy causing {damage} damage!')
        return damage


class Warrior(Character):
    def __init__(self):
        super().__init__(50, 10, 1, 10, 4, 4)


class Thief(Character):
    def __init__(self):
        super().__init__(30, 8, 1, 6, 8, 3)


class Dragoon(Character):
    def __init__(self):
        super().__init__(40, 9, 1, 8, 3, 5)


class Sorcerer(Character):
    def __init__(self):
        super().__init__(20, 4, 10, 6, 4, 8)


class Cleric(Character):
    def __init__(self):
        super().__init__(35, 6, 8, 7, 5, 6)


def hero_select():
    print('Choose your character class.')
    print('1. Warrior \n2. Thief \n3. Dragoon \n4. Sorcerer \n5. Cleric')

    choices = {
        1: Warrior,
        2: Thief,
        3: Dragoon,
        4: Sorcerer,
        5: Cleric
    }

    try:
        choice = int(input('Decision: '))
        character_class = choices.get(choice, Warrior)
    except ValueError:
        print('Invalid choice! Defaulting to Warrior.')
        character_class = Warrior

    return character_class()
