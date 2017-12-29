import datetime

def meetup_day(year, month, day_of_the_week, which):


    # which? 1-7 / 8-14 / 15-21 / 22-29 / 29-31 / 13-19
    anchor_date = {
            '1st': 1,
            '2nd': 8,
            '3rd': 15,
            '4th': 22,
            'last': 29,
            'teenth': 13
            }.get(which,-1)

    weekday = {
                'Sunday': 0,
                'Monday': 1,
                'Tuesday': 2,
                'Wednesday': 3,
                'Thursday': 4,
                'Friday': 5,
                'Saturday': 6
                }.get(day_of_the_week,-1)

    first_day_of_week = datetime.datetime(year, month, 1).weekday()

# If Sunday, want Sunday: add 0 (0-0). If Sunday, want Saturday: add 6 (6-0).
# If Wednesday, want Sunday: add 4 (0-3+7). If Wednesday, want Saturday: add 3 (6-3).

    return datetime.date(year, month, anchor_date + (first_day_of_week - weekday + 7) % 7)

