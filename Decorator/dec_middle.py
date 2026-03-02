import functools

def require_kwargs(*neces_kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            err=0
            for kwarg in neces_kwargs:
                if kwarg not in kwargs:
                    #print(f"Required kwarg '{kwarg}' not provided")
                    err+=1
                    raise ValueError(f"Required kwarg '{kwarg}' not provided")
            if err:
                return err
            else:
                return ['OK', func.__name__]

        return wrapper
    return decorator

@require_kwargs('list')
def some_func(list=[], number=0):
    pass

@require_kwargs("user_id", "role")
def process_request(**kwargs):
    print(f"Обработка запроса с параметрами: {kwargs}")

print(some_func(list=[1,2,3,4,5]))
#'list', 'number'
#list=[1,2,3,4,5], number=6, boo=True)
print()
print()
print(process_request(user_id=10, role="admin", action="delete"))

process_request(user_id=10, role="admin", action="delete")
