from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import*
window = Tk()
window.geometry("600x300")
window.title("Memorizer")
def deleting():
    index= lists.curselection()
    if index:
        lists.delete(index)

def adding():
    lists.insert(END,enter.get())
    enter.delete(0,END)

def saving():
    outcome= asksaveasfile(defaultextension=".txt")
    if outcome is not None:
        for item in lists.get(0,END):
            print(item.strip(),file=outcome)
        lists.delete(0,END)

def opening():
    income = askopenfile(title="openfile")
    if income is not None:
        lists.delete(0,END)
        items= income.readlines()
        for item in items:
            lists.insert(END,item.strip())

save = Button(window,text="Save",command= saving)
enter = Entry(window)
add = Button(window,text="Add",command=adding)
open = Button(window,text="Open",command=opening)
frame = Frame(window)
scroll= Scrollbar(frame,orient="vertical")
lists = Listbox(frame,width= 70, yscrollcommand=scroll.set, bg="light blue")
for i in range(1,101):
    lists.insert(END,"LIST"+str(i))
frame.grid(row=3,column=1)
scroll.config(command=lists.yview)
lists.grid(row=3,column=1)
scroll.grid(row=3,column=2)
delete = Button(window,text="Delete",command=deleting)
save.grid(row=0,column=1)
enter.grid(row=1,column=1)
add.grid(row=2,column=1)
open.grid(row=3,column=0)
delete.grid(row=3,column=2)
window.mainloop()