import decorator
from battle_system import battlestate as bs
from enemies import enemy_select, boss_select

@decorator.battle_text
def hello(greeting):
    print(f'{greeting}')

hello(f'Welcome adventurer! Please, introduce yourself and select your path to victory!')
import character_info

# def name_select(name):
#     name = input(f'Please enter your Character\'s name: ')
#     print(f'Your name is {name}')
#     return name

def writeScore(score, name):
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()

bs()


#
# hello(f'Hello, Welcome to the game!')
# name = name_select(name)
# character = classes.hero_select(name)
#
# bs()