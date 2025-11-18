from datetime import datetime, timedelta


def display_current_datetime(): 
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
    future_date = input('Enter the number of days to add to the current date: ')
    if type(int(future_date)) == int:
        calculated_date = timedelta(days=int(future_date))
        calculate_future_date = calculated_date + current_date
        print(calculate_future_date)

display_current_datetime()
