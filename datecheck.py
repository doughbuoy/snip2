import time
from datetime import datetime
from datetime import date

def YMD_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False
    
def YMDS_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%Y/%m/%d").strftime('%Y/%m/%d'):
            raise ValueError
        return True
    except ValueError:
        return False
    
def DMY_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%d-%m-%Y").strftime('%d-%m-%Y'):
            raise ValueError
        return True
    except ValueError:
        return False
    
def DMYS_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime('%d/%m/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False
    

def MDY_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%m-%d-%Y").strftime('%m-%d-%Y'):
            raise ValueError
        return True
    except ValueError:
        return False

def ISO_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S'):
            raise ValueError
        return True
    except ValueError:
        return False 
    
def ISOS_DATE_CHECK(STRING): 
    date_text = STRING
    try:
        if date_text != datetime.strptime(date_text, "%Y/%m/%d %H:%M:%S").strftime('%Y/%m/%d %H:%M:%S'):
            raise ValueError
        return True
    except ValueError:
        return False 
    
def ISOR_DATE_CHECK(STRING): 
    date_text = STRING
    print(STRING)
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%dT%I:%M:%S.%f").strftime('%Y-%m-%dT%I:%M:%S.%f'):
            raise ValueError
        return True
    except ValueError:
        return False 

def diff_dates(date1, date2):
    return abs(date2-date1).days
    
    
if __name__ == '__main__':
    print("START")
    TODAY = date.today()
    print(TODAY)
    TODAYISO = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(TODAYISO)
    now = datetime.today().isoformat()
    print(now)  # '2018-12-05T11:15:55.126382'

    print(DMY_DATE_CHECK('10/10/2012'))
    print(DMYS_DATE_CHECK('10/10/2012'))
    print(YMD_DATE_CHECK('1972-10-20'))
    print(YMD_DATE_CHECK('1972/10/20'))
    print(YMDS_DATE_CHECK('1972/10/20'))

    print(YMDS_DATE_CHECK('1972/02/28'))
    print(ISO_DATE_CHECK('1972/02/28 02:17:22'))
    print(ISOS_DATE_CHECK('1972/02/28 02:17:22'))

    print(ISOR_DATE_CHECK('2025-02-04T04:29:27.277079'))

    d1 = date(2013,1,1)
    d2 = date(2013,9,13)
    result1 = diff_dates(d2, d1)
    print('{} days between {} and {}'.format(result1, d1, d2))
    print("Happy programmer's day!")
    
    YEAR = datetime.today().strftime('%Y')
    MONTH = datetime.today().strftime('%m')
    DAY = datetime.today().strftime('%d')

    
    d1 = date(2025,1,12)
    d2 = date(int(YEAR),int(MONTH),int(DAY))
    result1 = diff_dates(d2, d1)
    print('{} days between {} and {}'.format(result1, d1, d2))
    print("Happy programmer's day!")

   




    
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)	

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = datetime.today().strftime("%Y-%m-%dT%I:%M:%S.%f")
#d = date_time.strftime("%Y-%m-%dT%I:%M:%S.%f")
print("Output 5:", d)