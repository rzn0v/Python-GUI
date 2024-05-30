from tkinter import *

window = Tk()
window.title("My first GUI program")
window.config(padx=20, pady=20)

input = Entry()
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 =Label(text="Km")
label4.grid(column=2,row=1)

def to_km():
    miles = float(input.get())
    km = (1.60934)*miles
    output = int(km)
    label3.config(text=output)

button = Button(text="Calculate", command=to_km)
button.grid(column=1,row=2)


window.mainloop()