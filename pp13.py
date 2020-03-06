print('Generate first n Fibonacci numbers')
print()
temp = int(input('Enter n: '))

def fibonacci_nums(num):
    if num == 1:
        return [1]
    if num == 0:
        return []
    Fibonacci = [1, 1]
    for _ in range(num - 2):
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
    return Fibonacci

print(fibonacci_nums(temp))








