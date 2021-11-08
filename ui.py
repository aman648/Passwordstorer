from tkinter import *
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root')
mydbcursor=mydb.cursor()
root=Tk()
mydbcursor.execute('use mydb')
root.geometry("400x400")


def click():
    la=Label(root,text="saved",width=500,fg="green")
    la.pack()
def submit():
    type=e.get()
    password=e1.get()
    mydbcursor.execute('use mydb')
    cmd=f"insert into storagepassword(type,Password) values('{type}','{password}')"
    mydbcursor.execute(cmd)
    mydb.commit()
    click()
    e.delete(0,"end")
    e1.delete(0,"end")



def display(l):
    listbox=Listbox(root,height=12,bg="grey",fg="white")
    c=0
    for i in l:
        listbox.insert(c,i)
        c=c+1
             
    listbox.pack(pady=10)
    
       

   

def show():
    mydbcursor.execute('select * from storagepassword;')
    l=mydbcursor.fetchall()
    print(type(l))
    display(l)

def delete():
    todelete=e.get()
    cmd=f'DELETE FROM storagepassword WHERE type="{todelete}"'
    mydbcursor.execute(cmd)
    print(todelete)

    Label(root,text="deleted",fg="green").pack()

e=Entry(root,width=100)
e.pack(pady=5)
e1=Entry(root,width=100)
e1.pack(pady=5)
button0=Button(root,text="submit",command=submit,bg="blue",fg="white")
button1=Button(root,text="show",command=show,bg="blue",fg="white")
button2=Button(root,text="delete",command=delete,bg="blue",fg="white")
button2.pack()
button0.pack()
button1.pack()
listbox=Listbox(root,height=12)
listbox.insert

root.mainloop()
