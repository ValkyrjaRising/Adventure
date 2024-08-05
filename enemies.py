import random
import decorator
class Enemy:
    def __init__(self, name, health, strength, defense, magic, evasion, meva):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.evasion = evasion
        self.meva = meva

    @decorator.monster_attk
    def monster_attack(self):
        damage = int(self.strength + random.randint(1, 6))
        return damage

# Define specific enemies
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 4, 4, 0, 3, 8)

class Cultist(Enemy):
    def __init__(self):
        super().__init__("Cultist", 35, 3, 4, 7, 7, 4)

class Sahagin(Enemy):
    def __init__(self):
        super().__init__("Sahagin",45,8,5,4,3,6)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc",50,7,6,1,1,3)

class Bat(Enemy):
    def __init__(self):
        super().__init__("Bat",25,3,4,0,8,4)

class Wolf(Enemy):
    def __init__(self):
        super().__init__("Wolf",40,6,4,0,8,2)

# More enemies...
class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon",150,12,6,7,6,6)

class Behemoth(Enemy):
    def __init__(self):
        super().__init__("Behemoth", 130, 14, 7, 3, 6, 4)

class Adamantoise(Enemy):
    def __init__(self):
        super().__init__("Adamantoise", 200, 8, 10, 5, 6, 4)
def enemy_select():
    enemies = [Goblin(), Cultist(), Sahagin(), Orc(), Bat(), Wolf()]  # List of enemy instances
    return random.choice(enemies)

def generate_enemy():
    return enemy_select()

def boss_select():
    bosses = [Dragon(), Behemoth(), Adamantoise()]
    return random.choice(bosses)

def generate_boss():
    boss = boss_select()
    return boss


enemy_score_values = {
    'Goblin': 5, 'Orc': 10, 'Bat': 3,
    'Cultist': 7, 'Sahagin': 10, 'Wolf': 8
}
boss_score_values = {'Dragon': 30, 'Behemoth': 25, 'Adamantoise': 25}

