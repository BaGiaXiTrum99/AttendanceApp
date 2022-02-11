import os
import random
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
from student1 import Student
from subject1 import Subject
from teacher1 import Teacher
from problem1 import Problem
from attendance1 import Attendance
from subject_class1 import SubjectClass
import pyodbc

value_from_p1 = None

def new_print(value):
    global value_from_p1
    value_from_p1 = value
    print(value_from_p1)

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        scrW=self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" %(scrW/2-600,scrH/2-345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width= False, height= False)
        today = strftime("%d-%m-%Y")

        # new_tcid(value_from_p1)
        #background
        print(value_from_p1)
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
        self.txt = "Phần mềm điểm danh sinh viên"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d"]
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 18, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=250, y=15, width=500)
        # self.slider()
        self.heading_color()

        #=========account===========
        #===get email from db=============
        self.account=""
        if(value_from_p1=="0"):
            self.account = "Admin"
        # elif(value_from_p1==None):
        #     self.account="AdminSafe"
        # else:
        #
        #     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
        #     my_cursor = conn.cursor()
        #     my_cursor.execute("select Email from teacher where Teacher_id=%s", (
        #         value_from_p1,
        #     ))
        #     row = my_cursor.fetchone()
        #     self.account = row[0]
        img_peop = PIL.Image.open(r"ImageFaceDetect\peop.png")
        img_peop = img_peop.resize((30, 30), PIL.Image.ANTIALIAS)
        self.photoimgpeop = ImageTk.PhotoImage(img_peop)
        time_img = Label(self.root, image=self.photoimgpeop, bg="white")
        time_img.place(x=780, y=23, width=30, height=30)
        # self.lblemail = Label(self.root,text=self.account, font=("yu gothic ui", 12, "bold"), bg="white", fg="green")
        # self.lblemail.place(x=1000, y=48, width=150, height=22)

        #=======Đăng-xuất==========
        img_logout = PIL.Image.open(r"ImageFaceDetect\logout.png")
        img_logout = img_logout.resize((30, 30), PIL.Image.ANTIALIAS)
        self.photoimglogout = ImageTk.PhotoImage(img_logout)
        b1 = Button(self.root, image=self.photoimglogout, cursor="hand2", command=self.exit, borderwidth=0, bg="white")
        b1.place(x=935, y=23, width=30, height=30)

        b1_1 = Button(self.root, text="Đăng xuất", cursor="hand2", command=self.exit,
                      font=("yu gothic ui", 14, "bold"),
                      bg="white", fg="black",borderwidth=0)
        b1_1.place(x=980, y=16, width=170)


        #=============Thong ke================
        img_btn1 = PIL.Image.open(r"ImageFaceDetect\report.png")
        img_btn1 = img_btn1.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)

        b2 = Button(self.root, text="Thống kê",font=("yu gothic ui", 16, "bold"),command=self.report_data,image=self.photobtn1,cursor="hand2",
                    activebackground="white",bg="white",borderwidth=5,compound="top")
        b2.place(x=170, y=400, width=170, height=170)

        #============student================
        img_btn2 = PIL.Image.open(r"ImageFaceDetect\student.png")
        img_btn2 = img_btn2.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn2 = ImageTk.PhotoImage(img_btn2)

        btn2 = Button(self.root, text="Sinh viên", font=("yu gothic ui", 16, "bold"),command=self.student_details, image=self.photobtn2,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        btn2.place(x=170, y=180, width=170, height=170)

        # # ============nhan dien============
        # img_btn3 = PIL.Image.open(r"ImageFaceDetect\nhandien.png")
        # img_btn3 = img_btn3.resize((80, 113), PIL.Image.ANTIALIAS)
        # self.photobtn3 = ImageTk.PhotoImage(img_btn3)
        #
        # b3 = Button(self.root, text="Nhận diện", font=("yu gothic ui", 16, "bold"), command=self.face_recognition,
        #             image=self.photobtn3,
        #             cursor="hand2",
        #             activebackground="white", bg="white", borderwidth=0, compound="top")
        # b3.place(x=520, y=200, width=180, height=180)

        #===========diem-danh===============
        img_btn4 = PIL.Image.open(r"ImageFaceDetect\diemdanh.png")
        img_btn4 = img_btn4.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn4 = ImageTk.PhotoImage(img_btn4)

        b4 = Button(self.root, text="Điểm danh", font=("yu gothic ui", 16, "bold"),command=self.attendance_data ,image=self.photobtn4,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b4.place(x=650, y=180, width=170, height=170)

        #==========hocphan=================
        img_btn5 = PIL.Image.open(r"ImageFaceDetect\book.png")
        img_btn5 = img_btn5.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn5 = ImageTk.PhotoImage(img_btn5)

        b5 = Button(self.root, text="Học phần", font=("yu gothic ui", 16, "bold"),command=self.subject_data, image=self.photobtn5,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b5.place(x=410, y=400, width=170, height=170)

        #==========teacher=============
        img_btn6 = PIL.Image.open(r"ImageFaceDetect\teacher.png")
        img_btn6 = img_btn6.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn6 = ImageTk.PhotoImage(img_btn6)

        b6 = Button(self.root, text="Giảng viên", font=("yu gothic ui", 16, "bold"),command=self.teacher_data, image=self.photobtn6,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b6.place(x=410, y=180, width=170, height=170)


        #==========dangdienra================
        img_btn7 = PIL.Image.open(r"ImageFaceDetect\happenning.png")
        img_btn7 = img_btn7.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn7 = ImageTk.PhotoImage(img_btn7)

        b7 = Button(self.root, text="Đang diễn ra", font=("yu gothic ui", 16, "bold"),command=self.happenning_data, image=self.photobtn7,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b7.place(x=650, y=400, width=170, height=170)

        # #==========XemAnh===============
        # img_btn8 = PIL.Image.open(r"ImageFaceDetect\picture.png")
        # img_btn8 = img_btn8.resize((80, 113), PIL.Image.ANTIALIAS)
        # self.photobtn8 = ImageTk.PhotoImage(img_btn8)
        #
        # b8 = Button(self.root, text="Xem ảnh", font=("yu gothic ui", 16, "bold"),command=self.open_img, image=self.photobtn8,
        #             cursor="hand2",
        #             activebackground="white", bg="white", borderwidth=0, compound="top")
        # b8.place(x=1175, y=490, width=180, height=180)
        # if(value_from_p1=="0" or value_from_p1==None):
        #     b4['state']="normal"
        #     b5['state'] = "normal"
        #     b6['state']="normal"
        #     b7['state']="normal"
        #     b8['state']="normal"
        # else:
        #     change_pass = Button(self.root, text="Đổi mật khẩu", cursor="hand2", command=self.change_pass,
        #                   font=("times new roman", 13, "bold"),
        #                   bg="white", fg="black", borderwidth=0)
        #     change_pass.place(x=1220, y=48, width=100, height=27)
        #     b4['state'] = "disabled"
        #     b5['state'] = "disabled"
        #     b6['state'] = "disabled"
        #     b7['state'] = "disabled"
        #     b8['state'] = "disabled"
        # ==========problem================
        img_btn9 = PIL.Image.open(r"ImageFaceDetect\problem.png")
        img_btn9 = img_btn9.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn9 = ImageTk.PhotoImage(img_btn9)

        b9 = Button(self.root, text="Báo cáo sự cố", font=("yu gothic ui", 16, "bold"), command=self.report_problem,
                    image=self.photobtn9,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b9.place(x=890, y=180, width=170, height=170)

        # ==========lophoc================
        img_btn10 = PIL.Image.open(r"ImageFaceDetect\class.png")
        img_btn10 = img_btn10.resize((100, 80), PIL.Image.ANTIALIAS)
        self.photobtn10 = ImageTk.PhotoImage(img_btn10)

        b10 = Button(self.root, text="Lớp học", font=("yu gothic ui", 16, "bold"), command=self.class_data,
                    image=self.photobtn10,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=5, compound="top")
        b10.place(x=890, y=400, width=170, height=170)
    # def slider(self):
    #     if self.count>=len(self.txt):
    #         self.count = -1
    #         self.text = ''
    #         self.heading.config(text=self.text)
    #
    #     else:
    #         self.text = self.text+self.txt[self.count]
    #         self.heading.config(text=self.text)
    #
    #     self.count+=1
    #
    #     self.heading.after(100,self.slider)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)
    def exit(self):
        Exit = messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất không?", parent=self.root)
        if(Exit>0):
            self.root.destroy()
        else:
            if not Exit:
                return
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def report_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)
    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def subject_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window)
    def teacher_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Teacher(self.new_window)
    def happenning_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Happenning(self.new_window)
    def report_problem(self):
        self.new_window=Toplevel(self.root)
        self.app=Problem(self.new_window)
    def class_data(self):
        self.new_window = Toplevel(self.root)
        self.app = SubjectClass(self.new_window)

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj = Face_Recognition_System(root)
    root.mainloop()# cua so hien len