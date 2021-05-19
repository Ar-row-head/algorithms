s1 = [4,5,6,7,-1,0,1,2]
m = len(s1)

def min_rotated_sorted_array_bf(x, m):
    min = x[0]
    for i in range(1,m):
        if min > x[i]:
            min = x[i]
    return min

print(min_rotated_sorted_array_bf(s1, m))

def min_rotated_sorted_array_bs(x,m):
    low = 0
    high = m-1
    mid = int((low+high+1)/2)
    while low < high:
        if(x[low] < x[high]):
            return x[low]
        if(x[mid] < x[high]):
            high = mid
        else:
            low = mid
        mid = int((low+high+1)/2)
    return x[low]

print(min_rotated_sorted_array_bs(s1, m))

