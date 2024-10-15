import itertools
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    digits = list(numbers)
    possible_numbers = set()
    
    for length in range(1, len(digits) + 1):
        permutations = itertools.permutations(digits, length)
        for p in permutations:
            num = int(''.join(p))
            possible_numbers.add(num)
    
    count = 0
    for num in possible_numbers:
        if is_prime(num):
            count += 1
    return count
