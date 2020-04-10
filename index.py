import tkinter as tk
import os





gui = tk.Tk()
gui.title("Hudspeth Regional Center Campus Police Weapon Log")
gui.geometry("")
txbx = tk.Text(gui)

photo = tk.PhotoImage(file = "logo150.gif")


header = tk.Label(gui, text = "Hudspeth Regional Center \nWeapon Information", font=("Helvetica", 20))
logo = tk.Label(gui, image=photo, padx=25)
logo.photo = photo
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
pdfBtn = tk.Button(gui, text="Save as PDF", command=pdf)


logo.grid(column="1", row="0")
header.grid(column="3", row="0", columnspan="2")

nameLbl.grid(column="0", row="3")
nameBox.grid(column="1",row="3")
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
pdfBtn.grid(column="3", row="10")
gui.mainloop()