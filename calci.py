from tkinter import *

def butnClick(numbers):
    global operators
    operators=operators+str(numbers)
    text_Input.set(operators)
def btnClearDisplay():
    global operators
    operators =""
    text_Input.set("")
def btnEqualInput():
    global operators
    sum=str(eval(operators))
    text_Input.set(sum)

cal=Tk()
cal.title("Calculator")
operators=""
text_Input=StringVar()
operators=""


txtDisplay=Entry(cal,font=("Arial",25,"bold"),textvariable=text_Input,bd=30,insertwidth=4,
                 bg="powder blue",justify="right").grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="7",command=lambda:butnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="8",command=lambda:butnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="9",command=lambda:butnClick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="+",command=lambda:butnClick("+")).grid(row=1,column=3)
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="4",command=lambda:butnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="5",command=lambda:butnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="6",command=lambda:butnClick(6)).grid(row=2,column=2)
Subraction=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",25,"bold"),bg="powder blue",text="-",command=lambda:butnClick("-")).grid(row=2,column=3)
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="1",command=lambda:butnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="2",command=lambda:butnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="3",command=lambda:butnClick(3)).grid(row=3,column=2)
Multiplication=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",25,"bold"),bg="powder blue",text="*",command=lambda:butnClick("*")).grid(row=3,column=3)
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="0",command=lambda:butnClick(0)).grid(row=4,column=0)
btnClear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="C",command=btnClearDisplay).grid(row=4,column=1)
btEqual=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="powder blue",text="=",command= btnEqualInput).grid(row=4,column=2)
Division=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("Arial",25,"bold"),bg="powder blue",text="/",command=lambda:butnClick("/")).grid(row=4,column=3)



cal.mainloop()