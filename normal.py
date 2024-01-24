def term():  # terms and conditions
	print("""
		1.  One Car for One Day : 500/-
		2.  Aadhar Card is Mandatory
		3.  Driving Licence is  Mandatory: """)


def bill_gen(*x): # bill generate in  txt 
	bill = f"""
: Welcome to Wscube Travel : 
Name 	  : {x[0]}
Phone     : {x[1]}
Id No     : {x[2]}
No of Day : {x[3]}
No of Car : {x[4]}
Bill 	  : {x[5]}
Car Booked
"""
	bill_name  = x[0]+".txt"
	p = open(bill_name,"w")
	p.write(bill)
	p.close()