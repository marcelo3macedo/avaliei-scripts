from datetime import datetime, timedelta

def get_first_and_last_day_of_month(input_date_str):
    """
    Returns the first and last day of the month for a given input date string in 'mm/yyyy' format.

    Parameters:
    - input_date_str: A string representing a date in 'mm/yyyy' format.

    Returns:
    - A tuple of datetime objects: (first_day_of_month, last_day_of_month)
    """
    # Parse the input date to get the month and year
    date_obj = datetime.strptime(input_date_str, "%m/%Y")

    # First day of the month is always 1
    first_day = date_obj.replace(day=1)

    # Last day of the month can be found by subtracting one day from the first day of the next month
    if date_obj.month == 12:
        # If the month is December, increment the year for the next month
        next_month = date_obj.replace(month=1, year=date_obj.year + 1)
    else:
        next_month = date_obj.replace(month=date_obj.month + 1)

    # Subtract one day from the first day of the next month to get the last day of the current month
    last_day = next_month - timedelta(days=1)

    return first_day, last_day