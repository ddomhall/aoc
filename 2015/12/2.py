import json
input = json.load(open('input.json'))

total = 0
def search(jsn):
    if type(jsn) == int:
        global total
        total += jsn
        return
    elif type(jsn) == list:
        for item in jsn:
            search(item)
    elif type(jsn) == dict:
        if 'red' in jsn.values():
            return
        for item in jsn.values():
            search(item)
    else:
        return

search(input)
print(total)

