class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create an empty dictionary to store the anagrams
        anagrams = {}

        # Iterate through the strings in the input list
        for s in strs:
            # Sort the string
            sorted_s = ''.join(sorted(s))

            # Check if the sorted string is in the dictionary
            if sorted_s in anagrams:
                # If it is, add the string to the list of anagrams
                anagrams[sorted_s].append(s)
            else:
                # If it is not, create a new list with the string and add it to the dictionary
                anagrams[sorted_s] = [s]

        # Return the values of the dictionary as a list
        return list(anagrams.values())
    

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["a"]))
    print(Solution().groupAnagrams(["a", "b"]))
    print(Solution().groupAnagrams(["a", "b", "c"]))
    print(Solution().groupAnagrams(["a", "b", "c", "d"]))
    print(Solution().groupAnagrams(["a", "b", "c", "d", "e"]))
    print(Solution().groupAnagrams(["a", "b", "c", "d", "e", "f"]))