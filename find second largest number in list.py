list=[12,45,7,89,23,56]
largest=list[0]
second=list[0]
for i in list: 
    if i>largest:
        second=largest
        largest=i
    elif i>second:
        second=i   
print(second)      
    

