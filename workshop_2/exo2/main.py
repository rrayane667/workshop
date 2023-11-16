import random
def al(a, b):
    n = random.randint(a, b)
    m = int(input("devinez le nombre\n")
    while n !=m:
        if n<m : print("nombre généré est inferieur\n")
        else : print("nombre généré est supérieur\n")
        m=int(input("devinez le nombre\n"))