numbers=[2,5,2,8,5,9,2]
new_list=[]
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)  
