import numpy as np


def parse(filename):
    with open(filename) as file:
        calories = [x.rstrip() for x in file.readlines()]
        
    def _split(flat_list):
        sublist = []
        for cals in flat_list:
            if cals == '':
                yield [int(cals) for cals in sublist]
                sublist = []
            else:
                sublist.append(cals)
        yield [int(cals) for cals in sublist]
    
    return [cals for cals in _split(calories)] 




def solution(elves, top=1):
    return sum(sorted([sum(x) for x in elves], reverse=True)[:top])

if __name__ == '__main__':
    elves = parse('input')
    print(f'The solution to part 1 is: {solution(elves)}')
    print(f'The solution to part 2 is: {solution(elves, 3)}')