class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for string in strs:
            cr = "".join(sorted(list(string)))
            if cr not in output:
                output[cr] = [string]
            else:
                output[cr].append(string)
        
        return [output[key] for key in output]