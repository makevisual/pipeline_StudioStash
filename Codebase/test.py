import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract day, month, and year from the current date
day = current_datetime.day
month = current_datetime.month
year = current_datetime.year

# Print the values
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")