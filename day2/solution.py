import numpy as np

translation = {'A': 'Rock', 'X': 'Rock', 'B': 'Paper', 'Y': 'Paper', 'C': 'Scissors', 'Z': 'Scissors'}
decoding = {('A', 'X'): ('A', 'C'),
            ('A', 'Y'): ('A', 'A'),
            ('A', 'Z'): ('A', 'B'),
            ('B', 'X'): ('B', 'A'),
            ('B', 'Y'): ('B', 'B'),
            ('B', 'Z'): ('B', 'C'),
            ('C', 'X'): ('C', 'B'),
            ('C', 'Y'): ('C', 'C'),
            ('C', 'Z'): ('C', 'A'),
            }

def score(strategy):
    if (translation[strategy[0]], translation[strategy[1]]) == ('Rock', 'Scissors'):
        res = 0
    elif (translation[strategy[0]], translation[strategy[1]]) == ('Rock', 'Paper'):
        res = 6
    elif (translation[strategy[0]], translation[strategy[1]]) == ('Paper', 'Scissors'):
        res = 6
    elif (translation[strategy[0]], translation[strategy[1]]) == ('Paper', 'Rock'):
        res = 0
    elif (translation[strategy[0]], translation[strategy[1]]) == ('Scissors', 'Rock'):
        res = 6
    elif (translation[strategy[0]], translation[strategy[1]]) == ('Scissors', 'Paper'):
        res = 0
    else:
        res = 3
    res += ['Rock', 'Paper', 'Scissors'].index(translation[strategy[1]])+1
    return res
    
def parse(filename):
    with open(filename) as file:
        strategies = [x.rstrip() for x in file.readlines()]
    return [tuple(x.split()) for x in strategies]

if __name__ == '__main__':
    strategies = parse('input')
    strategies_dec = [decoding[s] for s in strategies]

    print(f'The solution to part 1 is: {sum([score(x) for x in strategies])}')
    print(f'The solution to part 2 is: {sum([score(x) for x in strategies_dec])}')