import tkinter as tk

expression = ''
expr = ''
ex = ''
def printn(n):
    global label2
    global expression
    expression = (expression + '%d' % n)
    label2.config(text=expression)

def clr():
    global label2
    global expression
    expression = ''
    label2.config(text=expression)

def calc(ex):
    i = expression.find(ex)
    if(i==0):
        raise ValueError
    else:
        if (expression[i] == "+"):
            var1 = expression[:i]
            var2 = expression[i + 1:]
            sum = int(var1) + int(var2)
            return sum
        elif (expression[i] == "-"):
            var1 = expression[:i]
            var2 = expression[i + 1:]
            sum = int(var1) - int(var2)
            return sum
        elif (expression[i] == "*"):
            var1 = expression[:i]
            var2 = expression[i + 1:]
            sum = int(var1) * int(var2)
            return sum
        elif (expression[i] == "/"):
            var1 = expression[:i]
            var2 = expression[i + 1:]
            if(var2==0):
                raise ZeroDivisionError
            else:
                sum = int(var1) / int(var2)
                return sum

def operator(op):
    global label2
    global expression
    global expr
    global ex
    if (op == "+"):
        expr=(expr+'%s'%op)
        expression = (expression + '%s' % op)
        label2.config(text=expression)
    elif (op == "-"):
        expr = (expr + '%s' % op)
        expression = (expression + '%s' % op)
        label2.config(text=expression)
    elif (op == "*"):
        expr = (expr + '%s' % op)
        expression = (expression + '%s' % op)
        label2.config(text=expression)
    elif (op == "/"):
        expr = (expr + '%s' % op)
        expression = (expression + '%s' % op)
        label2.config(text=expression)
    elif (op == "="):
        try:
            ex=(ex + '%s' %expr)
            val = calc(ex)
            label2.config(text=val)
            expression = ' '
            ex=''
            expr=''
        except ZeroDivisionError:
            expression=''
            expression= (expression+' cannot be divided by zero')
            label2.config(text=expression)
        except ValueError:
            expression = ''
            expression = (expression + ' please enter a valid number')
            label2.config(text=expression)
mainWindow = tk.Tk()

label1 = tk.Label(mainWindow, text='Calculator')
label1.config(bg='grey', font=('arial', 36, 'bold'))
label1.grid(row=1, columnspan=3, ipadx=100, ipady=5, padx=5, pady=5)
label2 = tk.Label(mainWindow)
label2.config(bg='white', height=1, width=95, relief='sunken')
label2.grid(row=2, columnspan=4, ipadx=5, ipady=5, padx=5, pady=5)

button = tk.Button(mainWindow, text='=', command=lambda: operator("="), height=2, width=5)
button.config(bg='red', font=('bold'))
button.grid(row=6, column=1, padx=5, pady=10)
buttonc = tk.Button(mainWindow, text='DEL', command=lambda: clr(), height=2, width=5)
buttonc.config(font=('bold'))
buttonc.grid(row=6, column=2, padx=5, pady=10)

button1 = tk.Button(mainWindow, text='1', command=lambda: printn(1), height=2, width=5)
button1.grid(row=3, column=0, padx=5, pady=10)
button2 = tk.Button(mainWindow, text='2', command=lambda: printn(2), height=2, width=5)
button2.grid(row=3, column=1, padx=5, pady=10)
button3 = tk.Button(mainWindow, text='3', command=lambda: printn(3), height=2, width=5)
button3.grid(row=3, column=2, padx=5, pady=10)
button4 = tk.Button(mainWindow, text='4', command=lambda: printn(4), height=2, width=5)
button4.grid(row=4, column=0, padx=5, pady=10)
button5 = tk.Button(mainWindow, text='5', command=lambda: printn(5), height=2, width=5)
button5.grid(row=4, column=1, padx=5, pady=10)
button6 = tk.Button(mainWindow, text='6', command=lambda: printn(6), height=2, width=5)
button6.grid(row=4, column=2, padx=5, pady=10)
button7 = tk.Button(mainWindow, text='7', command=lambda: printn(7), height=2, width=5)
button7.grid(row=5, column=0, padx=5, pady=10)
button8 = tk.Button(mainWindow, text='8', command=lambda: printn(8), height=2, width=5)
button8.grid(row=5, column=1, padx=5, pady=10)
button9 = tk.Button(mainWindow, text='9', command=lambda: printn(9), height=2, width=5)
button9.grid(row=5, column=2, padx=5, pady=10)
button0 = tk.Button(mainWindow, text='0', command=lambda: printn(0), height=2, width=5)
button0.grid(row=6, column=0, padx=5, pady=10)

buttonm = tk.Button(mainWindow, text='-', command=lambda: operator("-"), height=2, width=7)
buttonm.grid(column=3, row=3, padx=5, pady=10)
buttonp = tk.Button(mainWindow, text='+', command=lambda: operator("+"), height=2, width=7)
buttonp.grid(column=3, row=4, padx=5, pady=10)
buttonmu = tk.Button(mainWindow, text='*', command=lambda: operator("*"), height=2, width=7)
buttonmu.grid(column=3, row=5, padx=5, pady=10)
buttond = tk.Button(mainWindow, text='/', command=lambda: operator("/"), height=2, width=7)
buttond.grid(column=3, row=6, padx=5, pady=10)


mainWindow.mainloop()