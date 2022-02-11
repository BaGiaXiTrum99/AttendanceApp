from PIL import Image, ImageTk,ImageDraw
from tkinter import *
from tkinter import ttk
import PIL.Image ,PIL.ImageDraw
from datetime import *
import time
from time import strftime
from math import *
# import mysql.connector
import pyodbc
from tkinter import messagebox
from main1 import Face_Recognition_System
from main1 import new_print

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Đăng nhập")
        scrW = self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" % (scrW / 2 - 600, scrH / 2 - 345))
        self.root.config(bg="#021e2f")
        self.root.resizable(width=False, height=False)
        today = strftime("%d-%m-%Y")  # time_today

        # =============variable============
        self.var_email = StringVar()
        self.var_password = StringVar()

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        #===========Frame============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        #===========style_ttk.tentry===========
        self.estyle = ttk.Style()
        self.estyle.configure("EntryStyle.TEntry", background='black')

        title=Label(login_frame,text="Đăng nhập ",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=40)

        email = Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=130)
        self.txtuser=ttk.Entry(login_frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txtuser.place(x=250, y=160,height=35,width=350)

        pass_word = Label(login_frame, text="Mật khẩu", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=220)
        self.txtpass = ttk.Entry(login_frame, textvariable=self.var_password,font=("times new roman", 15), background="black" ,show="*")
        self.txtpass.place(x=250, y=250,height=35,width=350)

        # =============check_button=============
        self.varcheck = IntVar()
        checkbtn = Checkbutton(login_frame, variable=self.varcheck, text="Đăng nhập bằng tài khoản Admin",
                               font=("times new roman", 12), onvalue=1, offvalue=0)
        checkbtn.place(x=250, y=320)



        btn_login = Button(login_frame, text="Đăng nhập", command=self.login,font=("times new roman", 17,"bold"), fg="white", bd=0,
                            bg="#B00857",cursor="hand2").place(x=250, y=400,width=220,height=40)

        # =============date============
        self.lbl = Label(self.root, bg="#081923", text=today, font=("Book Antiqua", 20, "bold"), compound=BOTTOM,
                         fg="white", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

        #=============clock============
        c = Canvas(width=1200, height=140, background='#00ffff')
        c.pack()
        while True:
            now = datetime.now()

            s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)

            c.create_rectangle(0, 0, 1200, 140, outline='#00ffff', fill='#00ffff')

            c.create_text(600, 70, text=s, font=('', 70), fill='blue')

            c.update()

            time.sleep(0.05)


    def reset(self):
        self.var_email.set('')
        self.var_password.set('')
        self.varcheck.set(0)
    def working(self):
        h=datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi !!","Vui lòng nhập đầy đủ thông tin")
        elif(self.varcheck.get()==1) :
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where Account=? and Password=?", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
            else:
                new_print(str(0))
                self.reset()
                messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền Admin")
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Login_Window(root)
    root.mainloop()# cua so hien len