import calendar
from tkinter import *

#function to display calender
def DisplayCalender():
    newRoot = Tk()
    newRoot.title("Calender Screen")
    newRoot.config(bg="light blue")
    newRoot.geometry("700x700")
    actualYear = int(yearEntry.get())
    actualMonth = int(monthEntry.get())
    if actualMonth == 0:
        calenderContent = calendar.calendar(actualYear)
    else:
        calenderContent = calendar.month(actualYear, actualMonth)
    lblNew = Label(newRoot, text=calenderContent, font="Consolas 10 bold")
    lblNew.grid(row=0, column=0, padx=30, pady=30)
    newRoot.mainloop()


#designing first window
root = Tk()
root.config(bg="deep sky blue")
root.title("Calender App")
root.geometry("400x400")

header = Label(root, text="Calender", bg = "light pink", fg = "brown", font=("times", 28, "bold"))
header.grid(row=0, column=0, padx=25, pady=25)

lblY = Label(root, text="Enter Year: ")
lblY.grid(row=1, column=0, padx=25)

lblM = Label(root, text="Enter Month (To get full year calender enter 0): ")
lblM.grid(row=3, column=0, padx=25)

yearEntry = Entry(root, width=5)
yearEntry.grid(row=2, column=0, padx=25, pady = 10)

monthEntry = Entry(root, width=5)
monthEntry.grid(row=4, column=0, padx=25, pady = 10)

showcalender = Button(root, text="Show Calender", fg = "dark green", command = DisplayCalender)
showcalender.grid(row=5, column=0, padx=25)

exitButton = Button(root, text="Exit", fg = "purple", command=root.destroy)
exitButton.grid(row=6, column=0, padx=25)

root.mainloop()