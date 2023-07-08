"""Write a function that converts the time from military to regular format.

Examples


>>> time12hr('1619')
'4:19 p.m.'
>>> time12hr('1200')
'12:00 p.m.'
>>> time12hr('1020')
'10:20 a.m.'
"""

from datetime import datetime

def time12hr(input):
	hours, minutes = int(input[0:2]), int(input[2:4])
	if hours >= 12:
    		afternoon = True
    		hours -= 12
	else:
    		afternoon = False
    	if hours == 0:
        	hours = 12



        return '{hours}:{minutes:02d} {postfix}'.format(
    hours=hours,
    minutes=minutes,
    postfix='p.m.' if afternoon else 'a.m.'
)
