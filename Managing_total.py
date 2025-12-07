from expense_data import expense
def total_management():
    total = 0
    for exp in expense:
        total = total + exp['amount']
    print("\n   Total Expenses :", total)