def convert_to_24_hour_format(time_12):
    time_part, period = time_12.split()
    hours, minutes = map(int, time_part.split(':'))
    if period == 'AM':
        if hours == 12:
            hours_24 = 0  
        else:
            hours_24 = hours
    else:  
        if hours == 12:
            hours_24 = 12  
        else:
            hours_24 = hours + 12
    formatted_hours = f'{hours_24:02}'
    formatted_minutes = f'{minutes:02}'
    return f'{formatted_hours}:{formatted_minutes}'
time_12 = input().strip()
print(convert_to_24_hour_format(time_12))
