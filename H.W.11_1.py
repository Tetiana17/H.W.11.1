def is_prime(num):
    """
    Перевіряє, чи є число простим

    :num: Число для перевірки
    :return: True, якщо число просте, інакше False
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_generator(end):
    """
    Генератор простих чисел до верхньої межі (включно)

    :yield: Просте число
    """
    for num in range(2, end + 1):
        if is_prime(num):
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, "Test0"
assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"
print("Ok")