"""
In this program we will build a calendar
"""
from time import sleep, strftime

name = "Alex"

calendar = {}

def welcome():
	print "Welcome "+ name
	print "The calendar is opening..."
	sleep(1)
	print "Today is: "+ strftime("%A, %B %d %Y") # day month/day-number/year
	print "The time is: "+ strftime("%H:%M:%S") # hour/minute/second
	sleep(1)

	print "What would you like to do?"

def start_calendar():
	welcome()

	start = True
	while start == True:
		user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
		user_choice = user_choice.upper()

		if user_choice == "V": # user views the calendar
			if len(calendar.keys()) < 1:
				print "The calendar is empty"
			else:
				print calendar

		elif user_choice == "U": # user promts to update the calendar
			date = raw_input("What date? - ")
			update = raw_input("Enter the update: ")
			calendar[date] = update #adding the update to date in the calendar
			print "Update succesful."

		elif user_choice == "A": #user wants to add an event to a certain date
			event = raw_input("Enter event: ")
			date = raw_input("Enter date (MM/DD/YYYY): ")

			if(len(date) > 10 or int(strftime("%Y")) > int(date[6:])): #if date has 10 characters or current year is bigger than the one prompted by the user
				print "Invalid date."
				try_again = raw_input("Try again? Y for Yes, N for No: ")
				try_again = try_again.upper()

				if try_again == "Y":
					continue
				else:
					start = False
			else:
				calendar[date] = event # trebuie bagat un if pentru override

		elif user_choice == "D":
			if len(calendar.keys()) < 1:
				print "The calendar is emtpy!"
			else:
				event = raw_input("What event? - ")
				for date in calendar.keys():
					if event == calender[date]:
						del calendar[date]
						print "Event succesfully deleted."
						print calendar
					else:
						print "Invalid event."
		elif user_choice == "X":
			start = False

		else:
			print "Invalid command."
			start = False

start_calendar()
