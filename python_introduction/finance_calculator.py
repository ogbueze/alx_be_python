Monthly_income = int(input('Enter your monthly income:'))
Monthly_expenses = input('Enter your monthly expenses:')
Monthly_savings = Monthly_income - Monthly_expenses

Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

print(f'your monthly savings are ${Monthly_savings}')
print(f'Projected savings after one year, with interest, is: ${Projected_savings}.')