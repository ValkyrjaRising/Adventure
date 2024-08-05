import classes

def name_select():
    name = input('Please enter your Character\'s name: ')
    print(f'Your name is {name}')
    return name

def character_select(name):
    character = classes.hero_select()
    print(f'You\'re now {name} the {type(character).__name__}!')
    return character

