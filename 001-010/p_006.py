def get_sum_of_the_squares(maximum):
    init_value = [(x + 1) ** 2 for x in range(maximum)]
    return sum(init_value)


def get_squares_of_the_sum(maximum):
    init_value = [x + 1 for x in range(maximum)]
    return sum(init_value) ** 2


def get_sum_square_difference(maximum):
    sum_of_the_squares = get_sum_of_the_squares(maximum)
    squares_of_the_sum = get_squares_of_the_sum(maximum)

    return squares_of_the_sum - sum_of_the_squares
