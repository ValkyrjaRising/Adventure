# import character_info
# import adventure
# import battle_system
import random

character_loot = {
    "Potion": "0",
    "Hi-Potion": "0",
    "Super-Potion": "0",
    "Ether": "0",
    }

#common 1-10
#uncommon 10-19
#rare 20-25

def loot():
    c, un, r = 10,19,25
    randomizer = random.randint(1,25)
    print(f'{randomizer}')
    possible_common_loot = ['Potion', 'Ether']
    possible_uncommon_loot = ['Hi-Potion', 'Sword', 'Armor']
    possible_rare_loot = ['Sword+1', 'Armor+1', 'Super-Potion']
    if randomizer <= c:
        loot = random.choice(possible_common_loot)
        return loot
    elif un >= randomizer > c:
        loot = random.choice(possible_uncommon_loot)
        return loot
    elif r >= randomizer >= un:
        loot = random.choice(possible_rare_loot)
        return loot



