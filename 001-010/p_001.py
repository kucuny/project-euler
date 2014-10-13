def multiples_3_or_5(maximum):
    return sum([x for x in range(1, maximum) if x % 3 == 0 or x % 5 == 0])

print multiples_3_or_5(1000)
