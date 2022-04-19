import math


def nCr(n, r):
    factorial_ = math.factorial
    return factorial_(n) / (factorial_(r)*factorial_(n-r))


def prob(k, N):
    prob_AaBb = 0.25
    prob = []
    total = 2 ** k

    for r in range(N, (total+1)):
        prob.append(nCr(total, r) *(prob_AaBb ** r)*((1-prob_AaBb)**(total-r)))
    return sum(prob)


print("%.3f" % prob(2, 1))