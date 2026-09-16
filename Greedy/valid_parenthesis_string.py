class Solution:
    def checkValidString(self, s: str) -> bool:
        low , high = 0,0

        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if low < 0:
                low = 0
            if high < 0:
                return False

        return low == 0




if __name__ == "__main__":

    sol = Solution()
    s = "***)"
    ans = sol.checkValidString(s)
    print(ans)


# // Recursive Solution
# class Solution {
#     bool ex(int ind, int count, string &s){
#         if(ind==s.size()) return (count==0);

#         bool ans=false;
#         if(s[ind]=='*'){
#             ans|=ex(ind+1,count+1,s); // Add '('
#             if(count) ans|=ex(ind+1,count-1,s); // Add ')'
#             ans|=ex(ind+1,count,s); //Add Nothing
#         }else{
#             if(s[ind]=='('){
#                 ans=ex(ind+1,count+1,s);
#             }else{
#                 if(count) ans=ex(ind+1,count-1,s);
#             }
#         }

#         return ans;
#     }

# public:
#     bool checkValidString(string s) {
#         return ex(0,0,s);
#     }
# };