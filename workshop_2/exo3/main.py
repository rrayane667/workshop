# coding=utf-8
from func import __calcul_volume_sphere
from monte_carlo import montecarl

def f(n):
    return __calcul_volume_sphere(montecarl(n), 2.2)
print(f(1000))