import mysql.connector
from tkinter import *
from tkinter import messagebox
#create database#create table
# user_insert_ in sql.py


#create window 
window=Tk()
window.geometry('500x400')
window.resizable(True,True)
window.title('insert data by user')

#column configure
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

#create information
fname=StringVar()
lname=StringVar()
#phone_number=IntVar()
email=StringVar()
password=StringVar()
r_password=StringVar()
#fname 
fname_lbl=Label(window,text='firstname:')
fname_lbl.grid(row=0,column=0,sticky=W,padx=5,pady=5)
fname_entry=Entry(window,textvariable=fname)
fname_entry.grid(row=0,column=1,sticky=E,padx=10,pady=10,ipadx=150,ipady=3)
fname_entry.focus()
#lname
lname_lbl=Label(window,text='lastname:')
lname_lbl.grid(row=1,column=0,sticky=NW,padx=5,pady=5)
lname_entry=Entry(window,textvariable=lname)
lname_entry.grid(row=1,column=1,sticky=E,padx=10,pady=10,ipadx=150,ipady=3)
#email
email_lbl=Label(window,text='email:')
email_lbl.grid(row=2,column=0,sticky=W,padx=5,pady=5)
email_entry=Entry(window,textvariable=email)
email_entry.grid(row=2,column=1,sticky=E,padx=10,pady=10,ipadx=150,ipady=3)
#password
password_lbl=Label(window,text='password:')
password_lbl.grid(row=3,column=0,sticky=W,padx=5,pady=5)
password_entry=Entry(window,textvariable=password,show='*')
password_entry.grid(row=3,column=1,sticky=E,padx=10,pady=10,ipadx=150,ipady=3)
#r_password
r_password_lbl=Label(window,text='r_password:')
r_password_entry=Entry(window,textvariable=r_password,show='*')
r_password_lbl.grid(row=5,column=0,sticky=W,padx=5,pady=5)
r_password_entry.grid(row=5,column=1,sticky=E,padx=10,pady=10,ipadx=150,ipady=3)
#def  warning errors
def empty_error():
 messagebox.showwarning(
   'hint',
    'The box must not be empty'
 )
def  unequal_pass_error():
 messagebox.showwarning(
   'hint',
    'password must be equal r_password'
 )
def len_pass_error():
 messagebox.showwarning(
   'hint',
    'password len must be  8 charectors and consist of uppercase and lowercase letters'
 )
def  email_error():
    messagebox.showwarning(
   'hint',
    'email must be @ and .com'
    )

#function  submitbutton
def submit_inform():
  #conditions
  if len(fname.get())==0 or len(lname.get())==0 or len(email.get())==0 or len(password.get())==0 or len(r_password.get())==0:
   empty_error()
  elif password.get()!=r_password.get():
    unequal_pass_error()
   
  elif  len(password.get())<8  or   any( password.get().islower() for i in  password.get() ) or  any ( password.get().isdigit() for i in  password.get()) or any( password.get().isupper() for i in  password.get()):
    len_pass_error()
  
  elif email.get().find('@')==-1 or email.get().endswith('.com')==False:
    email_error()
  else:
   mydb=mysql.connector.connect(
   host='localhost',
   username='root',
   password='',
   database='information'
   )
   mycursor=mydb.cursor()
   sql='insert into usersinform(firstname,lastname,email,password) values(%s,%s,%s,%s)' 
   val=(fname.get(),lname.get(),email.get(),password.get())
   mycursor.execute(sql,val)
   mydb.commit()
   msg=f'your information such as firstname: {fname.get()} and lastname: {lname.get()}and email: {email.get()} and password: {password.get()} and r_password: {r_password.get()} insert in databse'
   messagebox.showinfo(
    'information',
     message= msg
   )
#submit button
submit_button=Button(window,text='submit',command=submit_inform)
submit_button.grid(row=6,column=1,sticky=SE,padx=15,pady=15)

#none close window
window.mainloop()