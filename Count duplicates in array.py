def find_duplicates(nums):
    seen=set()
    duplicates=set()
    for num in nums:
       if num in seen:
         duplicates.add(num)
       else:
         seen.add(num)
    return list(duplicates)
nums=[1,5,3,2,3,5,1,6,2,3]
print(find_duplicates(nums))  