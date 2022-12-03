
def compartify(content):
    size = len(content)//2
    return content[:size], content[size:]

def split_into_groups(rucksacks):
    return [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
 

def find_same_item(compartments):
    return list(set(compartments[0]).intersection(*[set(x) for x in compartments[1:]]))[0]
    

def priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38
    
def parse(filename):
    with open('input') as filename:
        rucksacks = [x.rstrip() for x in filename.readlines()]
    return rucksacks

if __name__ == '__main__':
    rucksacks = parse('input')
    rucksacks_compartified = [compartify for rucksack in rucksacks]
    groups = split_into_groups(rucksacks)

    print(f'The solution to part 1 is: {sum([priority(find_same_item(compartify(rucksack))) for rucksack in rucksacks])}')
    print(f'The solution to part 2 is: {sum([priority(find_same_item(group)) for group in groups])}')