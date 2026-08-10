from typing import List
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        answer = []
        temp=[1]
        answer.append(temp)
        for i in range(1,n):
            temp = answer[i-1]
            new_array=[]
            new_array.append(1)
            for j in range(1,len(temp)):
                val = temp[j]+temp[j-1]
                new_array.append(val)
            new_array.append(1)
            answer.append(new_array)

        return answer
if __name__ == "__main__":

    sol = Solution()
    n = 5
    answer = sol.generate(n)
    print(answer)