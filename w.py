name=input("enter student name : ")
marks1=int(input("enter math marks : "))
marks2=int(input("enter math marks : "))
marks3=int(input("enter math marks : "))
marks4=int(input("enter math marks : "))
marks5=int(input("enter math marks : "))

total=marks1+marks2+marks3+marks4+marks5
per=total/5
def calculate():
    if per>=91:
        print("grade :","A+")
    elif per>=80:
        print("grade :","A")
    elif per>=70:
        print("grade :","B")
    elif per>=60:
        print("grade :","C")
    elif per>=33:
        print("grade :","D")
    else:
        print("please prectice more and work hard","Fail")
        
        
def pas():
    if per>32:
        print("status  :","pass")
    else:
        print("status  :","fail")
        
def remarks():
    if per>=91:
        print("remarks :","Excellent")
    elif per>=80:
        print("remarks :","very good")
    elif per>=70:
        print("remarks :","good ")
    elif per>=60:
        print("remarks :","average")
    elif per>=33:
        print("remarks  :","need Improvement")
    else:
        print("Work hard")    
        
def result():
    print("======result======")
    print("mathes       :",marks1)
    print("physics      :",marks2)
    print("chamistry    :",marks3)
    print("English      :",marks4)
    print("computer     :",marks5)
    print()
    print()
    print("total        :",total)
    print("persentage   :",per)
    
    

result()
calculate()
remarks()
    
    
