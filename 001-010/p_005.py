def get_smallest_multiple(maximum_value):
    target_value = [x + 1 for x in range(1, maximum_value)]
    lcm = 2

    for num in target_value:
        lcm = get_lcm(lcm, num)

    return lcm


def get_gcd(num_1, num_2):
    while num_2:
        x = num_1 % num_2
        num_1 = num_2
        num_2 = x

    return num_1


def get_lcm(num_1, num_2):
    gcd = get_gcd(num_1, num_2)
    return (num_1 * num_2) / gcd
