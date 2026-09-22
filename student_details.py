dict={}
dict["name"]="varshini"
dict["roll_no"]=19
dict["course"]="python"
dict["year"]=2
print("student_details=",dict)
dicti={}
n=int(input("enter no.of subjects:"))
for i in range (n):
    sub=input("enter sub name:")
    marks=int(input("enter marks:"))
    dicti[sub]=marks
total_marks=sum(dicti.values()) 
print("sub=",dicti.keys())
print("marks=",dicti.values())
print("sum=",total_marks)
avg=total_marks/len(dicti)
print("avg=",avg)
print("___Grade Details____")    
for sub,marks in dicti.items():
    if marks >=90:
        print("A")
    elif marks >=75:
        print("B")
    elif marks >=60:
        print("c")
    else:
        print("D") 
print("___avg_grade___")         
if avg>=90:
    print("A")
elif avg >=75:
    print("B")
elif avg >=60:
    print("c")
else:
    print("D") 
print("pass or fail") 
if avg>=50:
    print("pass")
else:
    print("fail")       

