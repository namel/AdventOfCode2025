pos = 50
zero_pos = 0
zero_pass = 0
POS_RANGE = 100 

def rotate_dial(p, step):
    global zero_pass

    p2 = p + int(step[1:]) * (1 if step[0] == 'R' else -1)
    if p2 == 0:
        zero_pass += 1
    if p2 >= POS_RANGE:
        zero_pass += (p2 // POS_RANGE)
    if p2 < 0:
        zero_pass += abs(p2 // POS_RANGE)
        if p == 0:
            zero_pass -= 1
        if p2 % POS_RANGE == 0:
            zero_pass += 1
    return p2 % POS_RANGE

with open('./day1/input', 'r') as input:
    for s in input.readlines():
        pos = rotate_dial(pos, s)
        if pos == 0:
            zero_pos += 1

print(f'number of times at zero-pos = {zero_pos} and zero-passes = {zero_pass}') 