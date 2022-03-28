class Solution:
    def beautifulArray(self, n: int):
        
        def divide(n):
            if n == 1:
                return [1]
            
            odds = divide(n//2 + n%2)
            even = divide(n//2)
            
            sum_odds = [2*x-1 for x in odds]
            sum_even = [2*x for x in even]

            return sum_odds + sum_even

        return divide(n)