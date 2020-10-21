# Imports
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import filedialog
import img2pdf
import webbrowser


def folderopening():
    global images
    try:
        Tk().withdraw()
        listPages = filedialog.askopenfilenames(title="Select files",
                                                filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        images = []
        for i in listPages:
            print(i)
            images.append(i)

        mesg = messagebox.askokcancel("Succeed", "Images Selected Succesfully", parent=root)
        if(mesg==True):
            return "None"
        else:
            return "None"
    except:
        errormsg = messagebox.askretrycancel("A Problem Has Been Occured", "Please Select Images Only")
        if(errormsg==True):
            return "None"
        else:
            root.destroy()


def convert():
    try:
        global pdfFilename
        pdfFilename = filedialog.asksaveasfilename(parent=root, initialdir=os.getcwd(), title="Save as",
                                                   filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")),
                                                   defaultextension=".pdf")
        pdfFilename = str(pdfFilename)
        with open(pdfFilename,"wb") as f:
            f.write(img2pdf.convert(images))

        success = messagebox.askokcancel("Succeed", "Hurray, PDF Converted Successfully Stored in " + pdfFilename)
    except:
        error = messagebox.askretrycancel("A Problem Has Been Occured", "Please Insert Images Only")

def on_enter(e):
        btnconvert['background'] = "black"
        btnconvert['foreground'] = "white"

def on_leave(e):
        btnconvert['background'] = 'lime'
        btnconvert['foreground'] = 'black'

    # Main Configs
root = Tk()
root.geometry("600x550")
root.config(bg="cyan")
root.iconbitmap("img.ico")
root.title("Kunal Images to PDF Convertor")

img = ImageTk.PhotoImage(Image.open("pdf.png"))
image = Label(root, image = img, bg="cyan")
image.pack(anchor="center", pady="20px")

Title = Label(root, text="Kunal Images to PDF Convertor", font=("ubuntu", 24, "bold"), bg="cyan", fg="black")
Title.pack(anchor="center")


Label1 = Label(root, text="Select Images to Convert :-", font=("ubuntu", 15, "bold"), bg="cyan", fg="black")
Label1.place(x=50, y=280)
Btn1 = Button(root, text="Select Images", font=("ubuntu", 15, "bold"),command=folderopening, bg="black", fg="white", relief=RAISED, cursor="hand2")
Btn1.place(x=400, y=275)


btnconvert = Button(root, text="Convert to PDF", bg="lime", fg="black", font=("ubuntu", 15, "bold"), command=convert, relief=RAISED, cursor="hand2")
btnconvert.bind("<Enter>", on_enter)
btnconvert.bind("<Leave>", on_leave)
btnconvert.place(x=220, y=350)

Follow = Label(root, text="Follow Us On", font=("ubuntu", 15, "bold"), bg="cyan", fg="purple")
Follow.place(x=240, y=420)

def subscribe():
    webbrowser.open("https://www.youtube.com/channel/UCIXud9Ot8pfDQizzdmQ-FyQ?sub_confirmation=1")

yt_icon = ImageTk.PhotoImage(Image.open("yt_icon.png"))
yt_icon1 = Button(root, text = 'Youtube', image = yt_icon, bg="cyan", relief=FLAT, cursor="hand2", command=subscribe)
yt_icon1.place(x=190, y=460)

def visit():
    webbrowser.open("https://macstockofficial.blogspot.com/")

web_icon = ImageTk.PhotoImage(Image.open("macstock.png"))
web_icon1 = Button(root, text = 'Website', image = web_icon, bg="cyan", relief=FLAT, cursor="hand2", command=visit)
web_icon1.place(x=350, y=460)
root.mainloop()