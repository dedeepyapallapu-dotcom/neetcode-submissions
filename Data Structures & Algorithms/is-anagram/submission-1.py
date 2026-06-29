class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick length check
        if len(s) != len(t):
            return False
        
        counts = {}
        
        # Step 2: Update counts for both strings
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Process character from string 's' (+1)
            if char_s in counts:
                counts[char_s] += 1
            else:
                counts[char_s] = 1
                
            # Process character from string 't' (-1)
            if char_t in counts:
                counts[char_t] -= 1
            else:
                counts[char_t] = -1
        
        # Step 3: Verify all balances are perfectly at 0
        for val in counts.values():
            if val != 0:
                return False
                
        return True