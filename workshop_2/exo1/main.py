# coding=utf-8

# Exercice 1.1
def sep(s):
    return tuple(s.split())

# Exercice 1.2
def mdp(m):
    up = False
    low = False
    spe = False
    for i in m:
        if i.isupper():up = True
        if i.islower():low=True
        for j in "!@#$%^&*":
            if j==i: spe = True
    if len(m)>=8 and up and low and spe: return True
    return False

# Exercice 1.3
def remp(s,r1,r2):
    l = list(s.split(r1))
    return r2.join(l)
# Exercice 1.4

def freq(s):
    return{ chr(i):s.count(chr(i)) for i in range(ord("a"), ord("z")+1) if s.count(chr(i))!=0}

# Exercice 1.5
def acr(s):
    return "".join(list(map(lambda x : x[0], list(s.split()))))

# Exercice 1.6
def class_sent(c, p, n):
    l = [i.lower().replace("'", " ").replace(".", " ").split() for i in c]
    f = lambda x : "positif" if set(x).intersection(set(p)) else ("negatif" if set(x).intersection(set(n)) else "neutre")
    return [ f(i) for i in l ]

# Exercice 2.1
def occur(s):
    return {i:s.count(i) for i in set(s.split())}

# Exercice 2.2
def fusion(a, b):
    return { i:a[i] for i in a if not (i in b)}.update({ i:a[i] + b[i] for i in a if i in b}).update({ i:b[i] for i in a if not (i in a)})

# Exercice 2.3
def imb(d):
    return [(i,d[i]) if type(d[i])!= dict else (i,imb(d[i])) for i in d  ]


# Exercice 2.4
def fus_imb(a, b):
    return { i:a[i] for i in a if not (i in b)}.update({ i:a[i] + b[i] for i in a if (type(a[i])!=dict and i in b)}).update({ i:b[i] for i in a if not (i in a)}).update({ i:a[i].update(b[i]) for i in a if (i in b and type(i)==dict)})
print(fus_imb({'a': 1, 'b': {'c': 2, 'd': 3}}, {'b': {'e': 4, 'f': {'g': 5, 'h': 6}}, 'i': 7}))

# Exercice 2.5
def srt(d):
    l = sorted(imb(d), key = lambda x : x[1])
    for i in l:
        l[i[0]] = i[1]
