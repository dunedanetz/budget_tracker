print('Welcome to Budget Tracker!')

while True:
    try:
        initial_budget = float(input('Please provide your monthly budget in €: '))
        if initial_budget >= 0:
            break
        else:
            print('Please provide a positive number.')
    except ValueError as e:
        print(f"An error occurred: {e}.\nPlease try again.")
        continue

print(f'Your monthly budget is: {initial_budget:.2f} €') 

fixed_expenses = {} 
spent_total = sum(fixed_expenses.values()) #sum(category: value) calculates the values of all keys in the dictionaly

while True:
    try:
        count_categories = int(input('How many Budget Categories do you want to add now?'))
        if count_categories > 0:
            break
        else:
            print('Please provide a positive whole number (> 0).')
    except ValueError as e:
        print(f"An error occurred: {e}.\nPlease try again.")
        continue

for i in range(count_categories):
    new_category = input('Provide an expense category: ')

    while True:
        try:
            new_category = new_category.strip().lower()
            if new_category == '':
                print('Category name cannot be empty. Please try again.')
                new_category = input('Provide an expense category: ')
                continue
            break
        except ValueError as e:
            print(f"An error occurred: {e}.\nPlease try again.")
            continue

    formatted_category = new_category.strip().lower()

    while True:
        try:
            new_expense = float(input(f'Provide a {new_category} budget amount in €: '))
            if new_expense > 0:
                break
            else:
                print('The Expense category must have a monthly budget. Please provide a sum.')
        except ValueError as e:
            print(f"An error occurred: {e}.\nPlease try again.")
            continue

    fixed_expenses[new_category.strip()] = fixed_expenses.get(new_category, 0) + new_expense
    spent_total += new_expense

    print(f"You entered: Budget category {new_category} - Monthly amount {new_expense:.2f} €")

spent_total = sum(fixed_expenses.values())
remaining = initial_budget - spent_total

print("\nExpenses:")
for category, amount in sorted(fixed_expenses.items()):
    print(f"- {category}: {amount:.2f} €")

print(f"Total spent: {spent_total:.2f} €")

if remaining < 0:
    print(f'Over the budget by {abs(remaining)} €')
elif remaining == 0:
    print('Exactly on budget!')
else:
    print(f'Your remaining expendable budget is: {remaining:.2f} €')