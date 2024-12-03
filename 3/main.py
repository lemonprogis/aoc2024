import regex


def extract_muls(e, s):
    return regex.findall(e, s)

def extract_nums(s):
    expression = r"\d+"
    return [ int(d) for d in regex.findall(expression, s)]

def multiply_num(l):
    return l[0] * l[1]

def process_data(e, s):
    muls = extract_muls(e, s)
    nums = [extract_nums(n) for n in muls]
    multiplied_nums = [multiply_num(l) for l in nums]
    print(multiplied_nums)
    return sum(multiplied_nums)

def test():
    test_str = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    expression = r"mul\(\d+\,\d+\)"
    total = process_data(expression, test_str)
    print(total == 161)

    test_str_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expression2 = r"mul\(\d+\,\d+\)"
    total2 = process_data(expression2, test_str_2)
    print(total2 == 48)

def main():
    with open("3/input.txt", 'r') as f:
        readings = f.readlines()
        print(readings)
        total = process_data(str(readings))
        print("Total: ", total)

test()

# main()