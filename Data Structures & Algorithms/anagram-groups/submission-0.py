class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #used to map charCount to list of anagrams
        for s in strs: #iterate through every string 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)   

        return list(res.values())


