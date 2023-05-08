import calendar

# Function to display calendar
def display_calendar(year, month):
    # Display the calendar header
    print(calendar.month_name[month], year)
    print("-----------------------------")
    
    # Get the calendar for the given year and month
    cal = calendar.monthcalendar(year, month)
    
    # Display the days of the week
    print(" Sun  Mon  Tue  Wed  Thu  Fri  Sat")
    
    # Display each week's row
    for week in cal:
        for day in week:
            # If it's a valid day, display it. Otherwise, display a blank space.
            if day != 0:
                print(f" {day:2d} ", end="")
            else:
                print("     ", end="")
        print()  # Move to the next line for the next week

# Get input from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Call the function to display the calendar
display_calendar(year, month)
