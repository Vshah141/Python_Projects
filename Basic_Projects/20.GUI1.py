import tkinter

window=tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(width=500,height=500)

label1=tkinter.Label(text="   ")
label1.grid(column=0,row=0)

input=tkinter.Entry(width=10)
input.grid(column=1,row=0)
label2=tkinter.Label(text="Miles")
label2.grid(column=2,row=0)
label3=tkinter.Label(text="is equal to")
label3.grid(column=0,row=1)
label4=tkinter.Label(text="Km")
label4.grid(column=2,row=1)
label5=tkinter.Label(text="0")
label5.grid(column=1,row=1)


def onclick():
    miles=float(input.get())
    x=miles*1.60
    label5["text"]=x
    
button=tkinter.Button(text="Calculate",command=onclick)
button.grid(column=1,row=2)
 








window.mainloop()