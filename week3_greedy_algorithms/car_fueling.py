# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    cnt = 0

    for i in range(len(stops)):
        if (i+1) < len(stops) and tank >= stops[i] and tank < stops[i+1]:
            cnt += 1
            tank += stops[i]
    if tank > distance:
        return 0
    if tank < distance:
        cnt += 1 
        return cnt

    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
