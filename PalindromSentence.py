s=input().strip()

s=''.join(ch for ch in s.lower() if ch.isalnum())
print(s)
if s==s[::-1]:
    return True 
else: 
    return False
  
#  Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
