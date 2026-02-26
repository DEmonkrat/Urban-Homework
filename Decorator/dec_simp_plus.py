def prefix (p: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(p + func(*args, **kwargs))
        return wrapper
    return decorator

@prefix("[LOGGER]: ")
def get_status(code):
    return f"Status code is {code}"

get_status(200)
get_status(500)