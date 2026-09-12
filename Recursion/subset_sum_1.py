class Solution:
    def subset_sum(self,i,temp,curr_sum,arr,k,ans):
        if i == len(arr):
                # print(temp)
                ans.append(curr_sum)
                return
            
         
        # take 
        temp.append(arr[i])
        self.subset_sum(i+1,temp,curr_sum+arr[i],arr,k,ans)

        # not take
        temp.pop()
        self.subset_sum(i+1,temp,curr_sum,arr,k,ans)

        return

if __name__ == "__main__":

    ans = []
    arr = [3,2,1]
    k = 2
    sol = Solution()
    sol.subset_sum(0,[],0,arr,k,ans)
    ans = sorted(ans)
    print(ans)
