from tkinter import *

root  = Tk()
root.config(bg='#400080')
root.resizable(0, 0)

#root.overrideredirect(True)

message = Label(root, text="From", bg = '#400080', 
                width = 15,height=3,
                fg='white').grid( row = 1, column = 0)
message1 = Label(root, text="To", bg = '#400080', 
                width = 15,height=3,
                fg='white').grid( row = 2, column = 0)
message2 = Label(root, text="Enter value", 
                 bg = '#400080', width = 15,height=3,
                 fg='white').grid( row = 10, column = 0)
message3 = Label(root, text="Final value", bg = '#400080', 
                 width = 15,height=3,
                 fg='white').grid( row = 10, column = 3)
message4 = Label(root, text="NUMBER\nSYSTEM CONVERTOR", 
                 bg = '#400080',height=3,fg='white'
                ,font=("Times New Roman", 20),
                justify=LEFT).grid( row = 1, column = 2,rowspan=2,columnspan=3)

def clear_text1():
    global expression 
    expression = "" 
    input_text1.set("")

def clear_text2():
    global expression 
    expression = "" 
    input_text2.set("")

def clear_text3():
    global expression3 
    expression3 = "" 
    input_text3.set("")

def btn_click1(item):
    global expression1
    expression1 = str(item)
    input_text1.set(expression1)

def btn_click2(item):
    global expression2
    expression2 = str(item)
    input_text2.set(expression2)

def btn_click3(item):
    global expression3
    expression3 = expression3 + str(item)
    input_text3.set(expression3)

def btn_click4(item):
    global expression4
    expression4 = str(item)
    input_text4.set(expression4)

expression1 = ""
expression2 = ""
expression3 = ""
expression4 = ""

input_text1 = StringVar()
input_text2 = StringVar()
input_text3 = StringVar()
input_text4 = StringVar()

e=Entry(root,width=15,textvariable=input_text1)
e.grid(row=1,column=1)

e1=Entry(root,width=15,textvariable=input_text2)
e1.grid(row=2,column=1)

e2=Entry(root,width=15,textvariable=input_text3)
e2.grid(row=10,column=1)

button_min = Button(root, text="Minimise", width = 15,
                     height = 3)#, command = lambda: min_win())
button_close = Button(root, text="Close", width = 15,
                       height = 3, command = lambda:root.destroy())
button_1 = Button(root, text="Binary", width = 15,
                   height = 3, command = lambda: btn_click1('Binary'))
button_2 = Button(root, text="Decimal", width = 15,
                   height = 3, command = lambda: btn_click1('Decimal'))
button_3 = Button(root, text="Octal", width = 15,
                   height = 3, command = lambda: btn_click1('Octal'))
button_4 = Button(root, text="Hexadecimal", width = 15
                  , height = 3, command = lambda: btn_click1('Hexadecimal'))
button_5 = Button(root, text="Binary", width = 15,
                   height = 3, command = lambda: btn_click2('Binary'))
button_6 = Button(root, text="Decimal", width = 15,
                   height = 3, command = lambda: btn_click2('Decimal'))
button_7 = Button(root, text="Octal", width = 15,
                   height = 3, command = lambda: btn_click2('Octal'))
button_8 = Button(root, text="Hexadecimal", width = 15, height = 3, 
                  command = lambda: btn_click2('Hexadecimal'))
button_9 = Button(root, text="Clear ALL", width= 15, height=3,
                  command = lambda:[clear_text1(), clear_text2(),clear_text3()])
button_10 = Button(root, text="=", width= 15, height=3,
                   command = lambda:[done_clicked()])
button_A = Button(root, text="A", width = 15, height = 3,
                   command = lambda: btn_click3('a'),font=("Helvetica", 9))
button_B = Button(root, text="B", width = 15, height = 3,
                   command = lambda: btn_click3('b'))
button_C = Button(root, text="C", width = 15, height = 3,
                   command = lambda: btn_click3('c'))
button_D = Button(root, text="D", width = 15, height = 3,
                   command = lambda: btn_click3('d'))
button_E = Button(root, text="E", width = 15, height = 3,
                   command = lambda: btn_click3('e'))
button_F = Button(root, text="F", width = 15, height = 3,
                   command = lambda: btn_click3('f'))
button_11 = Button(root, text="1", width = 15, height = 3,
                    command = lambda: btn_click3('1'))
button_12 = Button(root, text="2", width = 15, height = 3,
                    command = lambda: btn_click3('2'))
button_13 = Button(root, text="3", width = 15, height = 3,
                    command = lambda: btn_click3('3'))
button_14 = Button(root, text="4", width = 15, height = 3,
                    command = lambda: btn_click3('4'))
button_15 = Button(root, text="5", width = 15, height = 3,
                    command = lambda: btn_click3('5'))
button_16 = Button(root, text="6", width = 15, height = 3,
                    command = lambda: btn_click3('6'))
button_17 = Button(root, text="7", width = 15, height = 3,
                    command = lambda: btn_click3('7'))
button_18 = Button(root, text="8", width = 15, height = 3,
                    command = lambda: btn_click3('8'))
button_19 = Button(root, text="9", width = 15, height = 3,
                    command = lambda: btn_click3('9'))
button_20 = Button(root, text="0", width = 15, height = 3,
                    command = lambda: btn_click3('0'))
button_21 = Button(root, text="Clear user value", width= 15,
                    height=3,command = lambda:[clear_text3()])
button_22 = Button(root, text="Information", width= 15, height=3,
                   command = lambda:[information_123()])

def information_123():
    ws = Tk()
    ws.config(bg='#400080')
    Label(ws, text=
    " This project is created by Priyansh Raj Gupta\n for Python skill based",
    font=("Times New Roman", 14),
    fg ='#400080',bg='white').pack(pady=20)
    ws.overrideredirect(True)
    ws.after(5000,lambda:ws.destroy()) #Closing the window after 5 seconds :)
    ws.mainloop()

button_close.grid(row=3,column=1)
button_min.grid(row=3,column=0)
button_1.grid(row=4,column=0)
button_2.grid(row=5,column=0)
button_3.grid(row=6,column=0)

button_4.grid(row=7,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=5,column=1)

button_7.grid(row=6,column=1)
button_8.grid(row=7,column=1)
button_9.grid(row=8,column=0)
button_10.grid(row=8,column=1)

button_A.grid(row=3,column=2)
button_B.grid(row=3,column=3)
button_C.grid(row=3,column=4)
button_D.grid(row=4,column=2)
button_E.grid(row=4,column=3)
button_F.grid(row=4,column=4)

button_11.grid(row=7,column=2)
button_12.grid(row=7,column=3)
button_13.grid(row=7,column=4)
button_14.grid(row=6,column=2)
button_15.grid(row=6,column=3)
button_16.grid(row=6,column=4)
button_17.grid(row=5,column=2)
button_18.grid(row=5,column=3)
button_19.grid(row=5,column=4)
button_20.grid(row=8,column=2)
button_21.grid(row=8,column=3)
button_22.grid(row=8,column=4)

def done_clicked():
    prefix_value = e.get()
    a = str(prefix_value)

    prefix_value1 = e1.get()
    b = str(prefix_value1)

    prefix_value2 = e2.get()
    c = str(prefix_value2)

    #Binary to decimal
    if a == 'Binary' and b =='Decimal':
        decimal_number_3 = int(c,2)

    #Binary to octal
    elif a =='Binary' and b=='Octal':
        decimal_number_3 = oct(int(c,2))
    
    #Binary to Hexadecimal
    elif a=='Binary' and b=='Hexadecimal':
        decimal_number_3 = hex(int(c,2))
    
    #Binary to Binary
    elif a=='Binary' and b=='Binary':
        decimal_number_3 = c
    
    #Decimal to Decimal
    elif a=='Decimal' and b=='Decimal':
        decimal_number_3 = c
    
    #Decimal to Binary
    elif a=='Decimal' and b=='Binary':
        decimal_number_3 = bin(int(c))
    
    #Decimal to Hexadecimal
    elif a=='Decimal' and b=='Hexadecimal':
        decimal_number_3 = hex(int(c))
    
    #Decimal to Octal
    elif a=='Decimal' and b=='Octal':
        decimal_number_3 = oct(int(c))
    
    #Hexadecimal to Hexadecimal
    elif a=='Hexadecimal' and b=='Hexadecimal':
        decimal_number_3 = c
    
    #Hexadecimal to Binary
    elif a=='Hexadecimal' and b=='Binary':
        a = int(c,16)
        decimal_number_3 = bin(a)

    #Hexadecimal to Decimal
    elif a=='Hexadecimal' and b=='Decimal':
        decimal_number_3 = int(c,16)
    
    #Hexadecimal to Octal
    elif a=='Hexadecimal' and b=='Octal':
        a = int(c,16)
        decimal_number_3 = oct(a)
    
    #Octal to Octal
    elif a=='Octal' and b=='Octal':
        decimal_number_3 = c
    
    #Octal to Binary 
    elif a=='Octal' and b=='Binary':
        decimal_number_3 = bin(int(c,8))
   
    #Octal to Decimal
    elif a=='Octal' and b=='Decimal':
        decimal_number_3 = int(c,8)
    
    #Octal to Hexadecimal
    elif a=='Octal' and b=='Hexadecimal':
        a = int(c,8)
        decimal_number_3 = hex(a)

    elif a=='' or b==''or c=='':
        ws = Tk()
        ws.overrideredirect(True)
        message = Label(ws, text="Please Enter Correct value"
                        , bg = '#400080',fg='white',
                        font=("Times New Roman",
                         14)).grid( row = 0, column = 0)
        ws.after(5000,lambda:ws.destroy())
        ws.mainloop()


    e3=Label(root,width=15,text=decimal_number_3)
    e3.grid(row=10,column=4)

root.mainloop()