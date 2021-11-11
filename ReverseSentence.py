s = "Let's take LeetCode contest"
list_s = s.split(" ")
temp_list = []
for i in list_s:
    temp_list.append(i[::-1])
print(" ".join(temp_list))

