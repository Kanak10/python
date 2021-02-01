n = int(input())
n1 = int(input())

o = input("Which Operator You Want to Use:\n+\n-\n*\n/\n")

if (o == "+"):
    if ((n == 56 or n == 9) and (n1 == 56 or n1 == 9)):
        print("77")
    else:
        print(n + n1)

elif (o == "-"):
    print(n - n1)

elif (o == "*"):
    if ((n == 45 or n == 3) and (n1 == 45 or n1 == 3)):
        print("555")
    else:
        print(n * n1)

elif (o == "/"):
    if (n == 56 and n1 == 6):
        print("4")
    else:
        print(n / n1)

else:
    print("Please Enter Valid Operator")