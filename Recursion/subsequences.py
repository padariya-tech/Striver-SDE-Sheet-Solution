ans = []

def subsequences(i, temp, arr, n):

    if i >= n:
        # print(temp)
        ans.append(temp.copy())
        return

    # Take
    temp.append(arr[i])
    subsequences(i + 1, temp, arr, n)

    # Not take
    temp.pop()
    subsequences(i + 1, temp, arr, n)


arr = [3, 1, 2]

subsequences(0, [], arr, len(arr))

print(sorted(ans))
ans = []
str = "nij"
subsequences(0, [], str, len(arr))
print(sorted(ans))


## common pattern for this type of problem

# f(ind , [])
# {
#     if ind >= n :
#     print([])
#     return

#     [].add(arr[i])
#     f(ind+1,[])
#     [].remove(arr[i])
#     f(ind+1,[])
#     return
# }