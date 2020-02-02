from tkinter import *
import psycopg2

root = Tk()
root.geometry('500*500')
root.title("Registration Form")


Fullname=StringVar()
E-Mail=StringVar()
var = IntVar()
c=StringVar()
var1=IntVar()

def connect(database_name="registration"):
    db = psycopg2.connect("dbname={}".format(database_name))
    return db

def database():
	name=Fullname.get()
	email=E-Mail.get()
	gender=var.get()
	branch=c.get()
	session=var1.get()
	db = connect()
    c = db.cursor()
    c.execute('Create table if not exists Student (Fullname TEXT,E-Mail TEXT,Gender TEXT,Branch TEXT,Session TEXT)')
    c.execute('Insert Into Student (Fullname,E-Mail,Gender,Branch,Session) VALUES (?,?,?,?,?)',(name,email,gender,branch,session))
    db.commit()

label_0 = Label(root, text="Registration Form", width=20, font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Full Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)

label_2 = Label(root, text="E-Mail",width=20,font=("bold",10))
label_2.place(x=80,y=130)

entry_2= Entry(root)
entry_2.place(x=240,y=130)

label_3 = Label(root, text="Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20,variable=var,value=2).place(x=290,y=230)

label_4 = Label(root, text="Branch",width=20,font=("bold",10))
label_4.place(x=70,y=230)

list_1= ['Computer Sc.','Mechanical','Electrical','Civil','Diploma'];
c=StringVar()
droplist=OptionMenu(root,c, *list)
droplist.config(width=15)
c.set('Select Your Branch')
droplist.place(x=240,y=280)

label_4= Label(root,text="Session",width=20,font=("bold",10))
label_4.place(x=85,y=330)
var1= IntVar()
Checkbutton(root,text="Morning",variable=var1).place(x=235,y=330)
var2= IntVar()
Checkbutton(root,text="Evening",variable=var2).place(x=290,y=330)

Button(root,text='Submit',width=20,bg='brown',fg='white',comand=database).place(x=180,y=380)

mainloop()