import random, math

def montecarl(n):
    l1 = [[random.random(), random.random()] for _ in range(n)]
    l2 = [ l1[i] for i in range(n) if math.sqrt(l1[i][0]**2 + l1[i][1]**2)<=1]
    return 4*len(l2)/n