def fibs(n):

    if n < 0:
        raise ValueError("n должно быть неотрицательным числом")
    elif n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]

    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence


if __name__ == "__main__":
    n = int(input("Введите кол-во чисел "))
    print(fibs(n))