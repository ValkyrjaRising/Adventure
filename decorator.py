def welcome_text(func):
    def wrap_func(*args, **kwargs):
        print('//////--------------/////////')
        func(*args, **kwargs)
        print('//////--------------/////////')
    return wrap_func

def attack_text(func):
    def wrap_func(*args, **kwargs):
        print('<.........---------.........>')
        result = func(*args, **kwargs)
        print('<.........---------.........>')
        return result
    return wrap_func

def monster_attk(func):
    def wrap_func(*args, **kwargs):
        print('xxxxxxxxx!!!!!!!!!xxxxxxxxxx')
        result = func(*args, **kwargs)
        return result
    return wrap_func
