import csv
from tkinter import *

import tkinter.messagebox as mb


l=["a","a","r","z","o","o",1,2,3]
ll=["b","ok",1]

ll=ll+l
print(ll)

l2=l.index(1)

abc=2
l[l2]=abc
print(l)


r2=Tk()

def first():
	print("This does basically nothing")

def enter():
	global v,v2
	ent=Toplevel(r2)
	v=Label(ent,text="Name:",font=("times new roman",15,"bold"),bg="purple",fg="white")
	v.place(relx=0,rely=0.3,relheight=0.09,relwidth=0.3)
	v2=Entry(ent,font=("times new roman",15,"bold"))
	v2.place(relx=0.4,rely=0.3,relheight=0.09,relwidth=0.3)
	




menubar=Menu(r2)
menu_items=Menu(menubar)
menu_items.add_command(label="Add",command=enter)
menu_items.add_command(label="View",command=first)

menubar.add_cascade(label="About Us >>", menu=menu_items)

r2.config(menu=menubar)
r2.mainloop()


# Import Required Library
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry("200x530")
root.config(cursor="star")
# List of cursors
cursors =[
		"arrow",
		"circle",
		"clock",
		"cross",
		"dotbox",
		"exchange",
		"fleur",
		"heart",
		"man",
		"mouse",
		"pirate",
		"plus",
		"shuttle",
		"sizing",
		"spider",
		"spraycan",
		"star",
		"target",
		"tcross",
		"trek"
]



# Iterate through all cursors
for cursor in cursors:
	Button(root,text=cursor,cursor=cursor).pack()


# Execute Tkinter
root.mainloop()
