import decorator

#import classes
import enemies
# from enemies import enemy_select, boss_select

@decorator.welcome_text
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
from battle_system import constant_score
from battle_system import player_constant_health
from battle_system import battlestate as bs
bs(constant_score,player_constant_health)


#
# hello(f'Hello, Welcome to the game!')
# name = name_select(name)
# character = classes.hero_select(name)
#
# bs()