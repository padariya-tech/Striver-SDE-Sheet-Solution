class Solution:
    def move_zeros_to_end(self,a):
        n = len(a)
        j = 0
        for i in range(n):
            if a[i] == 0:
                j = i
                break

        for i in range(j+1,n):
            if a[i] != 0:
                a[i],a[j] = a[j],a[i]
                j += 1

        return a
        


if __name__ == "__main__":

    a = [1,0,0,0,0]

    sol = Solution()
    answer = sol.move_zeros_to_end(a)
    print(answer)

