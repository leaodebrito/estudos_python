original_value = float(input("How much is the item's cost: "))
discount = float(input("How much is the discount(%) on the product: "))

discount_value = original_value * (discount / 100)

price_after_discount = original_value - discount_value 

print(f"Congrats, you're receiveing more R${discount_value:5.2f} this month")
print(f"Your salary is R${price_after_discount:5.2f}")