
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  


root = Tk()
root.title("Denomination Calculator")

root.geometry("500x500")


upload = Image.open("app_img.jpg")  
upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
image_Label = Label(root, image=image, bg='light blue')
image_Label.pack(pady=20)

def msg():
    MsgBox = messagebox.showinfo(
         "Alert","do you want to calculate denomination count")
    if MsgBox == 'ok':
        topwin()
    

button1 = Button(root,
               text="Lets Get Started!", 
               command=msg,
               bg="red", 
               fg="black")
button1.place(x=260, y=360)
        
root.mainloop()