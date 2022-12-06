def find_marker(signal, length):
    i = 0
    c = True
    while c==True:
        c = len(set(signal[i:i+length])) != length
        i += 1
    return i + length - 1
def parse(filename):
    with open('input') as filename:
        signals = [x.rstrip() for x in filename.readlines()]    

    return signals

if __name__ == '__main__':
    signals = parse('input')
    print(f'The solution to part 1 is: {find_marker(signals[0], 4)}')
    print(f'The solution to part 2 is: {find_marker(signals[0], 14)}')