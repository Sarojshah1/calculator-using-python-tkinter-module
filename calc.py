from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("342x384")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression) 
 
# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
def bt_back():
    global expression
    val = str(expression) 
    upval=val[:-1]
    expression = upval
    input_text.set(expression)
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=312, height=50, border=4, bg="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('poppins', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=1, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=12) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=275, bg="#00827F")
 
btns_frame.place(x=5,y=80)
 
# first row
 
clear = Button(btns_frame, text = "C", fg = "white", width = 10, height = 3, bd = 2, bg = "red", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, padx = 1, pady = 2)
back = Button(btns_frame, text = "X", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: bt_back()).grid(row = 0, column = 3, padx = 1, pady = 1)
sq = Button(btns_frame, text = "^", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 0, column =1, padx = 2, pady = 1)
mod = Button(btns_frame, text = "%", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 0, column =2, padx = 2, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 2,bg = "black", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 2,bg = "black", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 2,bg = "black", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 2,bg = "black", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 4, column =2, padx = 2, pady = 1)
equals = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 2, bg = "green", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

 
win.mainloop()
