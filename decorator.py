def battle_text(func):
    def wrap_func(*args, **kwargs):
        print('//////--------------/////////')
        func(*args, **kwargs)
        print('//////--------------/////////')
    return wrap_func
