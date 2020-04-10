import tkinter as tk
from tkinter import messagebox
import os
import sqlite3
from sqlite3 import Error

def exit():
    gui.destroy()

def testCon():

    try:

        con = sqlite3.connect('policedb.db')

        message = "Connection is established: Database is policedb.db"
        title = "Connection Successful"

        tk.messagebox.showinfo(title= title, message= message)

    except Error:

        print(Error)



con = sqlite3.connect('policedb.db')
cursorObj = con.cursor()
#cursorObj.execute("CREATE TABLE weaponLog (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, cottage TEXT, shift TEXT, licenseNumber TEXT, expDate TEXT, weaponSerialNumberTEXT, weaponMake TEXT, caliber TEXT, tagNumber TEXT, county	TEXT, tagState	TEXT)")
### Trying it without the id autoincrement
#cursorObj.execute("CREATE TABLE weaponLog (employeeName TEXT, department TEXT, cottage TEXT, shift TEXT, licenseNumber TEXT, expDate TEXT, weaponSerialNumber TEXT, weaponMake TEXT, caliber TEXT, tagNumber TEXT, county TEXT, tagState TEXT)"

def save():

    nameData = nameBox.get()
    departmentData = departmentBox.get()
    cottageData = cottageBox.get()
    shiftData = shiftBox.get()
    licenseData = licenseBox.get()
    experationData = experationBox.get()
    serialData = serialBox.get()
    makeData = makeBox.get()
    caliberData = caliberBox.get()
    tagData = tagBox.get()
    countyData = countyBox.get()
    stateData = stateBox.get()
    
    try:

        ##cursorObj.execute("INSERT INTO weaponLog VALUE("+ nameData+","+ departmentData + "," + cottageData + "," + shiftData + "," + licenseData + "," +  experationData + "," + serialData + "," + makeData + "," + caliberData + "," + tagData + "," + countyData + "," + stateData + ")")
        cursorObj.execute("INSERT INTO weaponLog (employeeName, department, cottage, shift, licenseNumber, expDate, weaponSerialNumber, weaponMake, caliber, tagNumber, county, tagState) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (nameData, departmentData, cottageData, shiftData, licenseData, experationData, serialData, makeData, caliberData, tagData, countyData, stateData))
        con.commit()
    except Error:

        print("Something went wrong")

gui = tk.Tk()
gui.title("Hudspeth Regional Center Campus Police Weapon Log")
gui.geometry("")


photo = tk.PhotoImage(file = "logo150.gif")

"""Top section of gui"""

menubar = tk.Menu(gui)
optionmenu = tk.Menu(menubar, tearoff=0)
optionmenu.add_command(label="Search") ###Add Search function later
optionmenu.add_command(label="Test Connection", command = testCon)
optionmenu.add_command(label="Exit", command=gui.quit)
#### Add a 'new' button which deletes all the text. 
optionmenu.add_cascade(label="Menu", menu=optionmenu)
gui.config(menu=menubar)


header = tk.Label(gui, text = "Hudspeth Regional Center \nWeapon Information", font=("Helvetica", 20))
logo = tk.Label(gui, image=photo, padx=25)
logo.photo = photo

"""Main section of gui"""

nameLbl = tk.Label(gui, text="Name: ", pady=10)
nameBox = tk.Entry(gui)
departmentLbl = tk.Label(gui, text="Department: ", pady=10)
departmentBox = tk.Entry(gui)
cottageLbl = tk.Label(gui, text="Cottage: ", pady=10)
cottageBox = tk.Entry(gui)
shiftLbl = tk.Label(gui, text="Shift: ", pady=10)
shiftBox = tk.Entry(gui)
licenseLbl = tk.Label(gui, text="Driver's License#: ", pady=10)
licenseBox = tk.Entry(gui)
experationLbl = tk.Label(gui, text="Exp. Date: ", pady=10)
experationBox = tk.Entry(gui)
serialLbl = tk.Label(gui, text="Weapon Serial Number: ", pady=10)
serialBox = tk.Entry(gui)
makeLbl = tk.Label(gui, text="Make/Model of Weapon: ", pady=10)
makeBox = tk.Entry(gui)
caliberLbl = tk.Label(gui, text="Caliber: ", pady=10)
caliberBox = tk.Entry(gui)
tagLbl = tk.Label(gui, text="Tag #: ", pady=10)
tagBox = tk.Entry(gui)
countyLbl = tk.Label(gui, text="County: ", pady=10)
countyBox = tk.Entry(gui)
stateLbl = tk.Label(gui, text="State: ", pady=10)
stateBox = tk.Entry(gui)
testBtn = tk.Button(gui, text="Test Connection", command=testCon)
closeBtn = tk.Button(gui, text="Exit", command=exit)
saveBtn = tk.Button(gui, text="Save", command=save)



"""Grid manager, where I place everything"""

logo.grid(column="1", row="0")
header.grid(column="3", row="0", columnspan="2")

nameLbl.grid(column="0", row="3")
nameBox.grid(column="1",row="3")
nameBox.focus_set()
departmentLbl.grid(column="0", row="4")
departmentBox.grid(column="1", row="4")
cottageLbl.grid(column="2", row="4")
cottageBox.grid(column="3", row="4")
shiftLbl.grid(column="4", row="4")
shiftBox.grid(column="5", row="4")
licenseLbl.grid(column="0", row="5")
licenseBox.grid(column="1", row="5")
experationLbl.grid(column="2", row="5")
experationBox.grid(column="3",row="5")
serialLbl.grid(column="0", row="6")
serialBox.grid(column="1", row="6")
makeLbl.grid(column="0", row="7")
makeBox.grid(column="1", row="7")
caliberLbl.grid(column="2", row="7")
caliberBox.grid(column="3", row="7")
tagLbl.grid(column="0", row="8")
tagBox.grid(column="1", row="8")
countyLbl.grid(column="2", row="8")
countyBox.grid(column="3", row="8")
stateLbl.grid(column="0", row="9")
stateBox.grid(column="1",row="9")
testBtn.grid(column="3", row="10")
saveBtn.grid(column="4", row="10")


gui.mainloop()