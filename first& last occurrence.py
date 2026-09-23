num=[4,7,2,7,9,7,5]
n=7
first=-1
last=-1
for i in range(len(num)):
    if num[i]==7:
        if first == -1:
            first=i
        last=i
print("first occurence=",first)
print("second occurence=",last)
