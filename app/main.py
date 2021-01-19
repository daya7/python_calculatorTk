from tkinter import *
import parser
root = Tk()
root.title("calculator")

# Input Fields
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#functions
i = 0


def getnumbers(n):
    global i
    display.insert(i, n)
    i += 1

def getoperation(op):
    global i
    op_length = len(op)
    display.insert(i, op)
    i+=op_length
    
def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, 'Error')

def clear_display():
 	display.delete(0,END)
 	
def undo():
 	display_state= display.get()
 	if len(display_state):
 		new_display= display_state[:-1]
 		clear_display()
 		display.insert(0, new_display)
 		
 	else:
 		clear_display()
 		display.insert(0, 'Error')
 		

#buttons

# Numeric Buttons
Button(root, text="1", command=lambda: getnumbers(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2",  command=lambda: getnumbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3",  command=lambda: getnumbers(3)).grid(row=2, column=2, sticky=W+E)


Button(root, text="4",  command=lambda: getnumbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5",  command=lambda: getnumbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6",  command=lambda: getnumbers(6)).grid(row=3, column=2, sticky=W+E)
Button(root, text="7",  command=lambda: getnumbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8",  command=lambda: getnumbers(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9",  command=lambda: getnumbers(9)).grid(row=4, column=2, sticky=W+E)

# Bottom Buttons
Button(root, text="AC", command=lambda: clear_display()).grid(row=5, column=0)
Button(root, text="0", command=lambda: getnumbers(0)).grid(row=5, column=1)
Button(root, text="%", command=lambda: getoperation("%")).grid(row=5, column=2)

Button(root, text="+", command=lambda: getoperation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: getoperation("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: getoperation("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: getoperation("/")).grid(row=5, column=3, sticky=W+E)

# More Math Operators
Button(root, text="⟵", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda: getoperation("**")).grid(row=3, column=4)
Button(root, text="^2", command=lambda: getoperation("**2")).grid(row=3, column=5)
Button(root, text="(", command=lambda: getoperation("(")).grid(row=4, column=4,sticky=W+E)
Button(root, text=")", command=lambda: getoperation(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()