class BankAccount(object):
	"""making a bank account with details"""
	balance = 0
  
	def __init__(self, name):
		self.name = name
    
	def __repr__(self):
		return "The account belongs to: %s \
		Your balance: %.2f" % (self.name, self.balance)
  
	def show_balance(self):
		print "Your balance is: %.2f" % (self.balance)
    
	def deposit(self, amount):
		if amount < 0:
			print "That doesn't make sense."
			return
		else:
			print "You are depositing: %.2f" % (amount)
			self.balance += amount
			self.show_balance()
      
	def withdraw(self, amount):
		if amount > self.balance:
			print "You don't have enough money!"
			return
		else:
			print "You are withdrawing %.2f" % (amount)
			self.balance -= amount
			self.show_balance()
      
my_account = BankAccount("Alex")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
