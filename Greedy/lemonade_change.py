from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        count_5 = 0
        count_10 = 0

        for i in range(n):
            if bills[i] == 5:
                count_5 += 1
            if bills[i] == 10:
                count_10 += 1
                if count_5 >= 1:
                    count_5 -= 1
                else:
                    return False
                
            if bills[i] == 20:
                if count_5 >= 1 and count_10 >= 1:
                    count_5 -= 1
                    count_10 -= 1

                elif count_5 >= 3:
                    count_5 -= 3

                else:
                    return False

        return True
        

if __name__ == "__main__":

    bills = [5,5,10,10,20]
    sol = Solution()
    ans = sol.lemonadeChange(bills)
    print(ans)