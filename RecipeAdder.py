import json, sys

recipes = {}

with open('recipes.json', 'r') as file:
    recipes = json.load(file)

while True:
    command = input(">>>   ")
    while command.lower() not in ['quit', 'add', 'remove']:
        print('Wrong command')
        command = input(">>>   ")
    if command == 'quit':
        with open('recipes.json', 'w') as file:
            json.dump(recipes, file, indent=1)
        sys.exit()
    if command == 'add':
        name = input('Name = ')
        while name in recipes:
            print('you already have this')
            name = input('Name = ')
        A = input('A = ')
        B = input('B = ')
        outputA = input('Output A = ')
        outputB = input('Output B = ')
        recipes[name] = {'A': A, 'B': B, 'outputA': outputA, 'outputB': outputB}
    if command == 'remove':
        name = input('Name = ')
        while name not in recipes:
            print("you don't have this")
            name = input('Name = ')
        removedItem = recipes.pop(name, None)
        print('You removed: {}'.format(removedItem))