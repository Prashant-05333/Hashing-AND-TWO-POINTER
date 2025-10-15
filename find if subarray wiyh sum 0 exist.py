def has_pair_wiyh__sum(num,target):
    seen=set()
    for num in nums:
        if  target -num in seen:
            return False
    else:
        seen.add(num)
        return False
nums=[4,4,5,6,7,8,1,2,3,5]
target=8
print(has_pair_wiyh__sum(nums,target))