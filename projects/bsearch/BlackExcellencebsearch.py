Bsearch

# Justin Austin

def binary_search(a, x, small=0, big=None):
    if big is None:
        big = len(a)
    while small < big:
        mid = (small+big)//2
        midval = a[mid]
        if midval < x:
            small = mid+1
        elif midval > x: 
            big = mid
        else:
            return mid
    return -1
    
    
    
    
