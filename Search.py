from tkinter import *
root= Tk()
root.geometry('600x400')
sum_var= StringVar()

def entry_Fn():
    level_1 = Toplevel(root)
    Label( level_1, text = "level one").pack()
    entry_1 = Entry(level_1)
    entry_1.pack()
    entry_2 = Entry(level_1)
    entry_2.pack()
    def submitBtn():
        val_1= entry_1.get()
        val_2= entry_2.get()
        sum_var.set(int(val_1)+ int(val_2))
        level_1.destroy()
    Button(level_1, text= "submit", command=submitBtn).pack()


Label(root, text = "Main window").pack()
Button(root, text= "To enter Data", command= entry_Fn).pack()
sum = Label(root, textvariable = sum_var)
sum.pack()

root.mainloop()