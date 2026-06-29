class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]]+=1
            else:
                counts[s[i]]=1
            if t[i] in counts:
                counts[t[i]]-=1
            else:
                counts[t[i]]=-1
        for val in counts.values():
            if val!=0:
                return False
        return True

#NOTES
#first check if both string lengths r equal, if not equal return False
#make dictionary of counts
#check if each letter for first string is in counts,
#if not add to dictionary, if it is add 1
#then check each letter for seconf string is in counts,
#if not set equal to -1, if it is subtract 1 from value

#go through each value in counts and if each == 0 then return True