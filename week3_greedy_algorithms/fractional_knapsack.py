# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    for i in range(len(weights)):
        if capacity == 0:
            return value
        val_per_wt = [values[i] / weights[i] for i in range(len(weights)) if weights[i] != 0]
        max_val_wt = 0
        index = 0
        for i in range(len(val_per_wt)):
            if val_per_wt[i] > max_val_wt:
                max_val_wt = val_per_wt[i]
                index = i
        if weights[index] > 0 : 
                min_ = min(weights[index], capacity)
                value += max_val_wt * min_
                weights[i] -= min_
                capacity -= min_
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
