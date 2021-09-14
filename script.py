"""
Program that stores book information:
Title, Author
Year, ISBN

User can: 
View records
Search for an entry
Add, Update, Delete & Close
"""

from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, author_text)
e2.grid()

year_text = StringVar()
e3 = Entry(window, year_text)
e3.grid()


window.mainloop()