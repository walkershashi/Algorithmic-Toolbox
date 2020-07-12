# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    val_per_wt = []
    for i in range(len(weights)):
        val_per_wt.append(values[i] / weights[i])
    
    value = 0
    for i in range(len(weights)):
        if capacity == 0:
            return value
    
        max_index = val_per_wt.index(max(val_per_wt))
        taken_amt = min(weights[max_index], capacity)

        value += taken_amt * max(val_per_wt)
        weights[max_index] -= taken_amt

        if weights[max_index] == 0:
            val_per_wt[max_index] = 0
        else:
            val_per_wt[max_index] -= weights[max_index]
        
        capacity -= taken_amt
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
