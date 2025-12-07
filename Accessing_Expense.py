from expense_data import expense
def accesing_list_saman():
    if (len(expense) == 0):
        print("No expenses, Paila Kharcha ta gar na Bro")
    else:
        count = 1
        for exp in expense:
            print(f"{count}-> {exp['date']},{exp['category']},{exp['description']},Rs.{exp['amount']}")
            count = count + 1