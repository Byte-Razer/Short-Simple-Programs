import math
choice=1
while choice!=3:
  choice=int(input("Choose what u want to do:\nOption 1: Calculation\nOption 2: Function\nOption 3: Exit "))
  if choice==1:
    mathchoice=0
    while mathchoice!=1 and mathchoice!=2 and mathchoice!=3 and mathchoice!=4 and mathchoice!=5 and mathchoice!=6:
      mathchoice=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square\n6.Square root\n"))
    if mathchoice==1 or mathchoice==2 or mathchoice==3 or mathchoice==4:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter second number: "))
        operation=""
        if mathchoice==1:
          operation="+"
        elif mathchoice==2:
          operation="-"
        elif mathchoice==3:
          operation="*"
        elif mathchoice==4:
          operation="/"
        #operation=input("Enter operation")
        if operation=="/" and num2==0:
          print("Division by zero is not possible.")
          while num2==0:
            num2=int(input("Enter New denominator: "))
        #while operation!="+" and operation!="-" and operation!="*" and operation!="/":
        #  print("Operation shud be + - / or *")
        #  operation=input("Enter operation")
        if operation=="+":
          ans=num1+num2
        elif operation=="-":
          ans=num1-num2
        elif operation=="*":
          ans=num1*num2
        elif operation=="/":
          ans=num1/num2
          ans=round(ans,2)
        else:
          print("Invalid operation")
    elif mathchoice==5 or mathchoice==6:
      num=int(input("Enter the number"))
      if mathchoice==5:
        ans=num**2
      elif mathchoice==6:
        if num<0:
          print("Math error.")
          while num<0:
            num=int(input("Enter positive number to square root"))
        ans=math.sqrt(num)
    else:
      print("Invalid math choice")
      ans=""
    print("The answer is: ",ans)


  elif choice==2:
    print("Time to simplify a quadratic!")
    print("In 0 = ax²+bx+c")
    #printing the quadratic
    signa = signb = signc = "+"
    a=int(input("a= "))
    while a==0:
      print("Not a quadratic")
      a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    d=(b**2)-(4*a*c)
    while d<0:
      print("b²-4ac<0, no solution. ")
      a=int(input("a= "))
      while a==0:
        print("b")
        a=int(input("a= "))
      b=int(input("b= "))
      c=int(input("c= "))
      d=(b**2)-(4*a*c)
    if a<0:
      signa="-"
    if b<0:
      signb=""
    if c<0:
      signc=""
    if a==1:
      a=""
    print(f"0 = {str(a)}x²{signb}{str(b)}x{signc}{str(c)}")
    if a=="":
      a=1
    if a<0:
      a, b, c = -a, -b, -c
    value=math.sqrt(d)
    x=(-b+value)/(2*a)
    if x!=int(x):
      x=round(x,2)
    else:
      x=int(x)
    x2=(-b-value)/(2*a)
    if x2!=int(x2):
      x2=round(x2,2)
    else:
      x2=int(x2)
    xc="-"
    xc2="-"
    if x<0:
      xc="+"
      x=abs(x)
    x=str(x)
    if x2<0:
      xc2="+"
      x2=abs(x2)
    x2=str(x2)

    print("0= "+"(x"+xc+x+")"+"(x"+xc2+x2+")")
  elif choice==3:
    print("Bye")
  else:
    print("Invalid option")  
