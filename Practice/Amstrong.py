num = 153
reminder = []
length = len(str(num))

# print(length)

while num > 0 :
    rem = num % 10
    amstrong_num = rem**length 
    reminder.append(amstrong_num)
    num = int(num/10)
total = 0 
for item in reminder :
    total+=item

if(num==total):
    print("it is a amstrong number")
else : 
    print("it is not a amstrong number")
