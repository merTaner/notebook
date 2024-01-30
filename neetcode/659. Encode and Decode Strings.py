"""
Description

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is 
decoded back to the original list of strings.

Please implement encode and decode

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"


Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"


Takeaway :

use join(':;') on all strings item so string in encoder

then result of encoder's use in decoder method

** use only one charter for sperate strings. This time we have a problem. 

example -> ['mert', 'mert:;taner'] if we have like this list we during encode and decode

decode is never assing to original list. encode = 'mert:;mert:;taner;;' okay but decoder = ['mert', 'mert', 'taner'] 

"""

class Solution:
    """
    def encode(self, strings):
        return ':;'.join(strings)
        
    def decode(self, str):
        return str.split(':;')
    """

    def encode(self, strings):
        res = ''
        for s in strings:
            res += str(len(s)) + '#' + s 
        return res
    
    def decode(self, str):
        result = []
        i = 0

        while i < len(str):
            # this index holds width for the length of the word
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j+1: j+1+length])
            i = j + 1 + length
        return result

if __name__ == '__main__':
    sol = Solution()
    result_of_endocer = sol.encode(["lint","code","love","you"])
    print(sol.decode(result_of_endocer))
