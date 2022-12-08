import time
from RSA_CrackingPrivatekey_helper import n 
# Prompt the user to enter a number to factorize
# n = int(input("Enter a number to factorize: "))

t0 = time.monotonic_ns()
# Initialize a list to store the factors
factors = []

# Try all numbers from 2 to the square root of n as a potential prime factor
for i in range(2, int(n ** 0.5) + 1):
  # If the number is a factor of n, add it to the list of factors
  if n % i == 0:
    factors.append(i)
    # Divide n by the factor and try to factorize the result
    n = n // i

# If there are no factors found, the number is prime
if len(factors) == 0:
  print(f"{n} is a prime number.")
else:
  # Print the list of prime factors
  print(f"The prime factors of {n} are: {factors}")
  t1 = time.monotonic_ns()
  print(f'{(t1-t0)/1000000000:.5f} seconds')