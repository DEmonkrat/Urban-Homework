import json

def to_json(func):
    def wrapper(*args):
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(func(*args), file, ensure_ascii=False, indent=4)
        return json.dumps(func(*args), ensure_ascii=False, indent=4)

    return wrapper

@to_json
def get_user_data(user_id):
    return {"id": user_id, "name": "John Doe", "permissions": ["read", "write"]\
            , "lib_acc": {"1_book": "Maugli", "2_book": "Karlson"}}

json_string = get_user_data(123)
print(json_string)
# Выведет: {"id": 123, "name": "John Doe", "permissions": ["read", "write"]}
print(type(json_string)) # Выведет: <class 'str'>