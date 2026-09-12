class Solution:
    def combination_sum(self,i,temp,curr_sum,arr,k,ans):
        if curr_sum > k:
            return
        if i == len(arr):
            if curr_sum == k:
                ans.append(temp.copy())
                return
            else:
                return
            
        # take same element on the same index
        temp.append(arr[i])
        a = self.combination_sum(i,temp,curr_sum+arr[i],arr,k,ans)

        # not take element and move
        temp.pop()
        b = self.combination_sum(i+1,temp,curr_sum,arr,k,ans)

        return

if __name__ == "__main__":

    ans = []
    arr = [2,3,5]
    k = 8
    sol = Solution()
    aa = sol.combination_sum(0,[],0,arr,k,ans)
    print(ans)
    print(aa)