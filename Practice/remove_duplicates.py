numbers = [61,77,11,66,100,23,18,94,11 ,77 , 66 ]
removed_duplicates = []

for i in numbers :
    if not i in removed_duplicates:
        removed_duplicates.append(i)
removed_duplicates.sort()
print(removed_duplicates)