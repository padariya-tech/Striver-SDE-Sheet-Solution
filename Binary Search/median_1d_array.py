

nums = [1,2,3,4,5]

#. ( number of element <= x ) >= (n//2)

def median(nums):

    n = len(nums)
    k = (n+1)//2
    for x in nums:

        cnt = 0

        for num in nums:
            if num <= x:
                cnt += 1

        if cnt >= k:
            return x
        
print(median(nums))
