import datetime

def convert_string2datetime(datetime_string, format):
    try:
        date_time_obj = datetime.datetime.strptime(datetime_string, format)
    except ValueError:
        print('Incorrect format. Required format', format)
    else:
        return date_time_obj


def convert_datetime2string(date_time_obj, format):
    try:
        datetime_string = date_time_obj.strftime(format)
    except ValueError:
        print('Incorrect format. Required format', format)
    else:
        return datetime_string


def calc_time_difference(date_time_obj1, date_time_obj2):
    date_time_difference = date_time_obj2 - date_time_obj1
    return date_time_difference
