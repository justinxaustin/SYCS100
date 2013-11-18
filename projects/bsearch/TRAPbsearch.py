#Justin Austin 
#Malik Hornbuckle
#Jacari Boboye


rList = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]


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

print binary_search(rList, 2, small = 0, big = 10)
