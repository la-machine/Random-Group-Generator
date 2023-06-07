from tkinter import *
from random import shuffle
# from tkinter import messagebox 


numgroup=0
i=0
n=0
cnt=0

def Number():
    Num = int(input())

def names():
    name = [input() for i in range(EntryNum)]


def delete():
    global n, i, cnt
    n=0
    i=0
    cnt=0
    name=[]
    EntryGroup.delete(0,END)
    EntryNum.delete(0,END)
    EntryName.delete(0, END)
    LabelErr=Label(root, text="                                                                                                                                 ")

    

def OK2():
    global n, numgroup
    EntryName.config(state='normal')
    n=int(EntryNum.get())

    EntryGroup.config(state='normal')
    numgroup=int(EntryGroup.get())
    if (numgroup>n)or(numgroup<0):
        LabelErr=Label(root, text="The number of group should be greather than zero \n and less than the number of people in the group",
        font=("bold",7), fg="red", pady=0)
        LabelErr.grid(row=2,column=2)
    else:
        LabelErr=Label(root, text="")


def do():
    global i, n
    name.append(EntryName.get())
    i+=1
    EntryName.delete(0, END)
    if n == i:
        EntryName.config(state='disabled')


def action():
    global n
    Box.delete("1.0", "end")
    shuffle(name)
    mem=int(EntryGroup.get())
    
    m=int((n/mem))
    
    index=0
    num=1
    d=n%mem
    r=n-d
    group=[]
    g=[]
    if (n==0) or (EntryGroup.get()==0):
        EntryName.config(state='disabled')

    else:

	    for i in range(mem):
		    for j in range(m):
			    if len(name)>=1:
				    temp=name.pop()
			    if temp not in group:
				    group.append(temp)
		    if group not in g:
			    g.append(group)
			    group=[]
	    for x in range(d):
		    if len(name)>=1:
			    temp=name.pop()
		    if temp not in g:
			    g[x].append(temp)
	    i=0
	    for i in range(0,mem):
		    j=0
		    if i<d: 
			    for j in range(0,m+1):
				    Box.insert(INSERT, j+1)
				    Box.insert(INSERT, ". ")
				    Box.insert(INSERT, g[i][j])
				    Box.insert(INSERT, "\n")
		    else:
			    for j in range(0,m):
				    Box.insert(INSERT, j+1)
				    Box.insert(INSERT, ". ")
				    Box.insert(INSERT, g[i][j])
				    Box.insert(INSERT, "\n")
		    Box.insert(INSERT, "\n")

root = Tk()
root.geometry("700x350")
root.title('Random Selection')


LabelNum = Label(root, text="Enter the Number of Students", font=('bold', 14), pady=20)
LabelNum.grid(row=0, column= 0)
EntryNum = Entry(root,textvariable=LabelNum, bg="white", fg="black")
EntryNum.grid(row=0, column=1)



LabelGroup = Label(root, text="Enter the Number of Groups", font=('bold', 14), pady=10)
LabelGroup.grid(row=1, column= 0)
EntryGroup = Entry(root,textvariable=LabelGroup, bg="white", fg="black")
EntryGroup.grid(row=1, column=1)

Button2 = Button(root, text='OK', command=OK2)
Button2.grid(row=1, column=2)


LabelName = Label(root, text="Enter the Student's name", font=('bold', 14), pady=10)
LabelName.grid(row=3, column= 0)
EntryName = Entry(root,textvariable=LabelName, bg="white", fg="black")
EntryName.grid(row=3, column=1)

name=[]
Btn = Button(root, text='Generate Groups', command=action)
Btn.place(x=50, y=190)
btn1 = Button(root, text="Resert", command=delete)
btn1.place(x=200, y=190)

Button = Button(root, text='Assign', command=do)
Button.grid(row=3, column=2)
count=Text(root, height=1, width=3)
count.grid(row=3, column=4)


Box = Text(root, height=29, width=150, bg="white", fg="black")
Box.place(x=50, y=220)



root.mainloop()
