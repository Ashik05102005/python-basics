nums = [1,2,3,4,5,6,7,1,2,4,6,2,1,6,7,9,8,3,1,2,4,6,8,9]

nums_dict ={}

for i in nums :
    if i  in nums_dict:
        nums_dict[i] = nums_dict[i]+1

    else :
        nums_dict[i] = 1

res = []
for value in nums_dict.items():
    res.append((f"num {value[0]}" ,f"count {value[1]}"))

print(res)