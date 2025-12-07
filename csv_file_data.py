import csv

def save_all_expenses_to_csv(expense_list, filename="expenses.csv"):
    total = 0  # initialize total

    # OPEN FILE USING 'with' BLOCK
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["Date", "Category", "Description", "Amount"])

        # Write all expenses and calculate total
        for exp in expense_list:
            writer.writerow([
                exp["date"],
                exp["category"],
                exp["description"],
                exp["amount"]
            ])
            total += exp["amount"]  # accumulate total

        # WRITE TOTAL INSIDE 'with' BLOCK
        writer.writerow([f"Total(NPR)", "", "", total])

    # File is now closed automatically
    print(f"All expenses saved successfully. Total expenses: {total} NPR")
