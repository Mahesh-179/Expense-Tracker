# Expense Calculator
from Adding_Expenses import *
from Managing_total import *
from Accessing_Expense import *
from expense_data import expense
from csv_file_data import save_all_expenses_to_csv
print(" TALAI AAFNO KHARCHA PANII YAAD HUNNA HAII JATHAA !! ")
while True:
    print("============== MENU =====================")
    print("1. Add Expense")
    print("2. View Expense")
    print("3.View Total Sum of Expenses ")
    print("4. Save to csv")
    print("5.Quit")
    choice=input("Enter your choice: ")

# ADDING USER DATA IN EMPTY LIST
    if choice=="1":
        expense_list()

# VIEWING USER LIST FROM THE EMPTY LIST
    elif choice=="2":
        accesing_list_saman()
# View Total Spending
    elif choice=="3":
      total_management()
#saving to csv file
    elif choice=="4":
        save_all_expenses_to_csv(expense)
# Exiting While Loops
    elif choice=="5":
        print(" ARKO PALI DEKHI AAFAI YAAD RAKH HAII ")
        break
else:
    print("Invalid choice")