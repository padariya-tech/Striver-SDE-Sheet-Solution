class Solution:

    def check_balance(self,s):
        n = len(s)
        if n == 0:
            return True
        
        st = []
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                # print("append")
                st.append(s[i])

            elif s[i] == ')' and st[-1] == '(':
                st.pop()
            
            elif s[i] == '}' and st[-1] == '{':
                st.pop()

            elif s[i] == ']' and st[-1] == '[':
                st.pop()

            else:
                return False
            
        return len(st)==0



if __name__ == "__main__":

    s = "[["

    sol = Solution()
    answer = sol.check_balance(s)
    print(answer)