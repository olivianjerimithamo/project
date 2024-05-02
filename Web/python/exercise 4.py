print("grades calculator")
math  =  int(input("math =  "))
eng   =  int(input("eng =  "))
phyc  =  int(input("phyc = "))
kisw  = int(input("kisw =  "))
hist   = int(input("hist =  "))
total = math + eng + phyc + kisw + hist
average = total/5
print(average)

if average  >=0 and average <= 39:
    print("E")
elif average >= 40 and average <=50:
    print("D")
elif average >= 51 and average <= 60:
    print("C")
elif average >= 61 and average <= 70:
    print("B")
elif average >= 71 and average <= 100:
    print("A")
else:
    print("invalid input")

