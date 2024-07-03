import datetime
from datetime import datetime

# Find the day of the week:
def find_day_of_week(date_str: str):
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    day = parsed_date.weekday() + 1 
    print("The WeekDay is: ", day)
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Invalid Day")

find_day_of_week("2024-06-27")
find_day_of_week("2024-01-01")
find_day_of_week("2024-07-03")


# Example Test Cases
# Input: "2024-06-27"
# Output: "Thursday"

# Input: "2024-01-01"
# Output: "Monday"