"""
A promgram that stores book information:
Title, Author, Year, ISBN

User can:

Veiw all records
Can search an Entry
Add an Entery
Update and entry
delete
Close the application


Used Pyinstaller to create a single executable file
pyinstaller --onefile --windowed bookstore.py
--windowed removed commandline from background of gui - onefile keeps executable file as one not several
"""
from tkinter import *
#import backend
from oopbackend import Database

database=Database("books.db")

#event is a special parameter - hold info about type of event
#when passing through a bind method - expects function to have envet paramenter
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #populate fields with selected entry
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])#title
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2]) #author name
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3]) #year
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])#isbn
    except IndexError:
        pass



def view_command():
    list1.delete(0, END)
    for row in database.view():
        #END means new row will be put at the end
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window=Tk()
#labels for entry boxes

window.wm_title("Surens Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#entry boxes
title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

#text box for results
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#bind method to listbox widget - used bind a function to a widget event
list1.bind('<<ListboxSelect>>', get_selected_row)

#buttons
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
