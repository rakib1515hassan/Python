"""
##!   Python Program to Check Prime Number

NOTE:- # Negative numbers, 0 and 1 are not primes
"""

##? Example 1:-
number = int(input("Enter a number :"))

if number > 1:
    for v in range(2, number):
        if (number%v) == 0:
            print(number, "is not a prime number")
            break
    
    else:
        print(number, "is a prime number.")

else:
    print(number, "is not a prime number")



##? Example 2:-
num = 11

if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



##? Example 3:-
"""
    > The loop condition i * i <= n ensures that the function only checks potential factors up to the square root of n. This makes the algorithm more efficient by reducing the number of checks needed. The checks are based on the mathematical property that if n has a factor greater than its square root, it must also have a corresponding factor smaller than or equal to the square root.
"""
import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(11))  # True
print(is_prime(1))   # False


"""
Let's use an example to illustrate how the loop condition works. Suppose n = 29.

Initial Values:

Start with i = 2.
Compute i * i = 2 * 2 = 4.
Check if 4 <= 29. Since this is true, the loop continues.
First Iteration:

Check if 29 % 2 == 0. It is not (29 is not divisible by 2), so increment i to 3.
Second Iteration:

Compute i * i = 3 * 3 = 9.
Check if 9 <= 29. Since this is true, the loop continues.
Check Divisibility:

Check if 29 % 3 == 0. It is not (29 is not divisible by 3), so increment i to 4.
Third Iteration:

Compute i * i = 4 * 4 = 16.
Check if 16 <= 29. Since this is true, the loop continues.
Check Divisibility:

Check if 29 % 4 == 0. It is not (29 is not divisible by 4), so increment i to 5.
Fourth Iteration:

Compute i * i = 5 * 5 = 25.
Check if 25 <= 29. Since this is true, the loop continues.
Check Divisibility:

Check if 29 % 5 == 0. It is not (29 is not divisible by 5), so increment i to 6.
Fifth Iteration:

Compute i * i = 6 * 6 = 36.
Check if 36 <= 29. Since this is false, the loop terminates.
At this point, since no divisors were found up to sqrt(29), we conclude that 29 is a prime number.
"""




##? Example 4:-
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



##? Example 5:-
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes_in_list(numbers):
    for number in numbers:
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

# Example list
a = [5, 21, 11, 7, 29, 39, 51, 57, 83, 81]

# Check primes in the list
check_primes_in_list(a)
