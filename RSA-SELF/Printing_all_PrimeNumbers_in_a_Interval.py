lower = 1000000100
upper = 10000000000

print("These are the primenumbers", lower, "and", upper, "are:")

for num in range(lower, upper + 1): 
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
        else:
            print(num)