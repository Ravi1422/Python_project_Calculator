# all database work 

import sqlite3

conn = sqlite3.connect("travel.db")
cur = conn.cursor()

def total_car():   # total no of car go to rent 
	data = "SELECT no_car FROM travel"
	car = cur.execute(data)
	t = []
	for i in car:
		t.append(i[0])
	return sum(t)


def data_insert(*x): #  customer data entry 
	data = """INSERT INTO travel VALUES (?,?,?,?,?,?)"""
	cur.execute(data,x)
	conn.commit()

def id_get():  # id chack ( id get )
	data = "SELECT id from travel"
	var = cur.execute(data)
	id_data = []
	for i in var:
		id_data.append(i[0])

	return id_data 

def data_select(x): # only one id data get 
	no_car = 0
	data = """SELECT no_car FROM travel WHERE id = ? """
	var = cur.execute(data,(x,))
	for i in var:
		no_car = i[0]
	return no_car

def car_update(x,y): # no of car update 
	print("test 1")
	data = "UPDATE travel set no_car = ? WHERE id = ?"
	print("test 2")
	cur.execute(data,(y,x))
	conn.commit()
	print("test 3")

def data_del(x):  # all car deposit than data delete
	data = 'DELETE FROM travel WHERE id = ?'
	cur.execute(data,(x,))
	conn.commit()