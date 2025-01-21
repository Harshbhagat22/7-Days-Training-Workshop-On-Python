import tkinter as tk 
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("CALCULATOR")
frame = tk.Frame(master = window,bg="black",padx=120)
frame.pack()
# entry 
entry = tk.Entry(master = frame,relief=SUNKEN,borderwidth=3,width=40)
entry.grid(row=0,column=0,columnspan=3,ipady=2,padx=2)

def addButton(num):
    entry.insert(tk.END,num)
    

def calculate():
    try:
        y = str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
        
    except:
        tkinter.messagebox.showinfo("ERROR :","System Error :")
    
    
def clear():
    entry.delete(0,tk.END)

button_1 = tk.Button(master = frame,text='1',padx=20,pady=5,width=3,command=lambda:addButton(1))
button_1.grid(row=1,column=0,pady=2)

button_2 = tk.Button(master = frame,text='2',padx=20,pady=5,width=3,command=lambda:addButton(2))
button_2.grid(row=1,column=1,pady=2)

button_3 = tk.Button(master = frame,text='3',padx=20,pady=5,width=3,command=lambda:addButton(3))
button_3.grid(row=1,column=2,pady=2)

button_4 = tk.Button(master = frame,text='4',padx=20,pady=5,width=3,command=lambda:addButton(4))
button_4.grid(row=2,column=0,pady=2)

button_5 = tk.Button(master = frame,text='5',padx=20,pady=5,width=3,command=lambda:addButton(5))
button_5.grid(row=2,column=1,pady=2)

button_6 = tk.Button(master = frame,text='6',padx=20,pady=5,width=3,command=lambda:addButton(6))
button_6.grid(row=2,column=2,pady=2)

button_7 = tk.Button(master = frame,text='7',padx=20,pady=5,width=3,command=lambda:addButton(7))
button_7.grid(row=3,column=0,pady=2)

button_8 = tk.Button(master = frame,text='8',padx=20,pady=5,width=3,command=lambda:addButton(8))
button_8.grid(row=3,column=1,pady=2)

button_9 = tk.Button(master = frame,text='9',padx=20,pady=5,width=3,command=lambda:addButton(9))
button_9.grid(row=3,column=2,pady=2)

button_0 = tk.Button(master = frame,text='0',padx=20,pady=5,width=3,command=lambda:addButton(0))
button_0.grid(row=4,column=0,pady=2)

button_add = tk.Button(master = frame,text='+',padx=20,pady=5,width=3,command=lambda:addButton('+'))
button_add.grid(row=5,column=0,pady=2)

button_sub = tk.Button(master = frame,text='-',padx=20,pady=5,width=3,command=lambda:addButton('-'))
button_sub.grid(row=5,column=1,pady=2)

button_multi = tk.Button(master = frame,text='*',padx=20,pady=5,width=3,command=lambda:addButton('*'))
button_multi.grid(row=5,column=2,pady=2)

button_div = tk.Button(master = frame,text='/',padx=20,pady=5,width=3,command=lambda:addButton('/'))
button_div.grid(row=6,column=0,pady=2)

button_eq = tk.Button(master = frame,text='=',padx=20,pady=5,width=3,command=lambda:addButton('='))
button_eq.grid(row=6,column=1,pady=2)

button_clear = tk.Button(master=frame,text='clear',padx=25,pady=5,command=clear)
button_clear.grid(row=6,column=2,columnspan=3,pady=2)

button_equal= tk.Button(master=frame,text='equal',padx=25,pady=5,command=eval)
button_equal.grid(row=6,column=2,columnspan=3,pady=2)

window.mainloop()







