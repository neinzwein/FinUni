from datetime import datetime

def count_days(date1,date2):
    a = datetime.strptime(date1,"%d.%m.%Y")
    b = datetime.strptime(date2,"%d.%m.%Y")
    return (b-a).days
