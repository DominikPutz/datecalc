import datetime

# constants
Format = '[YYYY-MM-DD HH:MM:SS]'

# functions
def read_date():
    print('Input date and time', Format)
    # User should input until valid format
    while True:
        try:
            datetime_string = input()
            date_time_obj = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # strptime raised an error -> incorrect format -> Try again
            print('Incorrect format. Required format', Format)
            continue
        else:
            # string was successfully parsed -> exit the loop
            return date_time_obj


def calc_time_difference(date_time_obj1, date_time_obj2):
    date_time_difference = date_time_obj2 - date_time_obj1
    return date_time_difference


# General multi_output
date_time_obj = datetime.datetime.now()
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())

# Fetching 2 datetimes
date_time_obj1 = read_date()
date_time_obj2 = read_date()

# calculate time difference
date_time_difference = calc_time_difference(date_time_obj1, date_time_obj2)
print('Difference:', date_time_difference)
