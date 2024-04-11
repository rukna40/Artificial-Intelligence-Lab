import random

def calc(x):
    # return -x**2 + 5*x + 10
    return x**3-4*x**2+3*x+1

def hc(type):
    curr = random.uniform(-10, 10)
    step = 0.1
    iters = 1000
    for i in range(iters):
        next_pos = curr + random.choice([-step, step])
        if next_pos < -10:
            next_pos = -10
        elif next_pos > 10:
            next_pos = 10
        if type=='max':
            if calc(next_pos) > calc(curr):
                curr = next_pos
                curr_cost=calc(next_pos)
        elif type=='min':
            if calc(next_pos) < calc(curr):
                curr = next_pos
                curr_cost=calc(next_pos)
    return curr,curr_cost

x,cost=hc('min')
print("X = ",x)
print("Value at X = ",cost)
