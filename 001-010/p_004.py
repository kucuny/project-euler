from math import sqrt


def get_largest_palindrome_product(input_number):
    maximum_number = input_number ** 2

    while maximum_number > 0:
        if is_palindrome(maximum_number):
            minimum_value, maximum_value = get_numbers(maximum_number)
            if (minimum_value and maximum_value
                and len(get_converted_string(input_number))
                    == len(get_converted_string(minimum_value))
                and len(get_converted_string(input_number))
                    == len(get_converted_string(maximum_value))):
                return maximum_number, minimum_value, maximum_value

        maximum_number -= 1


def is_palindrome(input_str):
    if not is_valid_input(input_str):
        return False

    input_str = get_converted_string(input_str)
    length_of_string = len(input_str)

    start_index, end_index = 0, length_of_string - 1

    if length_of_string is 1:
        return True

    while start_index < end_index:
        if start_index + 1 == end_index \
                and input_str[start_index] == input_str[end_index]:
            return True
        elif start_index == end_index:
            return True
        elif input_str[start_index] != input_str[end_index]:
            return False
        else:
            start_index += 1
            end_index -= 1

    return True


def is_valid_input(input_str):
    input_str = get_converted_string(input_str)

    if not input_str:
        return False

    if len(input_str) == 0:
        return False

    if len(input_str) == 1:
        return True

    return True


def get_converted_string(input_str):
    if isinstance(input_str, int):
        convert_str = str(input_str)
    else:
        convert_str = input_str

    return convert_str


def get_numbers(input_number):
    mid_value = int(sqrt(input_number))

    while mid_value <= input_number:
        result_value = float(input_number) / float(mid_value)
        if result_value == int(result_value):
            num_1 = int(input_number / result_value)
            num_2 = int(result_value)
            if num_1 > num_2:
                return num_2, num_1
            else:
                return num_1, num_2

        mid_value += 1

    return None, None
