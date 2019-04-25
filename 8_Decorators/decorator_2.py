def new_decorator(original_fun):
    def wrap_func():
        print('before');
        original_fun();
        print('after');

    return wrap_func;


def func_needs_decorator():
    print('I want to be decorated!');

    
func_needs_decorator();
decorated_func = new_decorator(func_needs_decorator);
decorated_func();

print("\n")
@new_decorator
def func_needs_decorator():
    print('I want to be decorated!');

func_needs_decorator();
