creds = {'name1': 'pass1', 'name2': 'pass2'}
def auth_required(func):
    def wrapper_decorator(*args, **kwargs):
        input_name = input("enter your name:")
        input_password = input("enter your password:")
        if input_name not in creds or creds[input_name] != input_password:
            return "Authentication required"
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator
    return decorate

@auth_required
def some_func(a, b):
    return(a + b)

print(some_func(10, 10))