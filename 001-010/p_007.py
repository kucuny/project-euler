def is_prime_number(input_number):
    init_value = 2

    if input_number == init_value:
        return True

    while init_value < input_number:
        mod_result = input_number % init_value

        if mod_result == 0:
            return False

        init_value += 1

    return True


def get_xst_prime_number(maximum):
    init_value = 1
    prime_count = 0

    while prime_count < maximum:

        init_value += 1

        if is_prime_number(init_value):
            prime_count += 1

    print prime_count, init_value
    return init_value
