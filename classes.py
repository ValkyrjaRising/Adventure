import random
import decorator

class Character:
    def __init__(self, health, strength, magic, mp, defense, evasion, meva):
        self.health = health
        self.strength = strength
        self.magic = magic
        self.mp = mp
        self.defense = defense
        self.evasion = evasion
        self.meva = meva
        self.inventory = []
        self.skills = []
        self.spells = []
        self.has_mp = False

    @decorator.attack_text
    def attack(self):
        damage = int(self.strength + random.randint(1, 10))
        print(f'You hit the enemy causing {damage} damage!')
        return damage
    def add_inventory(self,item):
        self.inventory.append(item)
        return self.inventory
    def remove_inventory(self, item):
        self.inventory.remove(item)
        return self.inventory


class Warrior(Character):
    def __init__(self):
        super().__init__(50, 10, 1, 0,10, 4, 4)
        self.skills = ['Boost']
        self.has_mp = False

    def Boost(self):
        self.strength += 3
        turn_counter = 0
        print(f'You use Boost. Strength is increased by 3 for 1 turn.')
        return turn_counter


class Thief(Character):
    def __init__(self):
        super().__init__(30, 8, 1, 0,6, 8, 3)
        self.has_mp = False


class Dragoon(Character):
    def __init__(self):
        super().__init__(40, 9, 1, 0,8, 3, 5)
        self.skills = ['Jump']
        self.has_mp = False

    def Jump(self):
        invulnerable = 1
        enhanced_attack = self.strength + 4
        return invulnerable

class Sorcerer(Character):
    def __init__(self):
        super().__init__(30, 4, 10, 20,6, 4, 8)
        self.has_mp = True
        self.spells = ['Firebolt']

    def Firebolt(self):
        damage = int(self.magic + random.randint(1,8))
        self.mp -= 5
        print(f'You cast Firebolt at the enemy, causing {damage} damage!')
        return damage


class Cleric(Character):
    def __init__(self):
        super().__init__(35, 6, 8, 20,7, 5, 6)
        self.has_mp = True


@decorator.class_decorator
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
