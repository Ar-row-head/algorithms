import sys
s1 = [2,-5,3,1,-4,0,-10,2,8,-2]


def max_product_subarray_bf(x, m):
    max_prod = 0
    prod = -sys.maxsize
    for i in range(m):
        prod = x[i]
        if max_prod < prod:
            max_prod = prod
        for j in range(i+1,m):
            prod *=x[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod

print(max_product_subarray_bf(s1,len(s1)))

def max_product_subarray_dp(x, m):
    max_prod = x[0]
    min_val = x[0]
    max_val = x[0]
    for i in range(1, m):
        current = x[i]
        max_val = max(current*min_val, current*max_val, current)
        min_val = min(current*min_val, current*max_val, current)
        if(max_prod < max_val):
            max_prod = max_val
    return max_prod

print(max_product_subarray_dp(s1, len(s1)))