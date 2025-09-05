print('Welcome to Budget Tracker!')

initial_budget = int(input('Please provide your monthly budget in €: '))
print(f'Your monthly budget is: {initial_budget} €') 

fixed_expenses = {} 
spent_total = 0 

new_category = input('Provide an expense category: ')
new_expense = int(input(f'Provide a {new_category} budget amount in €: '))


fixed_expenses[new_category] = fixed_expenses.get(new_category, 0) + new_expense
spent_total += new_expense
print(f"You entered: Budget category {new_category} - Monthly amount {new_expense} €")

print(fixed_expenses)

remaining = initial_budget - spent_total

print("\nExpenses:")
for category, amount in sorted(fixed_expenses.items()):
    print(f"- {category}: {amount} €")
print(f"Total spent: {spent_total} €")

if remaining < 0:
    remaining = abs(remaining)
    print(f'Over the budget by {remaining} €')
elif remaining == 0:
    print('Exactly on budget!')
else:
    print(f'Your remaining expendable budget is: {remaining} €')