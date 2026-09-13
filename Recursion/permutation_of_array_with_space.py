class Solution:
    def permutation(self,temp,arr,ans,used):
        if len(temp) == len(arr):
            ans.append(temp.copy())
            return
        
        for j in range(len(arr)):
            if used[j]:
                continue
            
            used[j] = True
            temp.append(arr[j])

            self.permutation(temp,arr,ans,used)
            
            used[j] = False
            temp.pop()

        return

if __name__ == "__main__":

    ans = []
    arr = [1,3,2]
    sol = Solution()
    used = [0] * len(arr)
    # for i in range(len(arr)):
    sol.permutation([],arr,ans,used)
    # ans = sorted(ans)
    print(ans)
