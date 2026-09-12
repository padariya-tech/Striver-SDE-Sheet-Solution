class Solution:
    def subsequence_sum_k(self,i,temp,curr_sum,arr,k,ans):
        if i == len(arr):
            if curr_sum == k:
                # print(temp)
                ans.append(temp.copy())
                return 1
            else:
                return 0
         
        # take 
        temp.append(arr[i])
        a = self.subsequence_sum_k(i+1,temp,curr_sum+arr[i],arr,k,ans)

        # not take
        temp.pop()
        b = self.subsequence_sum_k(i+1,temp,curr_sum,arr,k,ans)

        return a+ b

if __name__ == "__main__":

    ans = []
    arr = [1,2,1]
    k = 2
    sol = Solution()
    aa = sol.subsequence_sum_k(0,[],0,arr,k,ans)
    print(ans)
    print(aa)