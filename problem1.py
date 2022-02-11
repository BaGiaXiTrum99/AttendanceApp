from tkinter import *
from tkinter import ttk
import PIL.Image
from PIL import Image, ImageTk
import random
from time import strftime
class Problem:
    def __init__(self,root):
        self.root=root
        scrW=self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" %(scrW/2-600,scrH/2-345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width= False, height= False)
        today = strftime("%d-%m-%Y")

        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1200, 653), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1200, height=653)

        #==================================heading====================================
        #====time====
        img_time = PIL.Image.open(r"ImageFaceDetect\timsearch50.png")
        img_time = img_time.resize((30, 30), PIL.Image.ANTIALIAS)
        self.photoimgtime = ImageTk.PhotoImage(img_time)
        time_img = Label(self.root, image=self.photoimgtime,bg="white")
        time_img.place(x=43, y=23, width=30, height=30)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("yu gothic ui", 12, "bold"),bg="white", fg="black")
        lbl.place(x=80,y=15,width=100,height=20)
        time()
        lbl1 = Label(self.root,text=today, font=("yu gothic ui", 12, "bold"), bg="white", fg="black")
        lbl1.place(x=80, y=39, width=100, height=20)

        #====title=========
        self.txt = "Báo cáo sự cố"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d"]
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 18, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=250, y=15, width=500)
        # self.slider()
        self.heading_color()


    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj = Problem(root)
    root.mainloop()# cua so hien len