# Uses python3
def calc_fib(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    print(fibo)
    return fibo[n]

n = int(input())
print(calc_fib(n))
