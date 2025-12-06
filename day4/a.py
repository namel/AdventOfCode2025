adjacent_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# check if there is a roll of paper at position
def is_roll(map, row, col):
    return 0 <= row < len(map) and 0 <= col < len(map[0]) and map[row][col] == '@' 

# count number of adjacent rolls of paper at position
def get_adjacent_count(map, row, col):
    return sum([is_roll(map, row + dy, col + dx) for dy, dx in adjacent_positions])
    
# part 1
with open('day4/input', 'r') as input:
    map = input.readlines()

    accessible = 0
    for row, col in [(r,c) for c in range(0, len(map[0])) for r in range(0, len(map))]:
        if is_roll(map, row, col) and get_adjacent_count(map, row, col) < 4:
            accessible += 1

    print(f'accessible rolls of paper {accessible}')


# scan area around a given point, and gradually remove rolls of paper
def remove_area(map, row, col):
    if not is_roll(map, row, col) or get_adjacent_count(map, row, col) >= 4:
        return 0
    
    map[row][col] = '.'
    return sum([remove_area(map, row + dy, row + dx) for dy, dx in adjacent_positions]) + 1

# part 2
with open('day4/input', 'r') as input:
    map = [list(l.strip()) for l in input.readlines()]

    removed = []
    while len(removed) == 0 or removed[-1] > 0:
        removed.append(0)
        for row, col in [(r,c) for c in range(0, len(map[0])) for r in range(0, len(map))]:
           removed[-1] += remove_area(map,row, col)
        print(f'removed {removed[-1]}')

    print(f'recursively removed {sum(removed)} rolls of paper ')


    