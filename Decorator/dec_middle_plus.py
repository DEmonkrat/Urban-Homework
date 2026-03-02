import json

j_dump = json.dumps({'key':1, 'val':2, 'dicti': {"li":1, 'lu':2}})
print(type(j_dump))
print(j_dump)
i = 1
for symb in j_dump:
    print(f"Symb number: {i}; value = {symb}")
    i += 1