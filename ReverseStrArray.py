s = ["h","e","l","l","o"]
print(int(len(s)/2))
for i in range(0,int(len(s)/2)):
    s[i],s[-i-1] = s[-i-1],s[i]
    print(s)
    
print(s)
'''
0,-1=-1,0
oellh 
1 -2 = -2 1 
olleh
2,-3 = -3 ,2 
olleh  

2nd testcase 
hell 

lelh

lleh 
'''
