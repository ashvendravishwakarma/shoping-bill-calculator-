print("================SHOPING BILL CALCULATOR=============== ")

customer_name=input("enter customer name  : ")

product1=input("product name : ")
p1=int(input("enter price :"))
q1=int(input("enter quantity of product"))

product2=input("product name : ")
p2=int(input("enter price :"))
q2=int(input("enter quantity of product"))

product3=input("product name : ")
p3=int(input("enter price :"))
q3=int(input("enter quantity of product"))

product4=input("product name : ")
p4=int(input("enter price :"))
q4=int(input("enter quantity of product"))

product5=input("product name : ")
p5=int(input("enter price :"))
q5=int(input("enter quantity of product"))

total_bill=(p1*q1)+(p2*q2)+(p3*q3)+(p4*q4)+(p5*q5)

def prodect():
    print("========== SHOPPING BILL ==========")
    print()
    print("Customer name          :",customer_name)
    print()
    print()
    print(f"{product1}      {p1} x {q1} = {(p1*q1)}")
    print(f"{product2}      {p2} x {q2} = {(p2*q2)}")
    print(f"{product3}      {p3} x {q3} = {(p3*q3)}")
    print(f"{product4}      {p4} x {q4} = {(p4*q4)}")
    print(f"{product5}      {p5} x {q5} = {(p5*q5)}")

def total():
    print("--------------------------------------------------")
    print("Total          :",total_bill)
    print("--------------------------------------------------")

def discount():
    if total_bill>=2000:
        print("Discount          : 20 %")
        print("Discount ammount  :",total_bill*(20/100))
        print("Final ammount     :",total_bill-(total_bill*(20/100)))
        
        
    elif total_bill>=1000:
        print("Discount          :10 %")
        print("Discount ammount  :",total_bill*(10/100))
        print("Final ammount     :",total_bill-(total_bill*(10/100)))
        
        
    elif total_bill>=500:
        print("Discount          :5 %")
        print("Discount ammount  :",total_bill*(5/100))       
        print("Final ammount     :",total_bill-(total_bill*(5/100)))
    else:
        print("NO DISCOUNT ")
        print("Final ammount     :",total_bill)
    print("Thank you for shopping ")
        
prodect()
total()
discount()