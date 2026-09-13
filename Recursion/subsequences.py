# ans = []

# def subsequences(i, temp, arr, n):

#     if i >= n:
#         # print(temp)
#         ans.append(temp.copy())
#         return

#     # Take
#     temp.append(arr[i])
#     subsequences(i + 1, temp, arr, n)

#     # Not take
#     temp.pop()
#     subsequences(i + 1, temp, arr, n)


# arr = [3, 1, 2]

# subsequences(0, [], arr, len(arr))

# print(sorted(ans))
# ans = []
# str = "nij"
# subsequences(0, [], str, len(arr))
# print(sorted(ans))


def subsequences(start, temp, arr):

    # Every point is a valid subsequence
    # if start == len(arr):
    #     print(temp)
    #     return
    print(temp)

    for i in range(start, len(arr)):

        # TAKE
        temp.append(arr[i])

        # Move forward
        subsequences(i + 1, temp, arr)

        # UNDO TAKE
        temp.pop()


arr = [1, 2, 3]

subsequences(0, [], arr)