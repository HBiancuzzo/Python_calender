def time_valid(time):
    if ':' in time:
        hour, minute = time.split(':')
        if number_valid(hour, 0, 24) and number_valid(minute, 0, 60):
            return True
    return False


def date_valid(date):
    num_day_of_month = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
        4: 30, 6: 30, 9: 30, 11: 30,
        2: 28
    }
    if '/' in date:
        month, day = date.split('/')
        if number_valid(month, 0, 12):
            if number_valid(day, 0, num_day_of_month[int(month)]):
                return True
    return False


def span_valid(span, time):
    if number_valid(span, 0, 1439) and time_valid(time):
        minute = int(span) + int(time.split(':')[1]) + 60 * int(time.split(':')[0])
        if minute < 1439:
            return True
    return False


def number_valid(num, minimum, maximum):
    try:
        if minimum < int(num) <= maximum:
            return True
        else:
            return False
    except ValueError:
        return False


