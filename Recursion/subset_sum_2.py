class Solution:
    def subset_sum(self,i,temp,arr,ans):
        # if i == len(arr):
        ans.append(temp.copy())
            # return

        start = i
        for j in range(i,len(arr)):
            
            if j > i and arr[j-1] == arr[j]:
                continue

            temp.append(arr[j])
            self.subset_sum(j+1,temp,arr,ans)
            temp.pop()

        return

if __name__ == "__main__":

    ans = []
    arr = [4,4,4,1,4]
    sol = Solution()
    arr = sorted(arr)
    sol.subset_sum(0,[],arr,ans)
    ans = sorted(ans)
    print(ans)
