travel_distance = float(input("How far is the the place you wanna go (Km): "))
travel_avarege_speed = float(input("What is the avage speed(Km/h): "))

time_travel = travel_distance / travel_avarege_speed
time_travel_minutes = time_travel * 60


print(f"It will take {time_travel} hours to arrive in your destiny.")
print(f"Or {time_travel_minutes} minutes")