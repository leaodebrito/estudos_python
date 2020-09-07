traveled_km = float(input("How many kilometers were traveled: "))
rent_days = int(input("How many days the car were rented: "))

traveled_km_value = traveled_km * 0.15
rent_days_value = rent_days * 60

total_bill = traveled_km_value + rent_days_value

print(f"You bill is R${total_bill:5.2f}")