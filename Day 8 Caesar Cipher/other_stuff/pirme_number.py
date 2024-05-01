def prime_checker(number):
    is_prime = True

    for digit in range(2, number):
        if number % digit == 0:
            is_prime = False
    print(is_prime)


n = int(input())
prime_checker(number=n)