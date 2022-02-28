
def read_display(file):
    test = [line.split('|') for line in open(file).read().splitlines()]
    keys = []
    numbers = []
    for jumble in test:
        keys.append(set(jumble[0].strip().split()))
        numbers.append(jumble[1].strip().split())
    return keys, numbers

def count_unique_digits(numbers):
    unique = 0
    for output in numbers:
        unique += sum([1 for num in output if len(num) in [2, 3, 4, 7]])
    return unique

def identify_simple(key):
    simple = [num for num in key if len(num) in [2, 3, 4, 7]]
    simple_sorted = sorted(simple, key=lambda x: len(x))
    key_dict = {}
    for i, num in enumerate([1, 7, 4, 8]):
        key_dict[num] = simple_sorted[i]
    key -= set(simple)
    return key_dict, key

def identify_on_len(key, key_dict, key_num, match, key_len, equal_len):
    length = len(key_dict[match]) if equal_len else len(key_dict[match]) - 1
    key_dict[key_num] = [num for num in key 
                        if len(num) == key_len
                        and len(set(key_dict[match]) & set(num)) == length][0]
    key -= set([key_dict[key_num]])
    return key_dict, key

def identify_two_five(key, key_dict):
    key_dict[2] = [num for num in key 
                   if len(num) == 5 
                   and len(set(key_dict[4]) & set(num)) == 2][0]
    key_dict[5] = [num for num in key 
                   if len(num) == 5 
                   and len(set(key_dict[4]) & set(num)) != 2][0]
    key -= set([key_dict[2], key_dict[5]])
    return key_dict, key

def crack_codes(keys, numbers):
    total = 0
    for i, key in enumerate(keys):
        key_dict, key = identify_simple(key)
        # Find first batch based on key length (3, 9, 5)
        for num in [[3, 7, 5, True], [9, 4, 6, True], [6, 1, 6, False]]:
            key_dict, key = identify_on_len(key, key_dict, *num)
        
        key_dict, key = identify_two_five(key, key_dict)
        key_dict[0] = [num for num in key][0]
        key_dict = {''.join(sorted(key)): str(num) for num, key in key_dict.items()}
    
        number = int(''.join(key_dict[''.join(sorted(digit))] for digit in numbers[i]))
        total += number
    return total

if __name__ == "__main__":
    file = 'Day 8.txt'
    keys, numbers = read_display(file)
    # print (count_unique_digits(numbers))
    print (crack_codes(keys, numbers))
