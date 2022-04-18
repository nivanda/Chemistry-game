import sys, os

elements = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl', 'Se', 'Br', 'I', 'Li', 'Na', 'K', 'Rb', 
            'Cs', 'Fr']

pointers = {'pointer1': 'None', 'pointer2': 'None', 'pointer3': 'None', 'pointer4': 'None'}

def Reactionist(A, B):
    if A == 'H' and B == 'O' or A == 'O' and B == 'H':
        answer = {'A': 'H2O2', 'B': 'None'}
        return answer
    elif A == 'H2O2' and B == 'H' or A == 'H' and B == 'H2O2':
        answer = {'A': 'H2O', 'B': 'H2O'}
        return answer
    elif A == 'S' and B == 'O' or A == 'O' and B == 'S':
        answer = {'A': 'SO2', 'B': 'None'}
        return answer
    elif A == 'SO2' and B == 'O' or A == 'O' and B == 'SO2':
        answer = {'A': 'SO3', 'B': 'SO3'}
        return answer
    elif A == 'SO3' and B == 'H2O' or A == 'H2O' and B == 'SO3':
        answer = {'A': 'H2SO4', 'B': 'None'}
        return answer
    else:
        answer = {'A': A, 'B': B}

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
    
