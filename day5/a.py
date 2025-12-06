

def merge_range(ranges, new_r):

    if len(ranges) == 0:
        ranges.append(new_r)
        return
    
    for r in ranges[:]:
        if r[1] < new_r[0] or r[0] > new_r[1]:
            continue
        if r[0] >= new_r[0] and r[1] <= new_r[1]:
            ranges.remove(r)
            continue
        if r[0] <= new_r[0] and r[1] >= new_r[1]:
            return
        if r[0] < new_r[0]:
            ranges.remove(r)
            new_r = (r[0], new_r[1])
        if r[1] > new_r[1]:
            ranges.remove(r)
            new_r = (new_r[0], r[1])

    ranges.append(new_r)


with open('day5/input', 'r') as input:
    lines = [l.strip() for l in input.readlines()]
    ranges = [(int(l.split('-')[0]), int(l.split('-')[1])) for l in lines if l.find('-') >= 0]
    nums = [int(l) for l in lines if l.isnumeric()]

    fresh = 0
    for n in nums:
        for r in ranges:
            if r[0] <= n <= r[1]:
                fresh += 1
                break

    print(f'number of fresh items {fresh}')

    merged_ranges = []
    for r in ranges:
        merge_range(merged_ranges, r)

    print(f'total number of possible fresh items {sum([r[1] - r[0] + 1 for r in merged_ranges])}')
