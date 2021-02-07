def volume(x, y, z):

	test = True
	decimal_flag = False;

  	for a in str(x):
		if a.isdigit() == False and (a != '.' or decimal_flag == True):
			test = False;

		elif a == '.' and decimal_flag == False:
			decimal_flag = True;

	
	decimal_flag = False;

  	for b in str(y):
		if b.isdigit() == False and (b != '.' or decimal_flag == True):
			test = False;

		elif b == '.' and decimal_flag == False:
			decimal_flag = True;

	decimal_flag = False;

  	for c in str(z):
		if c.isdigit() == False and (c != '.' or decimal_flag == True):
			test = False;

		elif c == '.' and decimal_flag == False:
			decimal_flag = True;


	if test == True:
		return round((x*y*z),5)

	else:
		return("At least one of your inputs was invalid.")
