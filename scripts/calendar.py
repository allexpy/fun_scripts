"""
In this program we will build a calendar
"""
from time import sleep, strftime

name = "Alex"

calendar = {}


def welcome():
	print("Welcome "+ name)
	print("The calendar is opening...")
	sleep(1)
	print("Today is: "+ strftime("%A, %B %d %Y")) # day month/day-number/year
	print("The time is: "+ strftime("%H:%M:%S")) # hour/minute/second
	sleep(1)

	print("What would you like to do?")


def start_calendar():
	welcome()

	start = True
	while start:
		user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
		user_choice = user_choice.upper()

		# user views the calendar
		if user_choice == "V":
			if len(calendar.keys()) < 1:
				print("The calendar is empty")
			else:
				print(calendar)

		# user promts to update the calendar
		elif user_choice == "U":
			date = input("What date? - ")
			update = input("Enter the update: ")
			# adding the update to date in the calendar
			calendar[date] = update
			print("Update succesful.")

		# user wants to add an event to a certain date
		elif user_choice == "A":
			event = input("Enter event: ")
			date = input("Enter date (MM/DD/YYYY): ")

			# if date has 10 characters or current year is bigger than the one prompted by the user
			if len(date) > 10 or int(strftime("%Y")) > int(date[6:]):
				print("Invalid date.")
				try_again = input("Try again? Y for Yes, N for No: ")
				try_again = try_again.upper()

				if try_again == "Y":
					continue
				else:
					start = False
			else:
				calendar[date] = event  # trebuie bagat un if pentru override

		elif user_choice == "D":
			if len(calendar.keys()) < 1:
				print("The calendar is emtpy!")
			else:
				event = input("What event? - ")
				for date in calendar.keys():
					if event == calendar[date]:
						del calendar[date]
						print("Event succesfully deleted.")
						print(calendar)
					else:
						print("Invalid event.")

		elif user_choice == "X":
			start = False

		else:
			print("Invalid command.")
			start = False


if __name__ == "__main__":
	start_calendar()
