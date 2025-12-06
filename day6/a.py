import functools

apply_operation = {
    '+': lambda args: functools.reduce(lambda x, y: x + y, args, 0),
    '*': lambda args: functools.reduce(lambda x, y: x * y, args, 1),
}

with open('day6/input', 'r') as input:
    lines = [l.rstrip() for l in input.readlines()]
    prob_lines = [l.strip().split() for l in lines]
    problems = [[prob_lines[row][col] for row in range(len(prob_lines)) ] for col in range(len(prob_lines[0]))]

    total = 0
    for p in problems:
        total += apply_operation[p[-1]]([int(a) for a in p[:-1]])
    print(f'total of the results of the operations is {total}')

    # find the starting offset for each problem
    offsets = [pos+1 for pos in range(len(lines[0])) if all([lines[c][pos] == ' ' for c in range(len(lines) - 1)])]
    offsets = [0] + offsets + [len(lines[0]) + 1]
    
    total = 0        
    for o in range(len(offsets) - 1):
        start, end = offsets[o], offsets[o+1]
        args = [int(''.join([lines[h][start + w] for h in range(len(lines) - 1)]).strip()) for w in range(end - start - 1)]
        total += apply_operation[prob_lines[-1][o]](args)

    print(f'total of the results of the vertically-parsed operations is {total}')
