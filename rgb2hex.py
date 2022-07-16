def rgb_hex():
	invalid_msg = "Invalid mesage"
  
	#for red
	red = int(raw_input("Enter a red value: "))
	if red < 0 or red > 255:
		print "Invalid value has been entered."
		return
  
	#for green
	green = int(raw_input("Enter a green value: "))
	if green < 0 or green > 255:
		print "Invalid value has been entered."
		return
  
	#for blue
	blue = int(raw_input("Enter a blue value: "))
	if blue < 0 or blue > 255:
		print "Invalid value has been entered."
		return
	
	val = (red << 16) + (green << 8) + blue
	print "%s" % (hex(val)[2:]).upper()
  
def hex_rgb():
  
	hex_val = raw_input("Enter a hexadecimal value: ")
	if len(hex_val) != 6:
		print "Invalid value has been entered."
		return
  
	else:
		hex_val = int(hex_val, 16)
  
	#blue
	two_hex_digits = 2 ** 8
	blue = hex_val % two_hex_digits
	hex_val = hex_val >> 8
  
	#green
	green = hex_val % two_hex_digits
	hex_val = hex_val >> 8
  
	red = hex_val % two_hex_digits
	print "Red: %s, Blue: %s, Green: %s" % (red, blue, green)
  
def convert():
	x = True
	while x == True:
		option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB: ")
    
		if option == '1':
			print "RGB to HEX..."
			rgb_hex()
		elif option == '2':
			print "HEX to RGB..."
		elif option == 'X' or option == 'x':
			break
		else:
			print "Error."
convert()
