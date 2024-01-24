import sqlite3
from database import *
from normal import *


conn = sqlite3.connect("travel.db")
cur = conn.cursor()

data = """CREATE TABLE if not exists travel(id varchar(20),
	name varchar(50),phone int , no_car int, no_day int , bill int)"""
cur.execute(data)     # database create only one time 

no_of_car = 20-total_car()

def rent():  # car rent function
	global no_of_car
	term()
	y_n = input("yes / no : ")
	if y_n == "yes":
		try:
				no_car = int(input("enter no of car : "))
				if no_car <= no_of_car :
					no_day = int(input("enter no of day : "))
					name = input("enter name : ")
					id_no  = input("enter your id : ")
					phone  = int(input("enter your no : "))
					bill = no_car*no_day*500
					print("your bill : ",bill)
					y = input("enter y/n : ")
					if y == "y":
						print(" Booked : ")
						bill_gen(name,phone,id_no,no_day,no_car,bill)
						data_insert(id_no,name,phone,no_car,no_day,bill)
						no_of_car = no_of_car - no_car
						return
					else :
						print("thank you : ")
						return
				else :
					print("ins : ")
					return	
		except Exception as e:
			print(e)
			return
	else :
		print("thank you : ")
		return 



def dep(): # car deposit function 
	global no_of_car
	id_no = input("enter your id : ")
	if id_no in id_get() :
		try:
				no_car = int(input("enter no of car : "))
				p = data_select(id_no)
				if no_car == p :
					data_del(id_no)
					no_of_car = no_of_car + no_car
					print("thank you : ")
					return
				elif no_car < p :
					new_car_no = p - no_car
					car_update(id_no,new_car_no)
					no_of_car = no_of_car + no_car
					print("thank you : ")
					return
				else :
					print("wrong input : ")
					return
		except Exception as e:
			print(e)
			return
	else :
		print("wrong id : ")
		return

if __name__ == '__main__':	
		print(" : welcome to wscube Travel : ")
		while True :
			print("total no of car : ",no_of_car)
			print("""
1.	Rent
2.	Deposit
3.	Exit : """)
			print()
			var = input("enter your no : ")
			if var == "1":
				rent()
			elif var == "2":
				dep()
			elif var == "3":
				print("thank you : ")
				break
			else :
				print("wrong input : ")
