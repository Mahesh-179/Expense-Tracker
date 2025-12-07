from expense_data import expense
from datetime import date

# ADDING USER DATA IN EMPTY LIST
def expense_list():
    today = date.today()
    category = input("Enter your category(RENT,FOOD,MEDICINE,COLLEGE OR OTHER):  ").upper().strip()
    description = input("Enter your description: ").strip().upper()
    amount = float(input("Enter your amount(NPR): "))

    expenses = {
        "date": today,
        "category": category,
        "description": description,
        "amount": amount
    }
    expense.append(expenses)
    print("\n DONE BRO !! Expenses added successfully")



