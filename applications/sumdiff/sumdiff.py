"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

from itertools import combinations_with_replacement

def f(x):
    
    result = []
    




    for c in x:
        c = (c*4) + 6
        result.append(c)
    n = 2
    

    result2 = (set(sum(comb) for comb in combinations_with_replacement(result, n)))
    result3 = (set(-sum(comb) for comb in combinations_with_replacement(result, n)))



    return result3        

    

q = (1, 3, 4, 7, 12)
print(f(q))       

# Your code here

