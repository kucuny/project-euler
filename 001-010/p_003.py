def largest_prime_factor(maximum):
    init_value = 2
    while True:
        if init_value == maximum:
            return init_value

        if maximum % init_value == 0:
            maximum /= init_value

        init_value += 1
