days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("seconds: "))

total_seconds_seconds = seconds
total_seconds_minutes = minutes * 60 
total_seconds_hours = hours * 60 * 60
total_seconds_days = days * 24 * 60 * 60

total_seconds = total_seconds_days + total_seconds_hours + total_seconds_minutes + total_seconds_seconds

print(f"segundos totais: {total_seconds}")