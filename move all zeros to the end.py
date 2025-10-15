def move_zeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i] !=0:
          arr[j]=arr[i]
          j +=1
    while j < len(arr):
        arr[j]=0
        j +=1
    return arr
arr=[0,1,0,3,12,0,5,0,6]
print("before:",[0,1,0,3,12,0,5,0,6])
print("after:",move_zeros(arr))