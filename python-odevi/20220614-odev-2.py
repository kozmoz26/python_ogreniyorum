

#user will input first number
num1=int(input("input number 1 :")) 

#user will input second number
num2=int(input("input number 2 :"))

#user will input third number
num3=int(input("input number 3 :"))

#add given numbers
result1=num1+num2+num3

#subtract given numbers
result2=num1-num2-num3

#take the average of given numbers
result3=result1*(1/3)

#ask for the result the user wants to see
x=(input("which result you want to see?( result1 / result2 / result3 ):"))

#show the result the user wants to see
if x == "result1":
    print(result1)
elif x == "result2":
    print(result2)
elif x== "result3":
    print(result3)
else:
    print("invalid result")


