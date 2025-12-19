#Median,mode,mean,range,interquartile range
import numpy as np
elements=[]
total=0
while True:
    try:
        Count=int(input("How many number values do you wish to enter for the array?\n"))
        break
    except ValueError:
        print("Should be an integer")
#Count=int(input("How many number values do you wish to enter for the array?\n"))
while Count<=0 or Count>30:
    if Count<0:
        print("Array cannot have negative number of elements")
    elif Count==0:
        print("Array cannot have 0 values")
    else:
        print("Too many values")
    Count=int(input("How many number values do you wish to enter?\n"))
for i in range(0,Count):
    num=int(input("Enter number {} \n".format(i+1)))
    total+=num
    elements.append(num)
elements.sort()
print(elements)
choice=""
def calculatesd():
            t=0
            length=len(elements)
            mean=total/Count
            for i in range(length):
                p=(elements[i]-mean)**2
                t=t+p
            variance=t/length
            standard_deviation=variance**0.5
            if type(standard_deviation)==float:
                standard_deviation=round(standard_deviation,2)
            return standard_deviation
while choice!="end" and choice!="e":
    print("\nENTER END TO STOP THE PROGRAM\n")
    choice=str(input("Which do you choose:\n1.Median\n2.Mode\n3.Mean\n4.Range\n5.Interquartile Range\n6.Standard Deviation\n7.Co-efficient of Variation\n\n")).strip().lower()
    if choice=="1" or choice=="median" or choice=="med":
        if Count%2==0:
            value1=int(Count/2)
            value2=value1-1
            median1=elements[value1]
            median2=elements[value2]
            median=(median1+median2)/2
        else:
            value=int(((Count+1)/2)-1)
            median=elements[value]
        print(elements)
        print(f"The median is {median}")
    elif choice=="2" or choice=="mode":
        mode_total2=0
        for j in range(0,Count):
            mode_total=0
            for i in range(0,Count):
                if elements[j] == elements[i]:
                    mode_total += 1
            if mode_total>mode_total2:
                mode_total2=mode_total
                mode_value2=elements[j]
        print(elements)
        if mode_total2==1:
            print("There is no mode")
        else:
            print(f"The mode is {mode_value2}")
    elif choice=="3" or choice=="mean":
        mean=total/Count
        print(elements)
        print(f"The mean is {mean}")
    elif choice=="4" or choice=="range" or choice=="r":
        smallest=elements[0]
        largest=elements[(len(elements)-1)]
        rangevalue=largest-smallest
        print(elements)
        print(f"Range value is {rangevalue}")
    elif choice=="5" or choice=="interquartile range" or choice=="i":
        q1 = np.percentile(elements, 25)
        q3 = np.percentile(elements, 75)
        iqr = q3 - q1
        print(elements)
        print(f"THe lower quartile:{q1}\nThe upper quartile:{q3}")
        print("The interquartile range",iqr)
    elif choice=="6" or choice=="sd" or choice=="standard_deviation":
        
        standard_deviation=calculatesd()
        print(f"The standard deviation is {standard_deviation}")
    elif choice=="7" or choice=="cv":
        mean=total/Count
        standard_deviation=calculatesd()
        coefficientofvariation=(standard_deviation/mean)*100
        if type(coefficientofvariation)==float:
            coefficientofvariation=int(coefficientofvariation)
        print(f"Co efficient of Variation is {coefficientofvariation}%")

    elif choice=="end" or choice=="e":
        print("OK Bye")
    else:
        print("Invalid input")
