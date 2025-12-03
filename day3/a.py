def scan_level(bank, digits, positions, level, start):

    # choose only those positions which have the highest digit, and still have room to build a number
    first = start
    last = len(bank) - digits + level
    next_digit = max(bank[first:last+1])
    candidates = [i for i in range(first, last+1) if bank[i] == next_digit]

    if level == digits - 1:
        return str(next_digit)

    best = '0'
    for i in candidates:
        positions[level] = i
        scanned = scan_level(bank, digits, positions, level + 1, i+1)
        if scanned > best:
            best = scanned

    return str(next_digit) + best

with open('day3/input', 'r') as input:

    banks = [[int(c) for c in l.strip()] for l in input.readlines()]
    hi_list_2, hi_list_12 = [], []
    for bank in banks:
        hi_list_2.append(int(scan_level(bank, 2, [0] * 2, 0, 0)))
        hi_list_12.append(int(scan_level(bank, 12, [0] * 12, 0, 0)))

    print(f'the sum of the highest digit selection is 2-sequence: {sum(hi_list_2)} 12-sequence: {sum(hi_list_12)}')
            