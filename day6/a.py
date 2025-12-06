
operation_map = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

# 64
# 23 
# 314
# -> 4 + 431 + 623
def yield_args(problem):
    width = max([len(a) for a in problem])
    padded_args = [a + ' ' * (width - len(a)) for a in problem]
    for w in range(width):
        new_arg = ''.join([d[w] for d in padded_args])
        yield int(new_arg.strip())

with open('day6/input', 'r') as input:
    lines = [l.strip().split() for l in input.readlines()]
    problems = [[lines[row][col] for row in range(len(lines)) ] for col in range(len(lines[0]))]

    total = 0

    for p in problems:
        result = int(p[0])
        operation = operation_map[p[-1]]
        for arg in p[1:-1]:
            result = operation(result, int(arg))
        total += result

    print(f'total of the results of the operations is {total}')

    total = 0
    for p in problems:
        args = list(yield_args(p[:-1]))
        result = args[0]
        operation = operation_map[p[-1]]
        for arg in args:
            result = operation(result, arg)
        total += result        

    print(f'total of the results of the vertically-parsed operations is {total}')
