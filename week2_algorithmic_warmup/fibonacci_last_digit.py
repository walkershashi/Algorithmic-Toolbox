# Uses python3
import sys
import math

def get_fibonacci_last_digit(n):
    fibo = [0, 1]

    for i in range(2, n+1):
        fibo_last = fibo[i-1]%10 + fibo[i-2]%10
        fibo.append(fibo_last%10)
    
    return fibo[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
