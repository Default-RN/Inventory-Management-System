from tkinter import *
from employees import employee_form, connect_database
from supplier import supplier_form
from category import category_form
from product import product_form
from tkinter import messagebox
import time

def update():
    cursor,connection=connect_database()
    if not cursor or not connection:
        return
    cursor.execute('use inventory_system')
    cursor.execute('SELECT * from employee_data')
    emp_records=cursor.fetchall()
    total_emp_count_label.config(text=len(emp_records))

    cursor.execute('SELECT * from supplier_data')
    sup_records=cursor.fetchall()
    total_sup_count_label.config(text=len(sup_records))

    cursor.execute('SELECT * from category_data')
    cat_records=cursor.fetchall()
    total_cat_count_label.config(text=len(cat_records))

    cursor.execute('SELECT * from product_data')
    pro_records=cursor.fetchall()
    total_prod_count_label.config(text=len(pro_records))


    date_time=time.strftime('%I:%M:%S %p on %A, %B %d, %Y')
    subtitleLabel.config(text=f'Welcome Admin\t\t\t\t\t\t {date_time}')
    subtitleLabel.after(400,update)


#creating tax button and its working
def tax_window():
    def save_tax():
        value=tax_count.get()
        cursor,connection=connect_database()
        if not cursor or not connection:
            return
        cursor.execute('use inventory_system')
        cursor.execute('CREATE TABLE IF NOT EXISTS tax_table (id INT primary key, tax DECIMAL(5,2))')
        cursor.execute('SELECT id from tax_table WHERE id=1')
        if cursor.fetchone():
            cursor.execute('UPDATE tax_table SET tax=%s WHERE id=1',value)
        else:
            cursor.execute('INSERT INTO tax_table (id,tax) VALUES(1,%s)',value)
        connection.commit()
        messagebox.showinfo('Success','Tax is set to {value}% and saved successfully.',parent=tax_root)
    tax_root=Toplevel()
    tax_root.title=('Tax Window')
    tax_root.geometry('300x200')
    tax_root.grab_set()
    tax_percentage=Label(tax_root,text='Enter Tax Percentage(%)',font=('arial',12))
    tax_percentage.pack(pady=10)
    tax_count=Spinbox(tax_root,from_ =0, to=100,font=('arial',12))
    tax_count.pack(pady=10)
    save_button = Button(tax_root, text='Save', font=('times new roman', 12, 'bold'),bg='#4d636d',fg='white',width=10,command=save_tax)
    save_button.pack(pady=20)

#for making sure that the frame are not more than one at a time
current_frame=None
def show_form(form_function):
    global current_frame
    if current_frame:
        current_frame.place_forget()
    current_frame=form_function(window)


#GUI part
window=Tk()
window.title('Dashboard')
window.geometry('1270x675+0+0')
window.resizable(0,0)
window.config(bg='white')

bg_image=PhotoImage(file='inventory.png')
titleLabel=Label(window,image=bg_image,compound=LEFT,text='   Inventory Management System',font=('times new roman',40,'bold'),bg='#010c48',fg='white',anchor='w',padx='20')
titleLabel.place(x=0,y=0,relwidth=1)
logoutButton=Button(window,text='Logout',font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100,y=10)

subtitleLabel=Label(window,text='Welcome Admin\t\t Date:10-05-2025\t\t Time: 07:12:50 pm',font=('times new roman',15),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)

leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=570)
logoImage=PhotoImage(file='logo.png')
imageLabel=Label(leftFrame,image=logoImage)
imageLabel.grid(row=0,column=0)
imageLabel.pack(fill=X)

employee_icon=PhotoImage(file='employee.png')
employee_button=Button(leftFrame,image=employee_icon,compound=LEFT,text=' Employees',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(employee_form))
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text=' Suppliers',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(supplier_form))
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text=' Categories',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(category_form))
category_button.pack(fill=X)

product_icon=PhotoImage(file='product.png')
product_button=Button(leftFrame,image=product_icon,compound=LEFT,text=' Products',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(product_form))
product_button.pack(fill=X)

tax_icon=PhotoImage(file='tax.png')
tax_button=Button(leftFrame,image=tax_icon,compound=LEFT,text='Tax',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:tax_window())
tax_button.pack(fill=X)

exit_icon=PhotoImage(file='exit.png')
exit_button=Button(leftFrame,image=exit_icon,compound=LEFT,text=' Exit',font=('times new roman',20,'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)

emp_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file='totalemp.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack()

total_emp_label=Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(emp_frame,text=0,bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()

sup_frame=Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file='totalsup.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#8E44AD')
total_sup_icon_label.pack(pady=10)

total_sup_label=Label(sup_frame,text='Total Suppliers',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
total_sup_label.pack()

total_sup_count_label=Label(sup_frame,text=0,bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.pack()

cat_frame=Frame(window,bg='#27AE60',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon=PhotoImage(file='totalcat.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#27AE60')
total_cat_icon_label.pack(pady=10)

total_cat_label=Label(cat_frame,text='Total Categories',bg='#27AE60',fg='white',font=('times new roman',15,'bold'))
total_cat_label.pack()

total_cat_count_label=Label(cat_frame,text=0,bg='#27AE60',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()

prod_frame=Frame(window,bg='#298089',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file='totalprod.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#298089')
total_prod_icon_label.pack(pady=10)

total_prod_label=Label(prod_frame,text='Total Products',bg='#298089',fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_count_label=Label(prod_frame,text=0,bg='#298089',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.pack(pady=10)

update()

window.mainloop()
