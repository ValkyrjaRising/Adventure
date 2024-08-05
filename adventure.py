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

    score = 0
    while True:
        enemy = generate_enemy()
        score, player_health, enemy = battlestate(score, character, enemy)
        #write_score(score, name)


if __name__ == "__main__":
    main()