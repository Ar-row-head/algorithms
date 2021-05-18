import random

x = [1, 6, 11, 5, 7]
lx = len(x)

def min_subset_rec(s1, i, calc_sum, tot_sum):
    if i==0:
        return abs(tot_sum - 2*calc_sum)
    return min(min_subset_rec(s1, i-1, calc_sum+s1[i-1], tot_sum), min_subset_rec(s1, i-1, calc_sum, tot_sum))


def min_subset_diff_brute_force(s1, m):
    tot_sum = sum(s1)
    return min_subset_rec(s1,m-1,0,tot_sum)

print(min_subset_diff_brute_force(x, lx))

print(random.randint(1,10))