# challenge easy
# write a function named sum that gets a number n 
# and returns the sum of the numbers from 1 to n


def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)


print(sum(6))