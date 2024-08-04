import classes



def name_select():
    name = input(f'Please enter your Character\'s name: ')
    print(f'Your name is {name}')
    return name

def character_select():
    character = classes.hero_select()
    return character


name = name_select()
character = character_select()

# character = classes.hero_select(name)