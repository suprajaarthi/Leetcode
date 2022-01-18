candidates = [2,3,5]
target = 8
dp = [[] for _ in range(target+1)]
for i in candidates:
    # i index
    # 2 - 12345678 21 22 23 24
    # 3 - 12345678
    # 5 - 12345678
    # 235
    for index in range(1, target+1):
        # 1,9-> 
        # if 1<2 : 
        if index < i: continue
        # 2==2 dp[2]
        elif index == i: dp[index].append([i])

        else: 
            for combination in dp[index-i]:
                dp[index].append(combination + [i])
        #  for j in dp[3-3]:
        #     dp[3].app(0+3)=> 3 
        #   for j in dp[4-3]:
        #       dp[4].app(0+2)
print(dp)                      
print(dp[target])
