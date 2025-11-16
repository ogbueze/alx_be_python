num = int(input("Enter the size of the pattern:"))

count = 0
while count < num:
    for i in range(num):
            print("*", end="")
    print()
    count +=1 