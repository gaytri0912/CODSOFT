import tkinter as tk
import random,string
def gen():
    num=int(e1.get())
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password=s[0:num]
    label3=tk.Label(root,text="Password: ",font=("Arial",12))
    label3.place(x=10,y=180)
    label3=tk.Label(root,text=password,font=("Arial",12,"bold"))
    label3.place(x=90,y=180)
def clear():

    e1.delete(0,"end")
    text1.delete(0,"end")
root=tk.Tk()
root.geometry("400x210")
root.title("Password Generator")
root.resizable(False,False)
label1=tk.Label(root,text="Password Generator ",font=("Arial",12),foreground="purple")
label1.place(x=100,y=10)
label1=tk.Label(root,text="Username: ",font=("Arial",12))
label1.place(x=10,y=50)
text1=tk.Text(root,height=1, width=25, font=("Arial",12 ))
text1.place(x=150,y=50)
label2=tk.Label(root,text="Password Length: ",font=("Arial",12))
label2.place(x=10,y=90)
e1=tk.Entry(root, width=25, font=("Arial",12 ))
e1.place(x=150,y=90)
b1=tk.Button(root,text="Generate",background="lightgreen",width=30,command=gen)
b1.place(x=90,y=140)
root.mainloop()
