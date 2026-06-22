class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            counts=[0]*26
            for ch in word:
                counts[ord(ch)-ord('a')] +=1
            key=tuple(counts)
            res[key].append(word)
        return list(res.values())

#create an empty dictionary to group words that are anagrams
#go through each word in the input list
#create a list of 26 zeros to count how many times each letter a-z appears in the word
#loop through each character in the current word
#convert character into a number from 0 to 25, where a = 0, b = 1, and so on
#increase the count for that letter
#change the list into a tuple so it can be used as a dictionary key
#check if this letter-count pattern has not been seen before
#create a new empty list for that anagram group
#create a new empty list for that anagram group
#return all the grouped anagram lists
