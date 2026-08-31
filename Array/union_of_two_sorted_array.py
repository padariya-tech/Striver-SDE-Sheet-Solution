class Solution:
    def find_union(self,a,b):
        n = len(a)
        m = len(b)
        ans = []
        i,j = 0,0
        while i < n and j < m:

            if a[i] < b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not ans or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1
            else:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1

        while i < n:
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1

        while j<m:
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1
        
        return ans


if __name__ == "__main__":

    a = [1,2,3]
    b = [4,5,6]

    sol = Solution()
    answer = sol.find_union(a,b)
    print(answer)

