#GUI prototype

import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#open file function

def open_file():
    x1 = " "

    file = askopenfile(parent=root, mode='r', title="choose a file", filetype=[("CSV File", "*.csv")])
    x1 = file.name  # This is getting the exact file address
    intCheck()
    eStr1 = e1.get()   # These are getting the inputs from Entry boxes 1-3
    eStr2 = e2.get()
    eStr3 = int(e3.get())

    if intCheck() == True:
        clean_rev(x1, eStr1, eStr2, eStr3)
        completeLabel = tk.Label(root, text=file.name + "has been processed").place(x=105, y=255)



    else:
        print("error")
        newWindow = tk.Toplevel(root)
        newWindow.geometry("350x50")
        completeLabel2 = tk.Label(newWindow, text="ERROR: Please enter numeric values ONLY", fg="red", font="bold")
        completeLabel2.grid(column=4, row=4)





    browse_text.set("Run")

def testInput(f1,a1,a2,a3): # to test openfile and entry box input
    print(type(f1))
    print(type(a1))
    print(type(a2))
    print(type(int(a3)))

def clean_rev(x, m1, m2, y):
    # This loads the CSV file into the console
    df1 = pd.read_csv(x)
    df1.columns = [
        'Posted_Dt',
        'Doc_Dt',
        'Doc',
        'Memo / Description',
        'Department',
        'Location',
        'Contract',
        'Customer Name',
        'JNL',
        'Curr',
        'Txn Amt',
        'Debit',
        'Credit',
        'Balance (USD)'
    ]
    df1 = df1.fillna(0)

    df1["Total Billed"] = df1.Credit - df1.Debit

    df1.drop(df1[df1['Memo / Description'] == 0].index, inplace=True)

    df1['Posted_Dt'] = pd.DatetimeIndex(df1['Posted_Dt']).month

    pivot1 = pd.pivot_table(df1, index=['Contract', 'Customer Name'],
                                columns='Posted_Dt',
                                values='Total Billed',
                                aggfunc='sum')

    df2 = pd.DataFrame(pivot1.to_records())

    df2 = df2.fillna(0)

    df2["Variance"] = df2[m1] - df2[m2]

    df_final = df2[(df2.Variance >= y) | (df2.Variance <= -y)]
    df_final.to_csv(r'C:\Users\gregi\Downloads\finalTest.csv')

def clicked(value):
    if value == 2:
        Funct2()

    if value == 1:
        Funct1()

def Funct1():   #shows Frame1

    frame2.place_forget()
    frame1.place(width=600, height=220)

def Funct2():   #shows Frame2

    frame1.place_forget()
    frame2.place(width=600, height=220)

def intCheck(): #checks for integer values in entry boxes, will return error
    try:
        int(e1.get())
        int(e2.get())
        int(e3.get())
        return True
    except ValueError:
        return False
##########################################################################################################
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
##########################################################################################################

root = tk.Tk()
canvas = tk.Canvas(root)
root.geometry("600x300")


frame1 = tk.Frame(root, bg="#F0F0F0", width=290, height=145)
frame2 = tk.Frame(root, bg="#F0F0F0", width=290, height=145)
#
# logos
logo = Image.open('iland.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame1, image=logo)
logo_label.image = logo
logo_label.place(x=380, y=20)

logo2 = Image.open('iland.png')
logo2 = ImageTk.PhotoImage(logo2)
logo2_label = tk.Label(frame2, image=logo2)
logo2_label.image = logo2
logo2_label.place(x=380, y=20)
# radio buttons
r = tk.IntVar()
r.set("1")

radB=tk.Radiobutton(root, text="Revenue Clean-up", variable=r, value=1, command=lambda: clicked(r.get()))
radB.place(x=80,y=220)
radB=tk.Radiobutton(root, text="Sales Register", variable=r, value=2, command=lambda: clicked(r.get()))
radB.place(x=250,y=220)

# instructions
instructions = tk.Label(frame1, text="Select a file to process", font="helvetica 12 bold", bg="#F0F0F0")
instructions.place(x=380, y=100)
instructions2 = tk.Label(frame2, text="Select a file to process", font="helvetica 12 bold", bg="#F0F0F0")
instructions2.place(x=380, y=100)
#input boxes
tk.Label(frame1, text="Value 1").place(x=80, y=50)
tk.Label(frame1, text="Value 2").place(x=80, y=100)
tk.Label(frame1, text="Value 3").place(x=80, y=150)

e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e3 = tk.Entry(frame1)
e1.place(x=180, y=50)
e2.place(x=180, y=100)
e3.place(x=180, y=150)

tk.Label(frame2, text = "Value").place(x=80, y=50)
e4 = tk.Entry(frame2)
e4.place(x=180, y=50)





browse_text = tk.StringVar()                                                         # changed font, color, and bg of button
browsebtn = tk.Button(frame1, textvariable=browse_text, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn.place(x=380, y=150)

Funct1()

root.mainloop()





