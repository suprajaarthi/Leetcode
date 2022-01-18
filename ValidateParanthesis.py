def isValid(s):    
    parent = ['{}','()','[]']
    if s == '':
        return True

    for el in parent:
        
        if el in s:
            print(el)
            return isValid(s.replace(el,''))
            
    return False

s=input().strip()
print(isValid(s))


# 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


#   Input s="[{]}"
# Output: false
