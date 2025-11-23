def triangle(n):
    for i in range(1,n+1):
        print(" ",end="")
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()    
triangle(5)            
