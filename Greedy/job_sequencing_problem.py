class Solution:
    def jobSequencing(self, deadline, profit):
        
        n = len(deadline)
        jobs = list(zip(profit,deadline))
        jobs.sort(reverse=True)

        max_deadline = max(deadline)
        job_sequence = [-1]*(max_deadline+1)

        for pf , ded in jobs:
            
            for i in range(ded,0,-1):
                # print(i)
                if job_sequence[i] == -1:
                    job_sequence[i] = pf
                    break

        number_of_jobs = 0
        total_profit = 0
        for i in range(len(job_sequence)):
            if job_sequence[i] != -1:
                number_of_jobs += 1
                total_profit += job_sequence[i]

        print(total_profit,number_of_jobs)
        return job_sequence
        


if __name__ == "__main__":

    deadline = [4, 1, 1, 1]
    profit = [20, 10, 40, 30]
    sol = Solution()
    ans = sol.jobSequencing(deadline,profit)

    print(ans)
