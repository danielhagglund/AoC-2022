def create_stacks(input):
    stacks_data = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    for line in input:
        if line[1] != '1' :
            if line[1] != ' ':
                stacks_data[1].append(line[1])
            if line[5] != ' ':
                stacks_data[2].append(line[5])
            if line[9] != ' ':
                stacks_data[3].append(line[9])
            if line[13] != ' ':
                stacks_data[4].append(line[13])
            if line[17] != ' ':
                stacks_data[5].append(line[17])
            if line[21] != ' ':
                stacks_data[6].append(line[21])
            if line[25] != ' ':
                stacks_data[7].append(line[25])
            if line[29] != ' ':
                stacks_data[8].append(line[29])
            if line[33] != ' ':
                stacks_data[9].append(line[33])
        else:
            break

        i = 1

    #reverse_stack
    while i <= 9:
        stacks_data[i].reverse()
        i = i+1

    return stacks_data

def move_crates(input, stacks_data):
    for line in input_data:
        if line.startswith("move"):
            move_instructions = line.rsplit(' ')
            quantity = int(move_instructions[1])
            from_stack = int(move_instructions[3])
            to_stack = int (move_instructions[5])
            if quantity>0:
                crate_stack = []
                for i in range(1,quantity+1):
                    crate_stack.append(stacks_data[from_stack].pop())
                for i in range(1,quantity+1):
                    stacks_data[to_stack].append(crate_stack.pop())

    return stacks_data

input_data = open("./input.txt", encoding="utf8").read().splitlines()

stacks = create_stacks(input_data)
stacks = move_crates(input_data, stacks)

top_crates = []
for i in range(1,10):
    top_crates.append(stacks[i][len(stacks[i])-1])

print(''.join(top_crates))