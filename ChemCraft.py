import sys, os, json

elements = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl', 'Se', 'Br', 'I', 'Li', 'Na', 'K', 'Rb', 
            'Cs', 'Fr', 'Fe', 'Al', 'Si']
recipes = {}

pointers = {'pointer1': 'None', 'pointer2': 'None', 'pointer3': 'None', 'pointer4': 'None'}

with open('recipes.json', 'r') as file:
    recipes = json.load(file)

def Reactionist(A, B):
    for recipe in recipes:
        if recipes[recipe]['A'] == A and recipes[recipe]['B'] == B or recipes[recipe]['A'] == B and recipes[recipe]['B'] == A:
            answer = {'A': recipes[recipe]['outputA'], 'B': recipes[recipe]['outputB']}
            return answer
    answer = {'A': A, 'B': B}
    return answer

while True:
    print('Pointer 1 = {}'.format(pointers['pointer1']))
    print('Pointer 2 = {}'.format(pointers['pointer2']))
    print('Pointer 3 = {}'.format(pointers['pointer3']))
    print('Pointer 4 = {}'.format(pointers['pointer4']))
    print('---------------------------------------')
    part1 = input('part1>>>   ')
    while part1.lower() not in ['pointer1', 'pointer2', 'pointer3', 'pointer4']:
        print('wrong word')
        part1 = input('part1>>>   ')
    part2 = input('part2>>>   ')
    while part2 not in ['+', '=', 'trash']:
        print('wrong word')
        part2 = input('part2>>>   ')
    if part2 == '+':
        part3 = input('part3>>>   ')
        while part3.lower() not in ['pointer1', 'pointer2', 'pointer3', 'pointer4'] or part3.lower() == part1:
            print('wrong word')
            part3 = input('part3>>>   ')
        answer = Reactionist(pointers[part1], pointers[part3])
        pointers[part1] = answer['A']
        pointers[part3] = answer['B']
    if part2 == '=':
        element = input('element>>>   ')
        while element not in elements:
            print('no such element')
            element = input('element>>>   ')
        pointers[part1] = element
    if part2 == 'trash':
        pointers[part1] == 'None'
    
