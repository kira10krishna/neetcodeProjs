class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are equal
        if len(s)!= len(t):
            return False

        # Sort the strings
        s = sorted(s)
        t = sorted(t)

        # Check if the sorted strings are equal
        return s == t

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"


    print(Solution().isAnagram(s="anagram", t="nagaram"))
    print(Solution().isAnagram(s="rat", t="car"))