def fibo(maximum):
    if maximum in [1, 2]:
        return maximum
    else:
        return fibo(maximum - 1) + fibo(maximum - 2)


def even_fibonacci_numbers(maximum):
    init_value = 1
    total = 0

    while (1):
        fibo_result = fibo(init_value)

        if fibo_result > maximum:
            return total

        if fibo_result % 2 == 0:
            total += fibo_result

        init_value += 1


print even_fibonacci_numbers(4000000)
