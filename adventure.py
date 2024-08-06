import decorator
from character_info import name_select, character_select
from battle_system import battlestate
from enemies import generate_enemy, enemy_score_values


@decorator.welcome_text
def hello(greeting):
    print(f'{greeting}')


def write_score(score, name):
    with open("score.txt", "a") as file:
        file.write(f"{name},{score}\n")


def main():
    hello('Welcome adventurer! Please, introduce yourself and select your path to victory!')
    name = name_select()
    character = character_select(name)
    battle_continue = True
    score = 0
    while True:
        enemy = generate_enemy()
        score, player_health, enemy, battle_continue = battlestate(score, character, enemy, battle_continue)
        #write_score(score, name)
        if not battle_continue:
            break
    print('You got out of battle!')

if __name__ == "__main__":
    main()