def is_leap_year(year):
    if(not year%400):
        return True
    if(not year%100):
        return False
    if(year%4):
        return False
    return True
