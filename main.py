import covid_tracker
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window=Tk()
window.minsize(300,300)
window.title("Covid Tracker")

logo=PhotoImage(file="D:\Covid_Tracer\Image\images.png")
window.iconphoto(False,logo)

imageLabel=Label(window,image=logo)
imageLabel.grid()


textLabel=Label(window, text="Enter name of Coumtry:")
textLabel.grid()

countryName=StringVar()
entry=Entry(window,width=30,textvariable=countryName)
entry.grid()

def getCases():
    nameOfCountry=countryName.get()
    response=covid_tracker.perform_request(nameOfCountry)
    messagebox.showinfo("Covid Data","Confirmed:"+str(response[0]["confirmed"])+"\nRecovered:"+str(response[0]["recovered"]))

getCaseButton=Button(window,text="Get Data",command=getCases)
getCaseButton.grid()

mainloop()

