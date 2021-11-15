s="abcabcbb"
m={}
string = s
max_length = 0    
seen_character = ''
for letter in string:   
    if letter not in seen_character:
        seen_character += letter    
    else:
        seen_character = seen_character[seen_character.index(letter) + 1:] + letter
        print(seen_character)
    max_length = max(max_length, len(seen_character))   
    # abc - bca - cab - abc - cb
print(max_length)   

'''
If the str has repeated character , remove it from the existing string and proceed. 
Update the length of the new str 
Return the max len of the str 
'''
