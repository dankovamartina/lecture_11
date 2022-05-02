
def recursive_nth_fibo(n):
    """
    :param n: n-ty prvek fbonacciho posloupnosti
    :return:
    """
    fibo = 0
    if n == 0:
        fibo = 0
    elif n == 1:
        fibo = 1
    else:
        fibo = recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)
    return fibo



def main():
    number = int(input("Zadejte prosim poradi prvku Fibonacciho posloupnosti, ktery chcete znat"))
    print(recursive_nth_fibo(number))
    end = int(input("Zadejte mnoztvi prvku, ktere chcete vypsat"))
    sequence = []
    for i in range (end):
        sequence.append(recursive_nth_fibo(i))
    print(sequence)


if __name__ == "__main__":
    main()
