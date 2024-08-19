from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def square_root():
    try:
        global expression
        val = float(expression)
        equation.set(val ** 0.5)
        expression = ""
    except:
        expression = ""

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")
if __name__  == "__main__":
    win = Tk()
    win.configure(background="gray")
    win.title("CalCulator")
    # "350*350+400+200"
    win.geometry()
    equation = StringVar()
    expression_field = Entry(win, textvariable=equation,width=35,relief=RIDGE,bd=10,insertwidth=1,font= 40 ).grid(columnspan=4, ipadx=1)
    Button1 = Button(win,text='1',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(1),height=2,width=7).grid(row=2,column=0)
    Button2 = Button(win,text='2',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(2),height=2,width=7).grid(row=2,column=1)
    Button3 = Button(win,text='3',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(3),height=2,width=7).grid(row=2,column=2)
    Button4 = Button(win,text='4',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(4),height=2,width=7).grid(row=3,column=0)
    Button5 = Button(win,text='5',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(5),height=2,width=7).grid(row=3,column=1)
    Button6 = Button(win,text='6',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(6),height=2,width=7).grid(row=3,column=2)
    Button7 = Button(win,text='7',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(7),height=2,width=7).grid(row=4,column=0)
    Button8 = Button(win,text='8',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(8),height=2,width=7).grid(row=4,column=1)
    Button9 = Button(win,text='9',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(9),height=2,width=7).grid(row=4,column=2)
    Button0 = Button(win,text='0',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press(0),height=2,width=7).grid(row=5,column=0)
    plus = Button(win,text='+',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press("+"),height=2,width=7).grid(row=2,column=3)
    minus = Button(win,text='-',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press("-"),height=2,width=7).grid(row=3,column=3)
    multiply = Button(win,text='*',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press("*"),height=2,width=7).grid(row=4,column=3)
    divide = Button(win,text='/',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press("/"),height=2,width=7).grid(row=5,column=3)
    equal = Button(win,text='=',fg='white',bg='#0052cc',font='Arial 15',command=equalpress,height=2,width=7).grid(row=5,column=2)
    clear = Button(win,text='c',fg='white',bg='#0052cc',font='Arial 15',command=clear,height=2,width=7).grid(row=5,column=1)
    Decimal = Button(win,text='.',fg='white',bg='#0052cc',font='Arial 15',command=lambda: press('.'),height=2,width=7).grid(row=6,column=0)
    SQroot = Button(win,text='/u221a',fg='white',bg='#0052cc',font='Arial 15',command=square_root,height=2,width=7).grid(row=6,column=0)
win.mainloop()


