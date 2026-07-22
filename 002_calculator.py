from unittest import result


print("Welcome to the calculator project")
first_number = int(input("Enter your first number:"))
sec_number = int(input("Enter your sec number:"))
'''
sum = first_number + sec_number
diff = first_number - sec_number
multiply = first_number * sec_number
div = first_number / sec_number'''

opr = input("Enter your operator:")

if sec_number != 0:
    result = first_number / sec_number
else:
    result = 'cannot divide by 0'

if opr == '+' or opr == 'sum':
    print(f"sum is:{first_number + sec_number}")

elif opr == "-" or opr == 'diff':
    print(f"Diff is:{first_number - sec_number}")    

elif opr == "*" or opr == 'mul':
    print(f"multiple is:{first_number * sec_number}")    
elif opr == "/" or opr == 'div':
    print(f"div is: {result}")    

 
    

else:
    print("Invalid operator")                
 