#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    common = ""
    if len(strs) == 0:
        return
    for letter in range(len(strs[0])):
        for word in range(1, len(strs)):
            if letter >= len(strs[word]) or strs[0][letter] != strs[word][letter]:
                return common
        common += strs[0][letter]
        

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["a","w","q"]))
print(longestCommonPrefix(["","",""]))