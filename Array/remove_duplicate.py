class Solution:
    def remove_duplicates(self,arr):
        n = len(arr)
        i,j = 0,0

        for j in range(1,n):

            if arr[j] != arr[i]:
                i+=1
                arr[i] = arr[j] 
        
        return arr


if __name__ == "__main__":

    a = [1,1,1,1,1,1,1,1,2,2,3,4,4]

    sol = Solution()
    answer = sol.remove_duplicates(a)
    print(answer)

