daily_cigarretes_amount = int(input("How many cigarretes do you smoke in one day: "))
years_smoking_cigarretes = float(input("how long do you smoke: "))

days_smoke_total = years_smoking_cigarretes * 365
total_cigarretes = days_smoke_total * daily_cigarretes_amount

minutes_lost = total_cigarretes * 10

minutes_day = 24*60

total_days_lost = minutes_lost / minutes_day
total_years_lost = total_days_lost / 365


print(f" You already lost {total_days_lost:5.2f}, sucker.")
print(f"or {total_years_lost:5.2f} years")