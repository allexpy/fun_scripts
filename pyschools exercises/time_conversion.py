"""
12hr To 24hr Time Conversion

Write a function that converts the time to 24hr format.

Examples

>>> time24hr('12:34am')
'0034hr'
>>> time24hr('12:15pm')
'1215hr'

"""

from datetime import datetime
def time24hr(tstr):
	the_time = datetime.strptime(tstr, "%I:%M%p")
	out_time = datetime.strftime(the_time, "%H%Mhr")
	return out_time
