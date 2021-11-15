''' 
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''

from collections import Counter
s1 = "ab"
s2 = "eidbaooo"
window = len(s1)
s1_c = Counter(s1)
print(s1_c)        
for i in range(len(s2)-window):
    print(i)
    s2_c = Counter(s2[i:i+window])
    print(s2_c)
    if s2_c == s1_c:
        print("True")
        f=1
if f!=1:
    print("False")
    
