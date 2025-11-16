num = int(input("Enter the size of the pattern:"))

count = 0
while count < num:
    pattern = ''
    for i in range(1, num+1):
        pattern +='*'
    print(pattern)
    count += 1