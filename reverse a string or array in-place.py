def array_reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
num=[2,4,3,2,3,45,6,7,8]
print("reverse array:",array_reverse(num))