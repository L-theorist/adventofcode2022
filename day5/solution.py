
def parse(filename):
    with open('input') as filename:
        stacks_raw = [x.rstrip() for x in filename.readlines()]
    
    stacks, procedures = stacks_raw[:stacks_raw.index('')], stacks_raw[stacks_raw.index('')+1:]
    return stacks, procedures

def decode_proc(procs):
    procedures_dec = [tuple([int(x) for x in proc.split(' ')[1::2]]) for proc in procs]
    return procedures_dec

def initiate_containers(stacks):
    nu_stacks = (len(stacks[-1]) + 2)//4
    containers = [[] for i in range(nu_stacks)]
    for stack in stacks[:-1][::-1]:
        for i, j in enumerate(range(1, len(stack), 4)):
            if stack[j] != ' ':
                containers[i].append(stack[j])
    return containers

def rearrange(containers, procedures_dec, crane_type='CrateMover 9001'):
    for x in procedures_dec:
        nu_containers, source_id, target_id = x[0], x[1] - 1, x[2] - 1
        if crane_type=='CrateMover 9001':
            containers[target_id] += containers[source_id][-nu_containers:][::-1]
        elif crane_type=='CrateMover 9000':
            containers[target_id] += containers[source_id][-nu_containers:]
        containers[source_id] = containers[source_id][:-nu_containers]
    
    return containers

def unload(containers):
    return ''.join([stack[-1] for stack in containers])


    

if __name__ == '__main__':
    stacks, procedures = parse('input')
    
    containers = initiate_containers(stacks)
    print(f"The solution to part 1 is: {unload(rearrange(containers, decode_proc(procedures)))}")
    containers = initiate_containers(stacks)
    print(f"The solution to part 2 is: {unload(rearrange(containers, decode_proc(procedures), crane_type='CrateMover 9000'))}")