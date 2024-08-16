def check_primes_in_list(numbers):
    def is_prime(number):
        if number <= 1:
            return False
        for v in range(2, number):
            if number % v == 0:
                return False
        return True

    for number in numbers:
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

# Example list
a = [5, 21, 11, 7, 29, 39, 51, 57, 83, 81]

# Check primes in the list
check_primes_in_list(a)

