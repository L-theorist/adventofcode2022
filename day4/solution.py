def fully_contained(pair):
    return pair[1].intersection(pair[0]) == pair[1] or pair[0].intersection(pair[1]) == pair[0]
    
def overlap(pair):
    return pair[1].intersection(pair[0]) != set()

def parse(filename):
    with open('input') as filename:
        pair_assignments = [x.rstrip() for x in filename.readlines()]
        assignment_pairs = [x.split(',') for x in pair_assignments]
        assignment_pairs = [[tuple(y[0].split('-')), tuple(y[1].split('-'))] for y in assignment_pairs]
        assignment_pairs = [[set(range(int(x[0][0]), int(x[0][1])+1, 1)), set(range(int(x[1][0]), int(x[1][1])+1, 1))] for x in assignment_pairs]
        return assignment_pairs

    

if __name__ == '__main__':
    assignment_pairs = parse('input')
    

    print(f'The solution to part 1 is: {sum([fully_contained(pair) for pair in assignment_pairs])}')
    print(f'The solution to part 2 is: {sum([overlap(pair) for pair in assignment_pairs])}')