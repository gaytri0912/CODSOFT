from tkinter import *
from tkinter import ttk

if __name__=="__main__":

    def addTask():
        word = tsk.get(1.0,END)
        tb.insert(END,word)
        with open('data.txt','a')  as file:
            file.write(word)
            file.seek(0)
            file.close()
        tsk.delete(1.0,END)
    
    
    def delOne():
        dele =  tb.curselection()
        look = tb.get(dele)
        with open ('data.txt','r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                item= str(look)
                if item not in line:
                    f.write(line)
            f.truncate()
        tb.delete(dele)
    with open('data.txt','r') as f:
        read=f.readline()
        for line in read:
            ready = line.split()
            #tb.insert(END,ready)
        f.close()
    
            


          
    task = []
    t=Tk()
    t.title("TODO List")
    t.geometry('300x260')
    t.configure(background="PowderBlue")
    t.resizable(False,False)
    lbl = Label(t, text = "Enter the task",font="times 12",foreground="Black",background="PowderBlue",padx=3)
    lbl.grid(column=0,row=0)
    tb=Listbox(t,selectmode="SINGLE",width=40)
    tsk=Text(t,width=20,height=1,font="Times 12")
    b1=Button(t,text="Add Task",fg = "Black", bg = "LightGreen",command=addTask,width=10)
    b2=Button(t,text="Remove Task",fg = "Black", bg = "Red",command=delOne,width=10)
    lbl1 = Label(t, text = "ToDo List:-",font="times 12",foreground="Black",background="PowderBlue",padx=3)
    lbl1.place(x=10,y=60)

    

    tsk.place(x=100, y=5)
    b1.place(x=50, y=30)
    b2.place(x=150, y=30)
    tb.place(x=20, y = 90)
    t.mainloop()
    
    