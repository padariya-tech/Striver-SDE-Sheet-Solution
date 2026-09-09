n = 10

sum = 0
i = 0
def reverse_array(arr,i,j):
    
    if i > j:
        return arr
    
    arr[i],arr[j] = arr[j],arr[i]
    return reverse_array(arr,i+1,j-1)


arr = [1,2,3,4,5,6,7,8,9]
print(reverse_array(arr, 0, len(arr)-1))