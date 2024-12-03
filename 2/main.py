def validate_nums(nums):
    if not nums or len(nums) == 1:
        return True

def within_3(nums):
    validate_nums(nums)
    return all(abs(nums[i + 1] - nums[i]) <= 3 for i in range(len(nums) - 1))

def within_3_dampener(nums):
    validate_nums(nums)
    breaks = 0
    for i in range(len(nums) - 1):
        if abs(nums[i + 1] - nums[i]) > 3:
            breaks += 1
            if breaks > 1:  # Allow at most one break
                return False
    return True

def is_increasing_or_decreasing(nums):
    validate_nums(nums)
    is_increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    is_decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))
    return is_increasing or is_decreasing


def is_increasing_or_decreasing_and_within_3(nums):
    return is_increasing_or_decreasing(nums) and within_3(nums)

def test():
    readings = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    is_good = 0
    dampened_is_good = 0
    for reading in readings:
        if is_increasing_or_decreasing_and_within_3(reading):
            is_good += 1
    
    print(is_good == 2)
    print(dampened_is_good == 4)


def main():
    with open("2/input.txt", 'r') as f:
        readings = f.readlines()
        is_good = 0
        for r in readings:
            reading = [ int(i) for i in r.strip('\n').split(' ')]
            if is_increasing_or_decreasing_and_within_3(reading):
                is_good += 1
            

    print("Safe Reports: ", is_good)

main()