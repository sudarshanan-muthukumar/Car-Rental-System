from tkinter import *
import cx_Oracle

root = Tk()
root.geometry('300x400')
root.title('Register to access')

con=cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
cur = con.cursor()

'''cur.execute("create table reg(username varchar(20) primary key,password varchar(20))")
 
cur.execute("create table customer(cu_id int primary key,customer_name varchar(40),phone_no int)")'''
'''cur.execute("create table car_details(no_of_pass int,car_name varchar(20),cu_id references customer(cu_id),c_date varchar(20))")'''
'''cur.execute("create table book_details(b_id int primary key,cost int,cu_id references customer(cu_id))")'''
con.commit()
lb = Label(root, text="Username")
lb.pack()
e = Entry(root)
e.pack()
lb2 = Label(root, text="Password")
lb2.pack()
e2 = Entry(root)
e2.pack()


def insert():
    a = str(e.get())
    b = str(e2.get())
    con=cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
    cursor = con.cursor()
    cursor.execute(f"insert into reg values('{a}','{b}')")
    con.commit()


def ne():
    def search():
        c = str(e3.get())
        d = str(e4.get())
        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
        cursor = con.cursor()
        cnt = 0
        for i in cursor.execute(f"select * from reg where username='{c}' and password='{d}'"):
            cnt += 1
        if cnt == 1:
            def newwindow():
                new = Toplevel(new1)
                new.geometry('500x300')
                new.title('Welcome to Kamal Cars')

                def add():
                    add = Toplevel(new)
                    add.geometry('500x300')
                    add.title('Add customer details')
                    l1 = Label(add, text="Customer id")
                    l1.grid(row=1, column=2)
                    l2 = Label(add, text="Name")
                    l2.grid(row=2, column=2)
                    l3=Label(add,text="Phone no").grid(row=3,column=2)
                    a1 = Entry(add)
                    a1.grid(row=1, column=3)
                    a2 = Entry(add)
                    a2.grid(row=2, column=3)
                    a3=Entry(add)
                    a3.grid(row=3,column=3)
                   

                    def insert():
                        a = int(a1.get())
                        b = str(a2.get())
                        c=int(a3.get())
                        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                        cur = con.cursor()
                        cur.execute(f"insert into customer values({a},'{b}',{c})")
                        con.commit()
                        con.close()
                        showcars()
                        def showcars():
                            show=Toplevel(add)
                            show.geometry('600x600')
                            show.title("List of various cars")
                            lb1=Label(show,text="Car name  \t  Seat capacity\t Price for 1 day\nHonda City\t5\tRs:1000\nTata Indigo\t5\tRs:400\nInova          \t10\tRs:1100")
                            lb1.grid(row=3,column=1)
                            sc1=Label(show,text="Car name").grid(row=6,column=1)
                            sc2=Label(show,text="Number of passenger(s)").grid(row=7,column=1)
                            sc3=Label(show,text="Date of travel").grid(row=8,column=1)
                            k=Entry(show)
                            k.grid(row=6,column=2)
                            k2=Entry(show)
                            k2.grid(row=7,column=2)
                            k3=Entry(show)
                            k3.grid(row=8,column=2)
                            d={"Honda City":1000,"Tata Indigo":400,"Inova":1100}
                            def inp():
                                ks=str(k.get())
                                ks2=int(k2.get())
                                ks3=str(k3.get())
                                con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                                cur = con.cursor()
                                cur.execute(f"insert into car_details values({ks2},'{ks}',{a},'{ks3}')")
                                v=int(d[ks])
                                b_id=1
                                for i in cur.execute("select max(b_id) from book_details"):
                                    print(i)
                                    for j in i:
                                        b_id=int(j)+1
                                t=Label(show,text=f"Your booking id={b_id}").grid(row=11,column=2)
                                t2=Label(show,text=f"Succesful Payment").grid(row=12 ,column=2)
                                cur.execute(f"insert into book_details values({b_id},{v},{a})")
                                con.commit()
                                def last():
                                    final=Toplevel(show)
                                    final.geometry("400x400")
                                    final.title("Payment Successful")
                                    c=Label(final,text=f"            Congrats your payment is succesful\n\n        Your booking id={b_id}\n Kindly visit us again! ").grid(row=2,column=1)
                                last()
                            bt=Button(show,text="Click for payment",command=inp)
                            bt.grid(row=9,column=2)


                       

                        # b1 = Button(d, text="serach", command=display2)
                        # b1.grid(row=3, column=3)

                    b1 = Button(add, text="Add your details", command=insert)
                    b1.grid(row=10, column=10)
                 

                    '''def dis():
                       
                        dis = Toplevel(add)
                        dis.geometry('500x300')
                        dis.title('show car details')
                        l1 = Label(dis, text='display here:')
                        l1.grid(row=5, column=5)
                        lb1 = Listbox(dis)
                        lb1.grid(row=5, column=6)
                        addbutton1 = Button(dis, text="show available cars")
                        addbutton1.grid(row=10, column=10)
                        addbutton2 = Button(dis, text="abort")
                        addbutton2.grid(row=11, column=11)
                        addbutton3 = Button(dis, text="procede to payment")
                        addbutton3.grid(row=9, column=9)'''

                def search():
                    def search2():
                        v=int(se.get())
                        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                        cur = con.cursor()
                        global txt
                        txt=""
                        cnt=0
                        for i in cur.execute(f"select customer_name,car_name,c_date from car_details,customer where customer.cu_id={v} and car_details.cu_id={v}"):

                            for j in i:
                                if cnt % 3 == 0:                      
                                    txt+="\n"
                                    txt += "customer name: "
                                elif cnt % 3 == 1:
                                    txt += "car name: "
                                elif cnt % 3 == 2:
                                    txt += "date: "
                                for k in j:
                                    txt+=str(k)
                                cnt += 1
                                txt += "\n"


                        if txt=="":
                            t=Label(search,text="Not found",font=("helvetica",17)).grid(row=5,column=3)
                        else:
                            t=Label(search,text=txt,font=("helvetica",17)).grid(row=5,column=3)
                        con.commit()
                        con.close()
                    search = Toplevel(new)
                    search.title("Search")
                    search.geometry("800x800")
                    sl=Label(search,text="Enter your customer id",font=("helvetica",17)).grid(row=2,column=2)
                    se=Entry(search,font=("helvetica",17))
                    se.grid(row=2,column=3)
                    bu=Button(search,text="Find details",font=("helvetica",17),command=search2)
                    bu.grid(row=3,column=3)
               

                def delete():
                    delete = Toplevel(new)
                    delete.geometry('500x300')
                    delete.title('Cancel booking')
                    l1 = Label(delete, text='Enter your book id ')
                    l1.grid(row=1, column=2)
                    e1 = Entry(delete)
                    e1.grid(row=1, column=3)
                   
                    def dell():
                        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                        cur = con.cursor()
                        c=int(e1.get())
                        cur.execute(f"delete from book_details where b_id={c}")
                        s1=Label(delete,text="Booking cancelled, amount will be refunded soon").grid(row=5,column=3)
                        cur.close()
                        con.commit()
                        con.close()
                    deletebutton = Button(delete, text='Cancel Booking',command=dell)
                    deletebutton.grid(row=10, column=10)
                   
                       

                def update():
                    update = Toplevel(new)
                    update.geometry('500x300')
                    update.title('Update car details')
                    l1 = Label(update, text='Enter booking date')
                    l1.grid(row=1, column=2)
                    e1 = Entry(update)
                    e1.grid(row=1, column=3)
                    l2 = Label(update, text='Enter your customer id')
                    l2.grid(row=2, column=2)
                    l3 = Label(update, text='Modified value->')
                    l3.grid(row=14, column=2)
                    e2 = Entry(update)
                    e2.grid(row=2, column=3)
                    lb1=Listbox(update,height=50,width=50)
                    lb1.grid(row=14,column=14)
                    def update1():
                        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                        cur = con.cursor()
                        c1=str(e1.get())
                        c2=int(e2.get())
                        cur.execute(f"update car_details set c_date='{c1}' where cu_id={c2}")
                        cur.close()
                        con.commit()
                        con.close()
                    def select12():
                        con = cx_Oracle.connect("xe/xe@DESKTOP-30KVP23:1521/xe")
                        cur = con.cursor()
                        c2=int(e2.get())
                        for j in cur.execute(f"select * from car_details where cu_id={c2}"):
                            lb1.insert('end',j)
                        con.commit()
                   
                           
                    updatebutton = Button(update, text='Update booking date',command=update1)
                    updatebutton.grid(row=10, column=10)
                    show=Button(update,text="Show changes",command=select12)
                    show.grid(row=12,column=12)
                def exit1():
                    new.destroy()

                addb = Button(new, text="Book Car", command=add)
                searchb = Button(new, text="Search details", command=search)
                updateb = Button(new, text="Update details", command=update)
                deleteb = Button(new, text="Cancel booking", command=delete)
                exit=Button(new,text='Exit',command=exit1)
                addb.grid(row=2, column=3)
                searchb.grid(row=5, column=6)
                updateb.grid(row=6, column=7)
                deleteb.grid(row=7, column=8)
                exit.grid(row=8,column=9)
            newwindow()

        elif cnt == 0:
            lbb = Label(new1, text="Invalid")
            lbb.pack()
        con.commit()

    new1 = Toplevel(root)
    new1.geometry("400x400")
    new1.title("Log in ")

    l = Label(new1, text="Username").pack()
    e3 = Entry(new1)
    e3.pack()
    l2 = Label(new1, text="Password").pack()
    e4 = Entry(new1,show='*')
    e4.pack()
    b = Button(new1, text="Log in", command=search).pack()


bt = Button(root, text="Sign up", command=insert).pack()
bt2 = Button(root, text="Already signed up", command=ne).pack()

root.mainloop()
