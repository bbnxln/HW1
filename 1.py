import math

N = int(input("Введите N: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum(N):
    total = 0
    for num in range(2, N + 1):
        if is_prime(num):
            total += num
    return total

result = sum(N)
print(f"Сумма простых чисел в диапазоне от 2 до {N} включительно равна: {result}")