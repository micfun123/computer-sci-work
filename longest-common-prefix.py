# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs):
    if not strs:  # if strs is empty
        return ""
    if len(strs) == 1:  # if strs has only one element
        return strs[0]
    strs.sort()  # sort the list of strings in alphabetical order  as ["flower","flow","flight"] becomes ["flight","flow","flower"]
    print(strs)
    result = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            result += strs[0][i]
        else:
            break
    return result


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["a", "a"]))
print(longestCommonPrefix(["a"]))
print(longestCommonPrefix(["", ""]))
