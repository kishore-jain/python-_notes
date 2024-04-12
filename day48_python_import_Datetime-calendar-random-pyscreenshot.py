Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# datetime
# --------

import datetime

datetime.datetime.now()
datetime.datetime(2023, 12, 13, 11, 13, 34, 975699)
print(datetime.datetime.now())
2023-12-13 11:14:19.349149

print(datetime.datetime.now().strftime('%a'))
Wed
print(datetime.datetime.now().strftime('%A'))
Wednesday
print(datetime.datetime.now().strftime('%b'))
Dec
print(datetime.datetime.now().strftime('%B'))
December
print(datetime.datetime.now().strftime('%c'))
Wed Dec 13 11:17:32 2023
>>> import time
>>> 
>>> time.asctime()
'Wed Dec 13 11:18:06 2023'
>>> # it is same of asctime & datetime
>>> 
>>> 
>>> print(datetime.datetime.now().strftime('%C'))
20
>>> # c mean century
>>> 
>>> print(datetime.datetime.now().strftime('%d'))
13
>>> print(datetime.datetime.now().strftime('%D'))
12/13/23
>>> print(datetime.datetime.now().strftime('%e'))
13
>>> print(datetime.datetime.now().strftime('%E'))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(datetime.datetime.now().strftime('%E'))
ValueError: Invalid format string
>>> print(datetime.datetime.now().strftime('%f'))
603159
>>> # f means micro second
>>> print(datetime.datetime.now().strftime('%g'))
23
>>> print(datetime.datetime.now().strftime('%G'))
2023
print(datetime.datetime.now().strftime('%h'))
Dec
print(datetime.datetime.now().strftime('%H'))
11
print(datetime.datetime.now().strftime('%i'))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(datetime.datetime.now().strftime('%i'))
ValueError: Invalid format string
print(datetime.datetime.now().strftime('%I'))
11

# H --> 24 hours format
# I --> 12 hours format

print(datetime.datetime.now().strftime('%j'))
347
# no fo days

print(datetime.datetime.now().strftime('%m'))
12
print(datetime.datetime.now().strftime('%M'))
26
print(datetime.datetime.now().strftime('%M'))
26

print(datetime.datetime.now().strftime('%p'))
AM
print(datetime.datetime.now().strftime('%s'))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(datetime.datetime.now().strftime('%s'))
ValueError: Invalid format string
print(datetime.datetime.now().strftime('%S'))
51
print(datetime.datetime.now().strftime('%r'))
11:28:17 AM
print(datetime.datetime.now().strftime('%R'))
11:28
print(datetime.datetime.now().strftime('%u'))
3
print(datetime.datetime.now().strftime('%U'))
50
print(datetime.datetime.now().strftime('%w'))
3
print(datetime.datetime.now().strftime('%W'))
50
print(datetime.datetime.now().strftime('%x'))
12/13/23
print(datetime.datetime.now().strftime('%X'))
11:30:10
print(datetime.datetime.now().strftime('%y'))
23
print(datetime.datetime.now().strftime('%Y'))
2023
print(datetime.datetime.now().strftime('%z'))

print(datetime.datetime.now().strftime('%Z'))

 # z not have datetime
 


# Calender
# --------

import calendar


calendar.month(2023,12)
'   December 2023\nMo Tu We Th Fr Sa Su\n             1  2  3\n 4  5  6  7  8  9 10\n11 12 13 14 15 16 17\n18 19 20 21 22 23 24\n25 26 27 28 29 30 31\n'

print(calendar.month(2023,12))
   December 2023
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31


print(calendar.calendar(2023))
                                  2023

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31

print(calendar.isleap(2020))
True
print(calendar.isleap(2021))
False
print(calendar.isleap(2022))
False
print(calendar.isleap(2023))
False
print(calendar.isleap(2024))
True

print(calendar.leapdays(2000,2023))# 2000,2004,2008,2012,2016,2020
6
cal = calendar.HTMLCalendar(firstweekday=0)
print(cal.formatmonth(2023,12,withyear=True))
<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">December 2023</th></tr>
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td><td class="sun">3</td></tr>
<tr><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class="sun">10</td></tr>
<tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td></tr>
<tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>
<tr><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td><td class="sun">31</td></tr>
</table>

# HTML calendar formate


# program to print sunday of year 2023

import datetime
for week in range(53):
    print(datetime.datetime.strftime('2023'+str(week)+'0','%Y%W%w'))

    
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    print(datetime.datetime.strftime('2023'+str(week)+'0','%Y%W%w'))
TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'str' object


for week in range(53):
    print(datetime.datetime.strptime('2023'+str(week)+'0','%Y%W%w'))

    
2023-01-01 00:00:00
2023-01-08 00:00:00
2023-01-15 00:00:00
2023-01-22 00:00:00
2023-01-29 00:00:00
2023-02-05 00:00:00
2023-02-12 00:00:00
2023-02-19 00:00:00
2023-02-26 00:00:00
2023-03-05 00:00:00
2023-03-12 00:00:00
2023-03-19 00:00:00
2023-03-26 00:00:00
2023-04-02 00:00:00
2023-04-09 00:00:00
2023-04-16 00:00:00
2023-04-23 00:00:00
2023-04-30 00:00:00
2023-05-07 00:00:00
2023-05-14 00:00:00
2023-05-21 00:00:00
2023-05-28 00:00:00
2023-06-04 00:00:00
2023-06-11 00:00:00
2023-06-18 00:00:00
2023-06-25 00:00:00
2023-07-02 00:00:00
2023-07-09 00:00:00
2023-07-16 00:00:00
2023-07-23 00:00:00
2023-07-30 00:00:00
2023-08-06 00:00:00
2023-08-13 00:00:00
2023-08-20 00:00:00
2023-08-27 00:00:00
2023-09-03 00:00:00
2023-09-10 00:00:00
2023-09-17 00:00:00
2023-09-24 00:00:00
2023-10-01 00:00:00
2023-10-08 00:00:00
2023-10-15 00:00:00
2023-10-22 00:00:00
2023-10-29 00:00:00
2023-11-05 00:00:00
2023-11-12 00:00:00
2023-11-19 00:00:00
2023-11-26 00:00:00
2023-12-03 00:00:00
2023-12-10 00:00:00
2023-12-17 00:00:00
2023-12-24 00:00:00
2023-12-31 00:00:00



# printing all sundays of 2023 using calendar module

import calendar
dayofweek=0
maxweeks = 52

for d in get_all_dates_of_day_of_week_in_year(dayofweek,2023,1,1,maxweeks):
    print("%s,%d/%d/%d" % (calendar.day_name[d.weekday()],d.year,d.month,d.day))

    
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    for d in get_all_dates_of_day_of_week_in_year(dayofweek,2023,1,1,maxweeks):
NameError: name 'get_all_dates_of_day_of_week_in_year' is not defined


# 3rd way
# -------

import calendar
from datetime import date
year = 2023
c = calendar.Textcalendar(calendar.sundaya)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    c = calendar.Textcalendar(calendar.sundaya)
AttributeError: module 'calendar' has no attribute 'Textcalendar'. Did you mean: 'TextCalendar'?



# random
# ======

import random

random.Random()
<random.Random object at 0x000002663E049820>
random.random()
0.7948455312402267
random.random()
0.6131265930690417
random.random()
0.6402129820144599

random.randint(1000,3000)
1204
random.randint(1000,3000)
1167
random.randint(1000,3000)
2062
random.randint(1000,3000)
1515
# random mean orderless(unorder)

random.randrange(10000,20000)
13861
random.randrange(10000,20000)
11960
random.randrange(10000,20000)
18707


# pyscreenshot
# -------------
import pyscreenshot

============================ RESTART: C:/Python310/screenshot _day1.py ============================

============================ RESTART: C:/Python310/screenshot _day1.py ============================
