from tkinter import *                     
import tkinter.messagebox as mb           
from PIL import ImageTk,Image
import csv
from random import *

global root

root=Tk()
root.iconbitmap("impo.ico")
root.title("ARMY")
root.geometry("1500x700+0+0")

ph=PhotoImage(file= "main_win3.png")

l=Label(root,image=ph)
l.place(relx=0,rely=0.3,relheight=0.7,relwidth=1)

f1main=Frame(root,bg="purple")
f1main.place(relheight=0.3,relwidth=1)

f2main=Frame(root,bg="orange")
f2main.place(relx=0,rely=0.03,relheight=0.067,relwidth=1)
label3_main=Label(f2main,text="Peace Through Strength!",font=('Harlow Solid Italic',25,'normal'),bg="orange",fg="white")
label3_main.place(relx=0.001,rely=0,relheight=1,relwidth=1)

label_main=Label(f1main,text="The Indian Army",font=('Goudy Stout',49,'normal'),bg="purple",fg="white",compound=LEFT)
label_main.place(relx=0,relheight=1,relwidth=1)

label2_main=Label(f1main,text="Extending Our Service To Mother India Forever...",font=('Harlow Solid Italic',25,'normal'),bg="green",fg="white")
label2_main.place(relx=0.001,rely=0.7,relheight=0.2,relwidth=1)

but1=Button(root,text="JOIN MILITARY",height=2,width=10,font=('garamond',22,'bold'),cursor="hand2",command= lambda:[join()],relief=GROOVE,bg="purple",fg="white")
but1.place(relx=0.08,rely=0.8,relheight=0.13,relwidth=0.2)

but2=Button(root,text="LOGIN",height=2,width=10,font=('garamond',22,'bold'),cursor="hand2",command=lambda:[train()],relief=RIDGE,bg="purple",fg="white")
but2.place(relx=0.38,rely=0.8,relheight=0.13,relwidth=0.2)
 
but3=Button(root,text="MORE INFO",height=2,width=10,font=('garamond',22,'bold'),command=lambda:[more_info()],relief=GROOVE,bg="purple",fg="white",cursor="hand2")
but3.place(relx=0.7,rely=0.8,relheight=0.13,relwidth=0.2)	
	
but13=Button(root,text="Personnels' Section",height=1,width=10,font=('garamond',22,'bold'),command=lambda:[personnel()],relief=GROOVE,bg="purple",fg="white",cursor="hand2")
but13.place(relx=0.75,rely=0.3,relheight=0.05,relwidth=0.2)

def save(obj):
	with open("entry.csv", "a") as f:
		write=csv.writer(f,lineterminator="\n")
		write.writerow(obj)


def join():
	
	global root2,bg,join_img,img_j
	
	root2=Toplevel(root)
	root2.geometry("1000x650+200+0")
	root2.title("JOIN")
	root2.iconbitmap("lieut.ico")

	img_j=ImageTk.PhotoImage(file="join_s.png")
	join_img=ImageTk.PhotoImage(file="join.png")
	j_l=Label(root2,image=join_img)
	j_l.place(relheight=1,relwidth=1)
	frame_j=Frame(root2,bd=5,borderwidth=1,relief=GROOVE)
	frame_j.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
	jf_tl=Label(frame_j,image=img_j)
	jf_tl.place(relheight=1,relwidth=1)

	join_head=Label(frame_j,text="REGISTER",font=('goudy Stout',45,'bold'),fg='purple')
	join_head.place(relx=0.08,rely=0.06,relheight=0.3,relwidth=0.85)

	name = Entry(frame_j,font=('Perpetua',17,'normal'))
	name_label = Label(frame_j, text = 'Name :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	name.place(relx=0.4301,rely=0.353,relheight=0.06,relwidth=0.5)
	name_label.place(relx=0.08,rely=0.353,relheight=0.06,relwidth=0.35)
	
	age = Entry(frame_j,font=('Perpetua',17,'normal'))
	age_label = Label(frame_j, text = 'Age :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	age.place(relx=0.4301,rely=0.41,relheight=0.06,relwidth=0.5)
	age_label.place(relx=0.08,rely=0.41,relheight=0.06,relwidth=0.35)

	gen = Entry(frame_j,font=('Perpetua',17,'normal'))
	gen_label = Label(frame_j, text = 'Gender M F O :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	gen.place(relx=0.4301,rely=0.467,relheight=0.06,relwidth=0.5)
	gen_label.place(relx=0.08,rely=0.467,relheight=0.06,relwidth=0.35)

	dob = Entry(frame_j,font=('Perpetua',17,'normal'))
	dob_label = Label(frame_j, text = 'D.O.B :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	dob.place(relx=0.4301,rely=0.524,relheight=0.06,relwidth=0.5)
	dob_label.place(relx=0.08,rely=0.524,relheight=0.06,relwidth=0.35)

	f_name = Entry(frame_j,font=('Perpetua',17,'normal'))
	f_name_label = Label(frame_j, text = 'Father Name :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	f_name.place(relx=0.4301,rely=0.581,relheight=0.06,relwidth=0.5)
	f_name_label.place(relx=0.08,rely=0.581,relheight=0.06,relwidth=0.35)

	m_name = Entry(frame_j,font=('Perpetua',17,'normal'))
	m_name_label = Label(frame_j, text = 'Mother Name :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	m_name.place(relx=0.4301,rely=0.638,relheight=0.06,relwidth=0.5)
	m_name_label.place(relx=0.08,rely=0.638,relheight=0.06,relwidth=0.35)

	ht = Entry(frame_j, font=('Perpetua',17,'normal'))
	ht_label = Label(frame_j, text = 'Height(in cm) :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	ht.place(relx=0.4301,rely=0.695,relheight=0.06,relwidth=0.5)
	ht_label.place(relx=0.08,rely=0.695,relheight=0.06,relwidth=0.35)

	wt = Entry(frame_j,font=('Perpetua',17,'normal'))
	wt_label = Label(frame_j, text = 'Weight(in kgs) :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	wt.place(relx=0.4301,rely=0.752,relheight=0.06,relwidth=0.5)
	wt_label.place(relx=0.08,rely=0.752,relheight=0.06,relwidth=0.35)

	ph = Entry(frame_j,font=('Perpetua',17,'normal'))
	ph_label = Label(frame_j, text = 'Phone no. :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	ph.place(relx=0.4301,rely=0.809,relheight=0.06,relwidth=0.5)
	ph_label.place(relx=0.08,rely=0.809,relheight=0.06,relwidth=0.35)

	def check2():
		global l1,img4,l_log
		
		b=randrange(1,10000)
		a="@Tid"+ str(b)
		
		name1 = name.get()
		dob2 = dob.get()
		age1 = age.get()
		f_name1 = f_name.get()
		m_name1 = m_name.get()
		height1 = ht.get()
		weight1 = wt.get()
		phn_no1 = ph.get()
		gen1=gen.get()

		l1=[name1,age1,gen1,dob2,f_name1,m_name1,height1,weight1,phn_no1,a,b]
		save(l1)

		name.delete(0,END)
		dob.delete(0,END)
		age.delete(0,END)
		f_name.delete(0,END)
		m_name.delete(0,END)
		ht.delete(0,END)
		wt.delete(0,END)
		ph.delete(0,END)
	
		root2.lift()
		root2.title("LOGIN DETAILS")
		root2.geometry('400x200+500+250')
		root2.iconbitmap("impo.ico")

		log_dtl=Frame(root2)
		log_dtl.place(relheight=1,relwidth=1)
		
		img4=ImageTk.PhotoImage(file="log_dtail.png")
		l_log=Label(log_dtl,image=img4)
		l_log.place(relheight=1,relwidth=1)
		
		
		def des():
			root2.destroy()
			join()

		f_login=Frame(log_dtl,bg="white")
		f_login.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
		
		
		l2=Label(f_login,text=a,font = ('Perpetua',12,'bold')) 
		l2.place(relx=0.45,rely=0.2,relheight=0.15,relwidth=0.3)
		
		l_l=Label(f_login,text="USERNAME:",font = ('Perpetua',12,'bold'),bg="purple",fg="white")
		l_l.place(relx=0.1,rely=0.2,relheight=0.15,relwidth=0.35)
		
		l=Label(f_login,text=b,font = ('Perpetua',12,'bold'))
		l.place(relx=0.45,rely=0.5,relheight=0.15,relwidth=0.35)

		l2_l=Label(f_login,text="PASSWORD:",font = ('Perpetua',12,'bold'),bg="purple",fg="white") 
		l2_l.place(relx=0.1,rely=0.5,relheight=0.15,relwidth=0.35)
		
		but3=Button(log_dtl,text="OK",font = ('Perpetua',12,'bold'),command=des)
		but3.place(relx=0.32,rely=0.7,relheight=0.12,relwidth=0.35)
		
		root2.mainloop()
	
	def check1():
		if (name.get()=="" or  age.get()=="" or dob.get()=="" or f_name.get()=="" or m_name.get()==""or ht.get()=="" or wt.get()=="" or ph.get()==""):
			mb.showerror("Error", "All fields need to be entered!")
		else:
			mb.showinfo("Status", "Registration Successful! \nYou will receive your UserId and Password shortly...")
			check2()

	buta=Button(frame_j,text="Enter",font=('garamond',15,'bold'),command=check1,bg="purple",fg="white")
	buta.place(relx=0.35,rely=0.89,relheight=0.1,relwidth=0.3)   

def train():
	global l2,l3,img2,imgt,tl_screen
	tl_screen=Toplevel(root)
	tl_screen.title("Trainee's Login")
	tl_screen.iconbitmap("lieut.ico")
	tl_screen.geometry("550x250+400+170")

	img2=ImageTk.PhotoImage(file="login.png")
	l_itl=Label(tl_screen,image=img2)
	l_itl.place(relheight=1,relwidth=1)

	f_tl=Frame(tl_screen)
	f_tl.place(relx=0.06,rely=0.13,relheight=0.7,relwidth=0.9)

	imgt=ImageTk.PhotoImage(file="tl_s.png")
	lf_tl=Label(f_tl,image=imgt)
	lf_tl.place(relheight=1,relwidth=1)

	l_tl=Label(f_tl,text="Enter Trainee_id:",font=('garamond',12,'bold'),bg="purple",fg="white")
	l_tl.place(relx=0.06,rely=0.13,relwidth=0.355,relheight=0.2)
	l2=Entry(f_tl,font=('garamond',12,'bold'))
	l2.place(relx=0.55,rely=0.13,relwidth=0.4,relheight=0.2)

	l3_l=Label(f_tl,text="Enter Trainee_password:",font=('garamond',12,'bold'),bg="purple",fg="white")
	l3_l.place(relx=0.0235,rely=0.5,relwidth=0.5,relheight=0.2)
	l3=Entry(f_tl,font=('garamond',12,'bold'))
	l3.place(relx=0.55,rely=0.5,relwidth=0.43,relheight=0.2)

	but3=Button(f_tl,text="Enter",font=('garamond',20,'bold'),fg="white",bg="purple",command=lambda:[search(l2.get(),l3.get())],relief=RIDGE)
	but3.place(relx=0.35,rely=0.75,relwidth=0.3,relheight=0.17)

	but_ftl=Button(tl_screen,text="Forgot Password?",font=('Courier',10,'bold'),bg="purple",fg="white",command=lambda:[for_pass()])
	but_ftl.place(relx=0.27,rely=0.89,relwidth=0.43,relheight=0.095)

def search(obj1,obj2):
	with open("entry.csv","r") as f:
		read=csv.reader(f)

		c=0
		for i in read:
			for j in range(len(i)):
				if i[j]==obj1 or i[j]==obj2:
					c=c+1
				else:
					pass
		if c==2:
			mb.showinfo("Login status","Record exists!")
			user_win()
		else:
			mb.showerror("Login Status","Invalid Id or Password!")
			l2.delete(0,END)
			l3.delete(0,END)
			tl_screen.lift()

def for_pass():
	global l_for_e,l_for2_e

	tl_screen.geometry("550x300+400+170")
	tl_screen.iconbitmap("lieut.ico")
	tl_screen.title("Forgot Password")

	frame_pas=Frame(tl_screen,bg="purple")
	frame_pas.place(relheight=1,relwidth=1)

	l_for=Label(frame_pas,text="Enter your name:",font=('garamond',12,'bold'))
	l_for_e=Entry(frame_pas,font=('garamond',12,'bold'))
	l_for.place(relx=0.06,rely=0.15,relwidth=0.43,relheight=0.15)
	l_for_e.place(relx=0.53,rely=0.15,relwidth=0.43,relheight=0.15)

	l_for2=Label(frame_pas,text="Enter your date of birth:",font=('garamond',12,'bold'))
	l_for2_e=Entry(frame_pas,font=('garamond',12,'bold'))
	l_for2.place(relx=0.06,rely=0.45,relwidth=0.43,relheight=0.15)
	l_for2_e.place(relx=0.53,rely=0.45,relwidth=0.43,relheight=0.15)

	but12=Button(tl_screen,text="Enter",font=('garamond',12,'bold'),command=lambda:[for_pass_chk(l_for_e.get(),l_for2_e.get())])
	but12.place(relx=0.25,rely=0.7,relwidth=0.43,relheight=0.15)

def for_pass_chk(obj4,obj5):
	with open("entry.csv","r") as f:
		read3=csv.reader(f)
		o=0
		global c,d
		for i in read3:
			if obj4 in i and obj5 in i:
				o=o+1
				c=i[9]
				d=i[10]
			else:
				pass
		if o==1:
			mb.showinfo("User Status","Record exists!")
			global new_img,l_img
		
			tl_screen.geometry("500x200+430+230")
			tl_screen.iconbitmap("impo.ico")
			tl_screen.config(bg="purple")
			tl_screen.title("LOGIN DETAILS")

			new=Frame(tl_screen)
			new.place(relheight=1,relwidth=1)
			tl_screen.lift()
			
			new_img=ImageTk.PhotoImage(file="new.png")
			l_img=Label(new,image=new_img)
			l_img.place(relheight=1,relwidth=1)
			l_new=Label(new,text="Trainee Id:",font=('garamond',12,'bold'),bg="purple",fg="white",)
			l_new.place(relx=0.13,rely=0.17,relwidth=0.43,relheight=0.15)
			l_new2=Label(new,text=''+c+'',font=('garamond',12,'bold'))
			l_new2.place(relx=0.56,rely=0.17,relwidth=0.25,relheight=0.15)
			l_new3=Label(new,text="Trainee_password:",font=('garamond',12,'bold'),bg="purple",fg="white",)
			l_new3.place(relx=0.13,rely=0.47,relwidth=0.43,relheight=0.15)
			l_new4=Label(new,text=''+d+'',font=('garamond',12,'bold'))
			l_new4.place(relx=0.56,rely=0.47,relwidth=0.25,relheight=0.15)

			but_fpass=Button(new,text="OK",font=('garamond',12,'bold'),command=lambda:[tl_screen.destroy(),train()])
			but_fpass.place(relx=0.45,rely=0.753,relwidth=0.15,relheight=0.1)
		else:
			mb.showerror("User Status","No such record found!")
			l_for_e.delete(0,END)
			l_for2_e.delete(0,END)
			tl_screen.lift()

global user_win

def user_win():
	global user_window,img,img5,img6,f_uw4

	tl_screen.lift()
	tl_screen.geometry("1250x600+85+50")
	tl_screen.title("Trainee")
	tl_screen.iconbitmap("impo.ico")
	
	user_window=Frame(tl_screen)
	user_window.place(relheight=1,relwidth=1)

	tw_op_view(l2.get())
	global n,ag,dob,fn,mn,stat
	n=l1[0]
	ag=l1[1]
	dob=l1[3]
	fn=l1[4]
	mn=l1[5]
	stat="CONFIRMED"

	f_uw3=Frame(user_window,bg="purple")
	f_uw3.place(relx=0,rely=0,relheight=0.3,relwidth=1)
	
	l_uw3=Label(f_uw3,text="Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.05,rely=0.1,relheight=0.3,relwidth=0.1)
	lr_uw3=Label(f_uw3,text=''+n+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.15,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Age:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.355,rely=0.1,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+ag+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.455,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="D.O.B.:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.635,rely=0.1,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+dob+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.776,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Father's Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.355,rely=0.6,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+fn+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.499,rely=0.6,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Mother's Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0,rely=0.6,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+mn+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.155,rely=0.6,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Reg. status:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.689,rely=0.6,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+stat+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.8,rely=0.6,relheight=0.3,relwidth=0.155)

	img6=ImageTk.PhotoImage(file="user_win.png")
	f_uw4=Frame(user_window,relief=RIDGE)
	f_uw4.place(relx=0,rely=0.3,relheight=0.7,relwidth=1)
	
	l_img6=Label(f_uw4,image=img6)
	l_img6.place(relheight=1,relwidth=1)

	but_uw=Button(f_uw4,text="View Confirmation Report",font=("times new roman",15,"bold"),command=lambda:[view()],bg="purple",fg="white")
	but_uw.place(relx=0,rely=0,relheight=0.1,relwidth=0.3)

	but4=Button(f_uw4,text="Edit Profile",font=("times new roman",15,"bold"),bg="purple",fg="white",command=lambda:[edit()])
	but4.place(relx=0.0,rely=0.1,relheight=0.1,relwidth=0.3)

	but11=Button(f_uw4,text="Delete Registration",font=("times new roman",15,"bold"),bg="purple",fg="white",command=lambda:[cancel()])
	but11.place(relx=0,rely=0.2,relheight=0.1,relwidth=0.3)
	

def tw_op_view(obj1):
	with open("entry.csv","r") as f:
		global l1
		l1=[]
		read=csv.reader(f)
		for i in read:
			for j in range(len(i)):
				if i[j]==obj1:
					l1=l1+i
				else:
					pass

def view():
	view_f=Toplevel(root)
	view_f.title("Registration details")
	view_f.iconbitmap("impo.ico")
	view_f.geometry("500x550+250+50")
	view_f.config(bg="#000fff000")

	global gen,htt,wtt
	gen=l1[2]
	htt=l1[6]
	wtt=l1[7]
	phn=l1[8]

	wwl_uw0=Label(view_f,text="CONFIRMATION REPORT",font=("times new roman",25,"bold"),bg="#000fff000")
	wwl_uw0.place(relx=0.06,rely=0.001,relheight=0.1,relwidth=1)

	wwl_uw1=Label(view_f,text="Name",font=("times new roman",15,"normal"))
	wwl_uw1.place(relx=0.15,rely=0.15,relheight=0.05,relwidth=0.32)
	
	oowl_uw1=Label(view_f,text=''+n+'',font=("times new roman",15,"normal"))
	oowl_uw1.place(relx=0.5,rely=0.15,relheight=0.05,relwidth=0.32)
	
	wwl_uw2=Label(view_f,text="Age",font=("times new roman",15,"normal"))
	wwl_uw2.place(relx=0.15,rely=0.2,relheight=0.05,relwidth=0.32)
	
	oowl_uw2=Label(view_f,text=''+ag+'',font=("times new roman",15,"normal"))
	oowl_uw2.place(relx=0.5,rely=0.2,relheight=0.05,relwidth=0.32)
	
	wwl_uw3=Label(view_f,text="Gender",font=("times new roman",15,"normal"))
	wwl_uw3.place(relx=0.15,rely=0.25,relheight=0.05,relwidth=0.32)
	
	oowl_uw3=Label(view_f,text=''+gen+'',font=("times new roman",15,"normal"))
	oowl_uw3.place(relx=0.5,rely=0.25,relheight=0.05,relwidth=0.32)
	
	wwl_uw4=Label(view_f,text="D.O.B.",font=("times new roman",15,"normal"))
	wwl_uw4.place(relx=0.15,rely=0.3,relheight=0.05,relwidth=0.32)
	
	oowl_uw4=Label(view_f,text=''+dob+'',font=("times new roman",15,"normal"))
	oowl_uw4.place(relx=0.5,rely=0.3,relheight=0.05,relwidth=0.32)
	
	wwl_uw5=Label(view_f,text="Father's Name",font=("times new roman",15,"normal"))
	wwl_uw5.place(relx=0.15,rely=0.35,relheight=0.05,relwidth=0.32)
	
	oowl_uw5=Label(view_f,text=''+fn+'',font=("times new roman",15,"normal"))
	oowl_uw5.place(relx=0.5,rely=0.35,relheight=0.05,relwidth=0.32)
	
	wwl_uw6=Label(view_f,text="Mother's Name",font=("times new roman",15,"normal"))
	wwl_uw6.place(relx=0.15,rely=0.4,relheight=0.05,relwidth=0.32)
	
	oowl_uw6=Label(view_f,text=''+mn+'',font=("times new roman",15,"normal"))
	oowl_uw6.place(relx=0.5,rely=0.4,relheight=0.05,relwidth=0.32)
	
	wwl_uw7=Label(view_f,text="Height",font=("times new roman",15,"normal"))
	wwl_uw7.place(relx=0.15,rely=0.45,relheight=0.05,relwidth=0.32)
	
	oowl_uw7=Label(view_f,text=''+htt+'',font=("times new roman",15,"normal"))
	oowl_uw7.place(relx=0.5,rely=0.45,relheight=0.05,relwidth=0.32)
	
	wwl_uw8=Label(view_f,text="Weight",font=("times new roman",15,"normal"))
	wwl_uw8.place(relx=0.15,rely=0.5,relheight=0.05,relwidth=0.32)
	
	oowl_uw8=Label(view_f,text=''+wtt+'',font=("times new roman",15,"normal"))
	oowl_uw8.place(relx=0.5,rely=0.5,relheight=0.05,relwidth=0.32)
	
	wwl_uw9=Label(view_f,text="Phone No.",font=("times new roman",15,"normal"))
	wwl_uw9.place(relx=0.15,rely=0.55,relheight=0.05,relwidth=0.32)
	
	oowl_uw9=Label(view_f,text=''+phn+'',font=("times new roman",15,"normal"))
	oowl_uw9.place(relx=0.5,rely=0.55,relheight=0.05,relwidth=0.32)

	wwl_uw10=Label(view_f,text="Your application has been confirmed.",font=("times new roman",15,"normal"))
	wwl_uw10.place(relx=0.2,rely=0.65,relheight=0.05,relwidth=0.6)

	global var1
	var1=IntVar()
	Checkbutton(view_f, text="Receive a copy of registration on mail",variable=var1).place(relx=0.02,rely=0.75,relheight=0.05,relwidth=1)
	def close():
		print(var1.get())
		if var1.get()==1:
			mb.showinfo("INFO","A copy of your registration has been sent on email")
			view_f.destroy()
		else:
			view_f.destroy()

	oowl_uw10=Button(view_f,text="Close",font=("times new roman",15,"bold"),command=lambda:[close()])
	oowl_uw10.place(relx=0.35,rely=0.85,relheight=0.05,relwidth=0.32)
	
def edit():
	global edit_ent2,edit_s2,edit_ent3,edit_s3,var,img3,label_img3
	global ran,edit_f,l4,ind

	label_edit=Label(f_uw4,text="Update Your Details",font=("times new roman",20,"bold"),bg="purple",fg="white")
	label_edit.place(relx=0.43,rely=0.009,relheight=0.1,relwidth=0.4)
	
	but6=Button(f_uw4,text="Age",font=("times new roman",15,"bold"),command=lambda:[ran(but6.cget('text'))])
	but6.place(relx=0.46,rely=0.11,relheight=0.07,relwidth=0.3)

	but7=Button(f_uw4,text="D.O.B.",font=("times new roman",15,"bold"),command=lambda:[ran(but7.cget('text'))])
	but7.place(relx=0.46,rely=0.18,relheight=0.07,relwidth=0.3)

	but8=Button(f_uw4,text="Height",font=("times new roman",15,"bold"),command=lambda:[ran(but8.cget('text'))])
	but8.place(relx=0.46,rely=0.25,relheight=0.07,relwidth=0.3)

	but9=Button(f_uw4,text="Weight",font=("times new roman",15,"bold"),command=lambda:[ran(but9.cget('text'))])
	but9.place(relx=0.46,rely=0.32,relheight=0.07,relwidth=0.3)

	but10=Button(f_uw4,text="Phone No.",font=("times new roman",15,"bold"),command=lambda:[ran(but10.cget('text'))])
	but10.place(relx=0.46,rely=0.39,relheight=0.07,relwidth=0.3)

def ran(obj3):
	var=str(obj3)
	edit_label2=Label(f_uw4,text="Previous Entry:",font=("times new roman",15,"bold"),bg="purple",fg="white")
	edit_label2.place(relx=0.287,rely=0.5,relheight=0.09,relwidth=0.3)
	edit_ent2=Entry(f_uw4,font=("times new roman",15,"bold"))
	edit_ent2.place(relx=0.587,rely=0.5,relheight=0.09,relwidth=0.3)

	edit_label3=Label(f_uw4,text="New Entry:",font=("times new roman",15,"bold"),bg="purple",fg="white")
	edit_label3.place(relx=0.287,rely=0.7,relheight=0.09,relwidth=0.3)
	edit_ent3=Entry(f_uw4,font=("times new roman",15,"bold"))
	edit_ent3.place(relx=0.587,rely=0.7,relheight=0.09,relwidth=0.3)

	but5=Button(f_uw4,text="Proceed",font=("times new roman",15,"bold"),command=lambda:[edit_f(var,edit_ent3.get())])
	but5.place(relx=0.43,rely=0.87,relheight=0.1,relwidth=0.255)

def edit_f(obj,aft):

	with open("entry.csv","r") as f:
		
		read2=csv.reader(f)
		l4=[]
		for row in read2:
			if obj in row:
				ind=row.index(obj)
			if row!=l1:
				l4.append(row)
			elif row==l1:
				l1[ind]=aft
				l4.append(l1)

	with open("entry.csv","w") as f:
		wr=csv.writer(f,lineterminator="\n")
		wr.writerows(l4)
		mb.showinfo("Update Status","Updated successfully!")
	user_win()
	

def cancel():
	l_uw4=Label(f_uw4,text="Do you want to cancel your registration?",font=("times new roman",20,"normal"),bg="purple",fg="white")
	l_uw4.place(relx=0.34,rely=0.2,relheight=0.2,relwidth=0.6)
	but12=Button(f_uw4,text="Yes",font=("times new roman",15,"bold"),command=lambda:[cancel2()],bg="purple",fg="white")
	but13=Button(f_uw4,text="No",font=("times new roman",15,"bold"),command=lambda:[user_win()],bg="purple",fg="white")
	but12.place(relx=0.5,rely=0.45,relheight=0.2,relwidth=0.1)
	but13.place(relx=0.65,rely=0.45,relheight=0.2,relwidth=0.1)

def cancel2():
	with open("entry.csv","r") as f:
		read2=csv.reader(f)

		global l3
		l3=[]
		for row in read2:
			if row!=l1:
				l3.append(row)

	with open("entry.csv","w") as f2:
		write2=csv.writer(f2,lineterminator="\n")
		write2.writerows(l3)
		mb.showinfo("Registration Status","Your registration has been cancelled!")
	tl_screen.destroy()

def more_info():
	root5=Toplevel(root)
	root5.geometry("2000x2000+0+0")
	root5.iconbitmap("impo.ico")

	fr=Frame(root5,bg="purple")
	fr.place(relheight=1,relwidth=1)
	tl=Label(fr,text=('''This is the official website of Indian Army. 
		The Indian Army is the land-based branch and the largest component of the Indian Armed Forces. 
		The President of India is the Supreme Commander of the Indian Army,
		and its professional head is the Chief of Army Staff (COAS), who is a four-star general. 
		Two officers have been conferred with the rank of field marshal, a five-star rank,
		 which is a ceremonial position of great honour. The Indian Army originated from the armies of the East India Company, 
		which eventually became the British Indian Army, and the armies of the princely states, 
		which were merged into the national army after independence. 
 The units and regiments of the Indian Army have diverse histories and have participated in a number of battles and campaigns around the world, 
		earning many battle and theatre honours before and after Independence.
	The primary mission of the Indian Army is to ensure national security and national unity, 
	to defend the nation from external aggression and internal threats, and to maintain peace and security within its borders. 
	It conducts humanitarian rescue operations during natural calamities and other disturbances, such as Operation Surya Hope, 
	and can also be requisitioned by the government to cope with internal threats. 
	It is a major component of national power, alongside the Indian Navy and the Indian Air Force. 
	The army has been involved in four wars with neighbouring Pakistan and one with China.
 Other major operations undertaken by the army include Operation Vijay, Operation Meghdoot, and Operation Cactus. 
 The army has conducted large peace time exercises such as Operation Brasstacks and Exercise Shoorveer, 
	   and it has also been an active participant in numerous United Nations peacekeeping missions,
	  including those in Cyprus, Lebanon, Congo, Angola, Cambodia, Vietnam, Namibia, El Salvador, Liberia, Mozambique, South Sudan, and Somalia.
	The Indian Army is operationally and geographically divided into seven commands, 
	with the basic field formation being a division. 
	Below the division level are permanent regiments that are responsible for their own recruiting and training. 
	The army is an all-volunteer force and comprises more than 80% of the country's active defence personnel. 
	It is the largest standing army in the world, with 1,237,117 active troops and 960,000 reserve troops. 
	The army has embarked on an infantry modernisation program known as Futuristic Infantry Soldier As a System (F-INSAS),
	 and is also upgrading and acquiring new assets for its armoured, artillery, and aviation branches.
  STRICT ACTION WOULD BE TAKEN AGAINST ANY COPYRIGHT OR ATTEMPT TO STEAL THE SITE'S RESOURCES.'''),font=('times new roman',13,'bold'))
	tl.place(relx=0.07,rely=0.08,relheight=0.75,relwidth=0.85)

def personnel():
	global phot,main_winn
	main_winn=Toplevel(root)
	main_winn.geometry("800x250+290+220")
	main_winn.title("The Army Page")
	main_winn.iconbitmap("lieut.ico")
	phot=ImageTk.PhotoImage(file="m_winph.png")
	l_winn=Label(main_winn,image=phot)
	l_winn.place(relheight=1,relwidth=1)
	but_p1=Button(main_winn,text="Military Updation",font=('garamond',22,'bold'),cursor="hand2",fg="white",bg="purple",command=lambda:[ask_pass()])
	but_p1.place(relx=0.05,rely=0.5,relheight=0.2,relwidth=0.3)
	but_p2=Button(main_winn,text="Login",font=('garamond',22,'bold'),fg="white",bg="purple",command=lambda:[login_ar()],cursor="hand2")
	but_p2.place(relx=0.4,rely=0.5,relheight=0.2,relwidth=0.25)
	but_p3=Button(main_winn,text="View Weapons",font=('garamond',22,'bold'),cursor="hand2",fg="white",bg="purple",command=lambda:[Ch_tab()])
	but_p3.place(relx=0.7,rely=0.5,relheight=0.2,relwidth=0.27)


def update_n():

	global img9,uw
	main_winn.lift()
	
	main_winn.geometry("1000x400+250+130")
	main_winn.iconbitmap("impo.ico")

	uw=Frame(main_winn)
	uw.place(relheight=1,relwidth=1)

	img9=ImageTk.PhotoImage(file="black_win.jpg")
	im_l=Label(uw,image=img9)
	im_l.place(relheight=1,relwidth=1)

	but_p2=Button(uw,text="New Recruitment",font=('garamond',16,'bold'),command=lambda:[mil_chk(but_p2.cget('text'))])
	but_p2.place(relx=0.15,rely=0.15,relheight=0.13,relwidth=0.35)

	but_p3=Button(uw,text="Old Updation",font=('garamond',16,'bold'),command=lambda:[mil_chk(but_p3.cget('text'))])
	but_p3.place(relx=0.56,rely=0.15,relheight=0.13,relwidth=0.35)
		
def mil_chk(obj6):
	global mi,name_p,Id
	if obj6=="New Recruitment":
		mi="Enter former trainee Id:"
	elif obj6=="Old Updation":
		mi="Enter commander's Id:"

	name_p = Entry(uw,font=('Perpetua',17,'normal'))
	namep_label = Label(uw, text = 'Name :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	name_p.place(relx=0.4301,rely=0.3531,relheight=0.1,relwidth=0.5)
	namep_label.place(relx=0.1,rely=0.3531,relheight=0.1,relwidth=0.35)

	Id = Entry(uw,font=('Perpetua',17,'normal'))
	Id_label = Label(uw, text =''+mi+'', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	Id.place(relx=0.4301,rely=0.5,relheight=0.1,relwidth=0.5)
	Id_label.place(relx=0.1,rely=0.5,relheight=0.1,relwidth=0.35)

	global but_p4
	but_p4=Button(uw,text="Enter",font=('garamond',17,'bold'),command=lambda:[uw_chk()])
	but_p4.place(relx=0.35,rely=0.67,relheight=0.1,relwidth=0.3)

global uw_chk
def uw_chk():
	if name_p.get()=="" or Id.get()=="":
		mb.showerror("Error","Fill in the required details!")
		uw.destroy()
		update_n()
	if mi=="Enter former trainee Id:":
		with open("entry.csv","r") as f:
			r=csv.reader(f)
			global row1
			for row1 in r:
				if name_p.get() in row1 and Id.get() in row1:
					but_p4.destroy()
					
					global l_row1,l_row3,i_ar,p_ar
					p_ar=randrange(500,10000)
					i_ar='@Mid'+str(p_ar)
					
					l_row1=[]
					l_row3=[]
					l_row1=l_row1+row1
					l_row3=l_row3+l_row1
					l_row1[9]=i_ar
					l_row1[10]=p_ar

					appt = Label(uw, text ="Appoint as:", font = ('Perpetua',17,'bold'),bg="purple",fg="white")
					appt.place(relx=0.02,rely=0.67,relheight=0.1,relwidth=0.2)
					
					but_pa1=Button(uw,text="Commando", font = ('Perpetua',17,'bold'),command=lambda:[enter_army(but_pa1.cget('text'))])
					but_pa1.place(relx=0.22,rely=0.67,relheight=0.1,relwidth=0.15)
					but_pa2=Button(uw,text="Field Marshal", font = ('Perpetua',17,'bold'),command=lambda:[enter_army(but_pa2.cget('text'))])
					but_pa2.place(relx=0.37,rely=0.67,relheight=0.1,relwidth=0.15)
					but_pa3=Button(uw,text="General", font = ('Perpetua',17,'bold'),command=lambda:[enter_army(but_pa3.cget('text'))])
					but_pa3.place(relx=0.52,rely=0.67,relheight=0.1,relwidth=0.15)
					but_pa4=Button(uw,text="Lieutenant General", font = ('Perpetua',17,'bold'),command=lambda:[enter_army(but_pa4.cget('text'))])
					but_pa4.place(relx=0.67,rely=0.67,relheight=0.1,relwidth=0.19)
					but_pa5=Button(uw,text="Colonel", font = ('Perpetua',17,'bold'),command=lambda:[enter_army(but_pa5.cget('text'))])
					but_pa5.place(relx=0.86,rely=0.67,relheight=0.1,relwidth=0.15)

				def cancel3():
					uw.destroy()
					update_n()

				but_pa6=Button(uw,text="Cancel", font = ('Perpetua',17,'bold'),command=cancel3)
				but_pa6.place(relx=0.45,rely=0.79,relheight=0.1,relwidth=0.15)

	elif mi=="Enter commander's Id:":
		
		with open("army.csv","r") as f3:
			read=csv.reader(f3)
			global list_up
			list_up=[]
			for rr in read:
				list_up.append(rr)
			
			with open("army.csv","r") as f5:
				read4=csv.reader(f5)
				for roww in read4:
					if name_p.get() and Id.get() in roww:
						but_p4.destroy()
						global l_row2
						l_row2=[]
						l_row2=l_row2+roww
						print(l_row2)

						appt = Label(uw, text ="Appoint as:", font = ('Perpetua',17,'bold'),bg="purple",fg="white")
						appt.place(relx=0.02,rely=0.67,relheight=0.1,relwidth=0.2)				

						but_pa1=Button(uw,text="Commando", font = ('Perpetua',17,'bold'),command=lambda:[update_army(but_pa1.cget('text'))])
						but_pa1.place(relx=0.22,rely=0.67,relheight=0.1,relwidth=0.15)
						but_pa2=Button(uw,text="Field Marshal", font = ('Perpetua',17,'bold'),command=lambda:[update_army(but_pa2.cget('text'))])
						but_pa2.place(relx=0.37,rely=0.67,relheight=0.1,relwidth=0.15)
						but_pa3=Button(uw,text="General", font = ('Perpetua',17,'bold'),command=lambda:[update_army(but_pa3.cget('text'))])
						but_pa3.place(relx=0.52,rely=0.67,relheight=0.1,relwidth=0.15)
						but_pa4=Button(uw,text="Lieutenant General", font = ('Perpetua',17,'bold'),command=lambda:[update_army(but_pa4.cget('text'))])
						but_pa4.place(relx=0.67,rely=0.67,relheight=0.1,relwidth=0.19)
						but_pa5=Button(uw,text="Colonel", font = ('Perpetua',17,'bold'),command=lambda:[update_army(but_pa5.cget('text'))])
						but_pa5.place(relx=0.86,rely=0.67,relheight=0.1,relwidth=0.15)

					def cancel3():
						uw.destroy()
						update_n()

					but_pa6=Button(uw,text="Cancel", font = ('Perpetua',17,'bold'),command=cancel3)
					but_pa6.place(relx=0.45,rely=0.79,relheight=0.1,relwidth=0.15)

def enter_army(post):
	print(row1)
	global l_army
	l_army=[]
	l_army=l_army+l_row1
	l_army.append(post)

	with open("army.csv","a",newline="") as f2:
		wr=csv.writer(f2)
		wr.writerow(l_army)
		mb.showinfo("Success","Entry done successfully!\n\nId and Password would be generated shortly")

		global img8
		img8=ImageTk.PhotoImage(file="army_log.png")
		main_winn.lift()
		main_winn.title("Commander's login info")
		main_winn.geometry('400x200+500+250')
		main_winn.iconbitmap("impo.ico")
		rlog_ar=Frame(main_winn)
		rlog_ar.place(relheight=1,relwidth=1)
		rlog_img=Label(rlog_ar,image=img8)
		rlog_img.place(relheight=1,relwidth=1)

		def des1():
			main_winn.destroy()
			personnel()

		l2=Label(rlog_ar,text=i_ar,font = ('Perpetua',12,'bold'),bg="white") 
		l2.place(relx=0.45,rely=0.25,relheight=0.15,relwidth=0.3)
		
		l_l=Label(rlog_ar,text="M_ID:",font = ('Perpetua',12,'bold'),bg="purple",fg="white")
		l_l.place(relx=0.1,rely=0.25,relheight=0.15,relwidth=0.35)
		
		l=Label(rlog_ar,text=p_ar,font = ('Perpetua',12,'bold'),bg="white")
		l.place(relx=0.45,rely=0.55,relheight=0.15,relwidth=0.35)

		l2_l=Label(rlog_ar,text="PASSWORD:",font = ('Perpetua',12,'bold'),bg="purple",fg="white") 
		l2_l.place(relx=0.1,rely=0.55,relheight=0.15,relwidth=0.35)
		
		but3=Button(rlog_ar,text="OK",font = ('Perpetua',12,'bold'),command=des1)
		but3.place(relx=0.32,rely=0.75,relheight=0.12,relwidth=0.35)

	with open("entry.csv","r") as f:
		read2=csv.reader(f)

		global l4
		l4=[]
		for row in read2:
			if row!=l_row3:
				l4.append(row)

	with open("entry.csv","w") as f2:
		write2=csv.writer(f2,lineterminator="\n")
		write2.writerows(l4)

def update_army(post):
	with open("army.csv","w",newline="") as f4:
		write3=csv.writer(f4)
		for i in range(len(list_up)):
			if list_up[i]==l_row2:
				l_row2[11]=post
				list_up[i]=l_row2

		write3.writerows(list_up)
		mb.showinfo("Update Status","Updation Successful")
		main_winn.destroy()
		personnel()

def ask_pass():
	global prot_ph
	prot=Toplevel(main_winn)
	prot.geometry("1000x200+200+220")
	prot.iconbitmap("impo.ico")

	prot_ph=ImageTk.PhotoImage(file="prot_pass.png")
	labe_protph=Label(prot,image=prot_ph)
	labe_protph.place(relheight=1,relwidth=1)

	labe=Label(prot,text="Enter the 6-digit access code:",font=("times new roman",18,"bold"),bg="gold")
	labe.place(relx=0.17,rely=0.27,relheight=0.17,relwidth=0.4)

	labe_e=Entry(prot,font=("times new roman",18,"bold"),show="*")
	labe_e.place(relx=0.58,rely=0.27,relheight=0.17,relwidth=0.3)

	def check_pass():
		password="123456"
		if labe_e.get()==password:
			mb.showinfo("Access","Access granted!")
			prot.destroy()
			update_n()
		else:
			mb.showerror("Access","Access denied!")
			prot.lift()
	
	but_prot1=Button(prot,text="Enter",font=("times new roman",18,"bold"),cursor="hand2",command=check_pass)
	but_prot1.place(relx=0.4,rely=0.55,relheight=0.15,relwidth=0.1)

def login_ar():
	global img10,le_ar,le_ar2

	main_winn.lift()
	main_winn.geometry("500x260+370+220")
	main_winn.iconbitmap("impo.ico")
	main_winn.title("LOGIN")
	log_ar=Frame(main_winn)
	log_ar.place(relheight=1,relwidth=1)

	img10=ImageTk.PhotoImage(file="army_log.png")
	l_img10=Label(log_ar,image=img10)
	l_img10.place(relheight=1,relwidth=1)

	l_ar=Label(log_ar,text="Enter Commander Id:",font=('garamond',16,'bold'),bg="purple",fg="white")
	l_ar.place(relx=0.04,rely=0.23,relwidth=0.4,relheight=0.12)
	le_ar=Entry(log_ar,font=('garamond',16,'bold'))
	le_ar.place(relx=0.52,rely=0.23,relwidth=0.4,relheight=0.12)

	l_ar2=Label(log_ar,text="Enter Password:",font=('garamond',16,'bold'),bg="purple",fg="white")
	l_ar2.place(relx=0.0235,rely=0.5,relwidth=0.5,relheight=0.12)
	le_ar2=Entry(log_ar,font=('garamond',16,'bold'),show="*")
	le_ar2.place(relx=0.55,rely=0.5,relwidth=0.43,relheight=0.12)

	but_ar1=Button(log_ar,text="Enter",font=('garamond',22,'bold'),command=lambda:[chk_ar()],cursor="hand2")
	but_ar1.place(relx=0.4,rely=0.68,relheight=0.1,relwidth=0.2)

def arm_page():
	global img6,img7,arm_p
	main_winn.lift()
	main_winn.geometry("1250x600+85+50")
	main_winn.iconbitmap("lieut.ico")
	
	arm_p=Frame(main_winn)
	arm_p.place(relheight=1,relwidth=1)

	img6=ImageTk.PhotoImage(file="Pers_2.png")
	l_img6=Label(arm_p,image=img6)
	l_img6.place(relheight=1,relwidth=1)

	aw_op_view(le_ar.get())
	
	global n1,ag1,dob1,fn1,mn1,post1

	n1=l5[0]
	ag1=l5[1]
	dob1=l5[3]
	fn1=l5[4]
	mn1=l5[5]
	post1=l5[11]

	f_uw3=Frame(arm_p,bg="purple")
	f_uw3.place(relx=0,rely=0,relheight=0.25,relwidth=0.76)
	
	l_uw3=Label(f_uw3,text="Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.05,rely=0.1,relheight=0.3,relwidth=0.1)
	lr_uw3=Label(f_uw3,text=''+n1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.15,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Age:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.355,rely=0.1,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+ag1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.455,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="D.O.B.:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.635,rely=0.1,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+dob1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.776,rely=0.1,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Father's Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.355,rely=0.6,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+fn1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.499,rely=0.6,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Mother's Name:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0,rely=0.6,relheight=0.3,relwidth=0.155)
	lr_uw3=Label(f_uw3,text=''+mn1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.155,rely=0.6,relheight=0.3,relwidth=0.155)
	
	l_uw3=Label(f_uw3,text="Rank:",font=("times new roman",15,"normal"))
	l_uw3.place(relx=0.699,rely=0.6,relheight=0.3,relwidth=0.1)
	lr_uw3=Label(f_uw3,text=''+post1+'',font=("times new roman",15,"bold"))
	lr_uw3.place(relx=0.795,rely=0.6,relheight=0.3,relwidth=0.175)

	global f_uw6
	f_uw6=Frame(arm_p,relief=RIDGE)
	f_uw6.place(relx=0,rely=0.25,relheight=0.75,relwidth=0.76)

	img7=ImageTk.PhotoImage(file="Pers_3.png")
	l_img7=Label(f_uw6,image=img7)
	l_img7.place(relheight=1,relwidth=1)

	buta4=Button(f_uw6,text="Edit Profile",font=("times new roman",20,"bold"),command=lambda:[edita()],bg="purple",fg="white",cursor="hand2")
	buta4.place(relx=0,rely=0.04,relheight=0.085,relwidth=1)
		
def aw_op_view(obj1):
	with open("army.csv","r") as f:
		global l5
		l5=[]
		read=csv.reader(f)
		for i in read:
			for j in range(len(i)):
				if i[j]==obj1:
					l5=l5+i
				else:
					pass
		
def edita():
	global edit_ent3,edit_s3,edit_ent4,edit_s4,var2,img4,label_img4
	global ran2,edit_f,l6,ind2

	label_edit=Label(f_uw6,text="Update Your Details",font=("times new roman",20,"bold"),bg="purple",fg="white")
	label_edit.place(relx=0.08,rely=0.17,relheight=0.1,relwidth=0.4)

	buta6=Button(f_uw6,text="Age",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[ran2(buta6.cget('text'))])
	buta6.place(relx=0.1,rely=0.3,relheight=0.07,relwidth=0.3)

	buta7=Button(f_uw6,text="D.O.B.",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[ran2(buta7.cget('text'))])
	buta7.place(relx=0.1,rely=0.37,relheight=0.07,relwidth=0.3)

	buta8=Button(f_uw6,text="Height",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[ran2(buta8.cget('text'))])
	buta8.place(relx=0.1,rely=0.44,relheight=0.07,relwidth=0.3)

	buta9=Button(f_uw6,text="Weight",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[ran2(buta9.cget('text'))])
	buta9.place(relx=0.1,rely=0.51,relheight=0.07,relwidth=0.3)

	buta10=Button(f_uw6,text="Phone No.",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[ran2(buta10.cget('text'))])
	buta10.place(relx=0.1,rely=0.58,relheight=0.07,relwidth=0.3)
	
def ran2(obj3):
	var2=str(obj3)
	edit_label2=Label(f_uw6,text="Previous Entry:",font=("times new roman",15,"bold"),bg="purple",fg="white")
	edit_label2.place(relx=0.399,rely=0.3,relheight=0.09,relwidth=0.3)
	edit_ent3=Entry(f_uw6,font=("times new roman",15,"bold"))
	edit_ent3.place(relx=0.699,rely=0.3,relheight=0.09,relwidth=0.3)

	edit_label3=Label(f_uw6,text="New Entry:",font=("times new roman",15,"bold"),bg="purple",fg="white")
	edit_label3.place(relx=0.399,rely=0.5,relheight=0.09,relwidth=0.3)
	edit_ent4=Entry(f_uw6,font=("times new roman",15,"bold"))
	edit_ent4.place(relx=0.699,rely=0.5,relheight=0.09,relwidth=0.3)

	but5=Button(f_uw6,text="Proceed",font=("times new roman",15,"bold"),cursor="hand2",command=lambda:[edit_f2(var2,edit_ent4.get())])
	but5.place(relx=0.55,rely=0.67,relheight=0.1,relwidth=0.255)

def edit_f2(obj2,aft2):
	if aft2=="":
		mb.showerror("Error","Fill required column!")
		edita()
	with open("army.csv","r") as f:
		read2=csv.reader(f)
		l6=[]
		for row in read2:
			if obj2 in row:
				ind2=row.index(obj2)
			if row!=l5:
				l6.append(row)
			elif row==l5:
				l5[ind2]=aft2
				l6.append(l5)
		print(l6)
		with open("army.csv","w",newline="") as f5:
			wr=csv.writer(f5)
			wr.writerows(l6)
			mb.showinfo("Update Status","Updated successfully!")
		arm_p.destroy()
		arm_page()
		
def chk_ar():
	with open("army.csv","r") as f:
		read=csv.reader(f)
		var_1=0
		for i in read:
			if le_ar.get() and le_ar2.get() in i:
				var_1=var_1+1
		if var_1==1:
			mb.showinfo("Search","Record exists")
			arm_page()
		else:
			mb.showerror("Search","No such record!")

def table_show(total_rows,total_columns):
	global photo_w

	photo_w=ImageTk.PhotoImage(file="join.png")
	main_winn.geometry("700x500+270+100")
	tab = Frame(main_winn)
	tab.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)

	labe_tab=Label(tab,image=photo_w)
	labe_tab.place(relheight=1,relwidth=1)

	tab2=Frame(main_winn)
	tab2.place(relx=0,rely=0,relheight=0.2,relwidth=1)

	labe_tab=Label(tab2,image=photo_w)
	labe_tab.place(relheight=1,relwidth=1)

	l_t=Label(tab2,text="WEAPONS",font=('goudy stout',25,'bold'),fg="purple")
	l_t.place(relx=0.28,rely=0.2,relheight=0.7,relwidth=0.5)


	for i in range(total_rows):
		for j in range(total_columns):
			tab_ent= Entry(tab, width=20, fg='purple',justify="center",font=('Arial',16,'bold'))
			tab_ent.insert(END,l1[i][j])
			tab_ent.configure(state="readonly")
			tab_ent.grid(row=i, column=j)
	but_me=Button(tab,text="Make changes",height=3,width=33,command=lambda:[make_entry()],fg="white",bg="purple",font=('times new roman',10,'bold'))
	but_me.grid(row=total_rows,column=0)


def Ch_tab():
	main_winn.lift()
	with open("weapons.csv","r") as f:
		global l1
		l1=[]
		read=csv.reader(f)
		for i in read:
			l1=l1+[i]
		print(l1)
		tr=len(l1)
		tc=len(l1[0])
		table_show(tr,tc)

def save1(obj):
	global list_a
	list_a=[]
	with open("weapons.csv", "r") as f1:
		read_w=csv.reader(f1)
		for i in read_w:
			if S_No.get() in i:
				list_a=list_a+[obj]
			else:
				list_a=list_a+[i]
		with open("weapons.csv","w") as f:
			wr=csv.writer(f,lineterminator="\n")
			wr.writerows(list_a)
			mb.showinfo("Update Status","Updated successfully!")
	Ch_tab()

def make_entry():

	global list_w,S_No,n_w,quant
	main_winn.geometry("500x300+350+100")
	ent=Frame(main_winn)
	ent.place(relheight=1,relwidth=1)

	labe_ent=Label(ent,image=photo_w)
	labe_ent.place(relheight=1,relwidth=1)

	head_lab=Label(ent,text="Update",font=('goudy stout',25,'bold'),fg="purple")
	head_lab.place(relx=0.2,rely=0.1,relheight=0.2,relwidth=0.6)

	S_No = Entry(ent,font=('Perpetua',19,'normal'),justify="center")
	s_no_label = Label(ent, text = 'S.No. :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	S_No.place(relx=0.1,rely=0.46,relheight=0.14,relwidth=0.25)
	s_no_label.place(relx=0.1,rely=0.353,relheight=0.1,relwidth=0.25)
	
	n_w = Entry(ent,font=('Perpetua',19,'normal'),justify="center")
	n_w_label = Label(ent, text = 'Weapon :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	n_w.place(relx=0.35,rely=0.46,relheight=0.14,relwidth=0.25)
	n_w_label.place(relx=0.35,rely=0.353,relheight=0.1,relwidth=0.25)

	quant = Entry(ent,font=('Perpetua',19,'normal'),justify="center")
	quant_label = Label(ent, text = 'Quantity :', font = ('Perpetua',17,'bold'),bg="purple",fg="white")
	quant.place(relx=0.6,rely=0.46,relheight=0.14,relwidth=0.25)
	quant_label.place(relx=0.6,rely=0.353,relheight=0.1,relwidth=0.25)

	but_w=Button(ent,text="Enter",command=lambda:[check_w()],fg="purple",font=('times new roman',15,'bold'))
	but_w.place(relx=0.29,rely=0.63,relheight=0.14,relwidth=0.35)

def check_w():
	if S_No.get()=="" or n_w=="" or quant=="":
		mb.showerror("Error","Fill all fields")
	else:
		list_w=[S_No.get(),n_w.get(),quant.get()]
		save1(list_w)

root.mainloop()	