k = 8
for i in range(0,5):
    for j in range(0,k):
        print(end=" ")
    k -= 2
    
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")

x = 65
for i in range(5):
    for j in range(0,i+1):
        print(chr(x),end=" ")
        x += 1
    print("\n")

    