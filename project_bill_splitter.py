print("Bill splitter")
total_bill = int(input("How much the total bill $ "))
tip_percentage = int(input("How much the tip percentage 5, 10, 15, 25: %  "))
number_of_people = int(input("Total number of people sit in one table: "))
tip_amount = total_bill * (tip_percentage/100)
amount_per_person = total_bill * (1 + tip_percentage/100)/number_of_people
print(f"Amount of each person to pay is: {amount_per_person:.2f}")
total = total_bill + tip_amount
print(f"Total bill of the table is:{total}")
 



