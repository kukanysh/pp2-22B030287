#task1
from datetime import datetime, timedelta
today = datetime.now()
def subt(date, days):
    return date - timedelta(days=days)
print(f'The date is: {subt(today, 5)}')

#task2
from datetime import datetime, timedelta
today = datetime.now()
def yesterday(date, days):
    return date - timedelta(days=days)
def tomorrow(date, days):
    return date + timedelta(days=days)
print(f'Yesterday was: {yesterday(today, 1)}')
print(f'Today is: {today}')
print(f'Tomorrow is: {tomorrow(today, 1)}')

#task3
from datetime import datetime
def drop_micro(dt):
    return dt.replace(microsecond=0)
today = datetime.now()
print(drop_micro(today))

#task4
from datetime import datetime
d1 = datetime(2023, 12, 4)
d2 = datetime(2022, 5, 26)
def diff(d1, d2):
    dif = d1 - d2
    return dif.total_seconds()
print(f'The difference in seconds is: {diff(d1, d2)} seconds')
