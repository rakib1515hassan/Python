class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
        

# Creating an instance of Calculator
calc = Calculator()

# Calling add method with different numbers of arguments
print(calc.add(5))        # Output: 5 (uses default b=0, c=0)
print(calc.add(5, 10))    # Output: 15 (uses default c=0)
print(calc.add(5, 10, 15)) # Output: 30 (all arguments provided)





class Calculator:
    def add(self, *args):
        return sum(args)

# Creating an instance of Calculator
calc = Calculator()

# Calling add method with varying numbers of arguments
print(calc.add(5))             # Output: 5
print(calc.add(5, 10))         # Output: 15
print(calc.add(5, 10, 15))     # Output: 30
print(calc.add(5, 10, 15, 20)) # Output: 50
