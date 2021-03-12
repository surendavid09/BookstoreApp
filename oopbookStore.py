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

class Window(object):

    def __init__(self,window):
        self.window=window

        self.window.wm_title("Surens Book Store")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        #entry boxes
        self.title_text=StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.author_text=StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        #text box for results
        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        #bind method to listbox widget - used bind a function to a widget event
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #buttons
        b1=Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2=Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3=Button(window, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4=Button(window, text="Update Selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5=Button(window, text="Delete Selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6=Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            #populate fields with selected entry
            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_tuple[1])#title
            self.e2.delete(0,END)
            self.e2.insert(END, self.selected_tuple[2]) #author name
            self.e3.delete(0,END)
            self.e3.insert(END, self.selected_tuple[3]) #year
            self.e4.delete(0,END)
            self.e4.insert(END, self.selected_tuple[4])#isbn
        except IndexError:
            pass


    def view_command(self):
            self.list1.delete(0, END)
            for row in database.view():
                #END means new row will be put at the end
                self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])


    def update_command(self):
        database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window=Tk()
Window(window)
window.mainloop()
