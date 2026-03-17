n1=int(input("Enter value:"))
n2=int(input("Enter value:"))
n3=int(input("Enter value:"))
n4=int(input("Enter value:"))
max=n1
if max<n2:
    max=n2
    if max<n3:
        max=n3
        if max<n4:
            max=n4
            print("Max number is:",max)
