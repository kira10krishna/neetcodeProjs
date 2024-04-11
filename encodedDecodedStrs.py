class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        # Initialize an empty string to store the encoded string
        encoded_str = ""

        # Iterate over the list of strings
        for s in strs:
            # Encode each string by prefixing it with its length
            encoded_str += str(len(s)) + ":" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        # Initialize an empty list to store the decoded strings
        decoded_list = []

        # Initialize a variable to store the current index
        i = 0

        # Iterate while the index is less than the length of the encoded string
        while i < len(s):
            # Decode the next string by first extracting its length
            length = int(s[i:i + 2])

            # Extract the string itself
            string = s[i + 2:i + 2 + length]

            # Add the decoded string to the list
            decoded_list.append(string)

            # Update the index
            i += 2 + length

        return decoded_list