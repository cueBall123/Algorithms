__author__ = 'cue'

arr = [3,4,5,6,7]



def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary(arr,l,r,x):

    if r >= l:
        mid = int((l + r)/2)
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary(arr,l,mid-1,x)

        else:
            return binary(arr,mid+1,r,x)
    else:
        return -1

print (binary(arr,0,len(arr)-1,3))