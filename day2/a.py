sum_single_repeat, sum_multi_repeat = 0, 0

# return true if string "s" is a repeating sequence of a length "rep_len"
def does_repeat(s, rep_len):
    for pos in range(rep_len, len(s), rep_len):
        if s[0:rep_len] != s[pos:pos+rep_len]:
            return False
    return True

with open('day2/input', 'r') as input:
    ranges = [(p[0], p[1]) for p in (r.split('-') for r in  input.readlines()[0].split(','))]
    for r in ranges:
        for n in range(int(r[0]), int(r[1]) + 1):
            n_str = str(n)
            digits = len(n_str)

            # cycle over possible repeat-lengths
            for rep_size in range(digits//2, 0, -1):
                if digits % rep_size == 0 and does_repeat(n_str, rep_size):
                    sum_multi_repeat += n
                    if rep_size == digits//2:
                        sum_single_repeat += n
                    break

print(f'sum of numbers with repeating sequences in given ranges. single-repeat:{sum_single_repeat} multi-repeat:{sum_multi_repeat}')