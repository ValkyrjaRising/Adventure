import random
class Goblin(object):
    name = "Goblin"
    health = 30
    strength = 4
    defense = 4
    magic = 0
    evasion = 3
    meva = 8
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage

class Cultist(object):
    name = "Cultist"
    health = 35
    strength = 3
    defense = 4
    magic = 7
    evasion = 7
    meva = 4
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage
class Sahagin(object):
    name = "Sahagin"
    health = 45
    strength = 8
    defense = 5
    magic = 4
    evasion = 3
    meva = 6
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage
class Orc(object):
    name = "Orc"
    health = 50
    strength = 7
    defense = 6
    magic = 1
    evasion = 1
    meva = 3
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage

class Bat(object):
    name = "Bat"
    health = 25
    strength = 3
    defense = 4
    magic = 0
    evasion = 8
    meva = 4
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage

class Wolf(object):
    name = "Wolf"
    health = 40
    strength = 6
    defense = 4
    evasion = 8
    meva = 2
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage


class Dragon(object):
    name = "Red Dragon"
    health = 150
    strength = 12
    defense = 6
    magic = 7
    evasion = 6
    meva = 6
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage

class Behemoth(object):
    name = "Behemoth"
    health = 130
    strength = 14
    defense = 7
    magic = 3
    evasion = 6
    meva = 4
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage

class Adamantoise(object):
    name = "Adamantoise"
    health = 200
    strength = 8
    defense = 10
    magic = 5
    evasion = 6
    meva = 4
    def monster_attack(self):
        damage = enemy.strength + random.randint(1,6)
        return damage


enemy_list = [Goblin(), Orc(), Bat(), Cultist(), Sahagin(), Wolf()]
boss_list = [Dragon(), Behemoth(), Adamantoise()]


def enemy_select(*args):
    chance = random.randint(0,5)
    enemy = enemy_list[chance]
    return enemy

def boss_select():
    chance = random.randint(0, 2)
    boss = boss_list[chance]
    return boss

def generate_enemy():
    generated_enemy = enemy_select()
    return generated_enemy

def generate_boss():
    boss = boss_select()
    return boss
enemy = enemy_select()
boss = 'default'
generated_enemy = 'default'

