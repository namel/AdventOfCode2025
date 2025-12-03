def scan_level(bank, digits, level, start):

    last = len(bank) - digits + level
    next_digit = max(bank[start:last+1])

    if level == digits - 1:
        return str(next_digit)

    # choose only those positions which have the highest digit, and still have room to build a number
    candidates = [i for i in range(start, last+1) if bank[i] == next_digit]
    best = max([scan_level(bank, digits, level + 1, i+1) for i in candidates])
    return str(next_digit) + best

with open('day3/input', 'r') as input:

    banks = [[int(c) for c in l.strip()] for l in input.readlines()]
    hi_list_2, hi_list_12 = [], []
    for bank in banks:
        hi_list_2.append(int(scan_level(bank, 2, 0, 0)))
        hi_list_12.append(int(scan_level(bank, 12, 0, 0)))

    print(f'the sum of the highest digit selection is 2-sequence: {sum(hi_list_2)} 12-sequence: {sum(hi_list_12)}')
            