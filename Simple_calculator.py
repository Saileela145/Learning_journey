def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print('''select the operation:\n
      1.Add\n
      2.Sub\n
      3.Mul\n
      4.div''')
sel=int(input("enter the operation(1-4):"))
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
if sel==1:
    print(a,"+",b,"=",add(a,b))
elif sel==2:
    print(a,"-",b,"=",sub(a,b))
elif sel==3:
    print(a,"*",b,"=",mul(a,b))
elif sel==4:
    print(a,"/",b,"=",div(a,b))
else:
    print("invalid operation")
