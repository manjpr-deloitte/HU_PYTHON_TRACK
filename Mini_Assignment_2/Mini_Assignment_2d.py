nrows= int(input("enter no of rows:"))
for row in range(1,nrows+1):
    for col in range(1,nrows+1):
        if(col == nrows) or (row == 1) or (col == row):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
