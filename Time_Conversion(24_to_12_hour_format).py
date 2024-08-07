def convert_to_12_hour_format(time_24):
    hours, minutes = map(int, time_24.split(':'))
    if hours == 0:
        period = 'AM'
        hours_12 = 12
    elif hours < 12:
        period = 'AM'
        hours_12 = hours
    elif hours == 12:
        period = 'PM'
        hours_12 = 12
    else:
        period = 'PM'
        hours_12 = hours - 12
    formatted_hours = f'{hours_12:02}'
    formatted_minutes = f'{minutes:02}'
    return f'{formatted_hours}:{formatted_minutes} {period}'
time_24 = input().strip()
print(convert_to_12_hour_format(time_24))
