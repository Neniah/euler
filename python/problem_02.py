def Fibonacci(n):
    if n == 2 or n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


suma = 0
fibo = 0

for i in range(0, 4000000):
    fibo = Fibonacci(i)
    if fibo % 2 == 0:
        suma += fibo
    print(suma)
