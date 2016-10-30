def MaxMin(mylist):
    if max(mylist)==min(mylist):
        return len(mylist)
    else:
        return( max(mylist),min(mylist))


print MaxMin([3,3,3,3])

