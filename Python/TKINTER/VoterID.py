from tkinter import *
from tkinter import messagebox


screen = Tk()
screen.title("Voter Eligibility Checker")
screen.geometry("400x300")
screen.config(bg="#f0f8ff")

#title
title = Label(screen,text="Check Your Voter Eligibility!",font=("Comic sans MS",16,"bold"),bg="#f0f8ff",fg="#003366")
title.pack(pady=10)

#name label
name_label= Label(screen,text="Enter Your Name",font=("Ariel",12,"bold"),bg="#f0f8ff")
name_label.pack()

#input name
name_input = Entry(screen,width=25,font=("Ariel",12,"bold"),bg="white",fg="#1e3a8a",justify="center",relief="flat")
name_input.pack(padx=2,pady=2)

#age label
age_label= Label(screen,text="Enter Your Age",font=("Ariel",12,"bold"),bg="#f0f8ff")
age_label.pack()

#input age
age_input = Entry(screen,width=25,font=("Ariel",12,"bold"),bg="white",fg="#1e3a8a",justify="center",relief="flat",)
age_input.pack(padx=2,pady=2)


def Check_Eligibility():
    name = name_input.get().strip()
    age = age_input.get().strip()

    if not name or not age:
        messagebox.showwarning("Input Missing","Please enter both name and age!")
        return
    
    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Input Age","Please enter valid age!")
        return

    if age>=18:
        result.config(text=f"Hey! {name} You are eligible to vote !",fg="green")
    else:
        result.config(text=f"Sorry! {name} You are not eligible",fg="red")




#check Button
check = Button(screen,text="Check Eligibility",bg="#047008",fg="white",font=("Ariel",10,"bold"),relief="raised",command=Check_Eligibility)
check.pack(pady=10)

#result
result = Label(screen,text="",bg="#f0f8ff",font=("Comic sans MS",14,"bold"))
result.pack(pady=20)

screen.mainloop()