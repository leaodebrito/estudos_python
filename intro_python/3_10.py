salary_original = float(input("How much is the salary: "))
increase_salary = float(input("How much is the increase(%) on the salary: "))

increase_amount = salary_original * (increase_salary / 100)

new_salary = increase_amount + salary_original

print(f"Congrats, you're receiveing more R${increase_amount:5.2f} this month")
print(f"Your salary is R${new_salary:5.2f}")