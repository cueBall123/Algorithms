__author__ = 'cue'

def findpivot(searchlist,low,high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((high + low)/2)

    if mid < high and searchlist[mid] > searchlist [mid+1]:
        return mid
    if mid > low and searchlist[mid] < searchlist[mid -1]:
        return  mid - 1

    if searchlist[low] >= searchlist[mid]:
        return findpivot(searchlist,low,mid - 1)
    else:
        return findpivot(searchlist,mid + 1 ,high)

if __name__ == '__main__':
    list1 = [ 1, 2, 3, 4, 5, 6, 7]
    print (findpivot(list1,0, len(list1) - 1))