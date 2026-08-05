import calendar

# Get input from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Print the calendar of the given month
print("\n", calendar.month(year, month))