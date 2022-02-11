from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import datetime
from time import strftime
import PIL.Image
import pyodbc
import csv
import random
from tkinter import filedialog
from datetime import date
from csv import writer
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        scrW = self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" % (scrW / 2 - 600, scrH / 2 - 345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width=False, height=False)
        today = strftime("%d-%m-%Y")

        # ================variable===================
        self.var_id_attendence = StringVar()
        self.var_date = StringVar()
        self.var_id_class = StringVar()
        self.var_id_addclass = StringVar()
        self.var_tiethoc = StringVar()
        self.var_ngaytrongtuan = StringVar()
        self.var_id_student = StringVar()
        self.var_time_in = StringVar()
        self.var_status = StringVar()
        # background
        # print(value_from_p1)
        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1200, 653), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1200, height=653)

        ##==================================heading====================================
        # ====time====
        img_time = PIL.Image.open(r"ImageFaceDetect\timsearch50.png")
        img_time = img_time.resize((30, 30), PIL.Image.ANTIALIAS)
        self.photoimgtime = ImageTk.PhotoImage(img_time)
        time_img = Label(self.root, image=self.photoimgtime, bg="white")
        time_img.place(x=43, y=23, width=30, height=30)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(self.root, font=("yu gothic ui", 12, "bold"), bg="white", fg="black")
        lbl.place(x=80, y=15, width=100, height=20)
        time()
        lbl1 = Label(self.root, text=today, font=("yu gothic ui", 12, "bold"), bg="white", fg="black")
        lbl1.place(x=80, y=39, width=100, height=20)

        # ====title=========
        self.txt = "Quản lý thông tin điểm danh"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d"]
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 18, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=250, y=15, width=500)
        # self.slider()
        self.heading_color()

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=18, y=60, width=1160, height=568)

        # =====================left_label======================
        self.getNextid()
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=18, y=5, width=344, height=568)

        label_Update_att = Label(Left_frame, bg="#F0FFF0", fg="#483D8B", text="Thông tin điểm danh",
                                 font=("times new roman", 17, "bold"))
        label_Update_att.place(x=0, y=1, width=340, height=45)
        #======================left-up-label====================
        left_inside_frame = Frame(Left_frame, bd=1, bg="white")
        left_inside_frame.place(x=0, y=60, width=340, height=568)

        #attenID
        idattendance = Label(left_inside_frame, text="ID điểm danh:", font=("times new roman", 12, "bold"),
                     bg="white")
        idattendance.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        idattendance_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id_attendence,
                               font=("times new roman", 12, "bold"), width=22, state="readonly")
        idattendance_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #date
        date_label = Label(left_inside_frame, text="Ngày:", font=("times new roman", 12, "bold"),
                             bg="white")
        date_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.date_entry = ttk.Entry(left_inside_frame, text=self.var_date,state="readonly",
                                       font=("times new roman", 12, "bold"), width=22)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # ClassID
        class_label = Label(left_inside_frame, text="ID Lớp", font=("times new roman", 12, "bold"),
                              bg="white")
        class_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        class_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id_class,state="readonly",
                                  font=("times new roman", 12, "bold"), width=22)
        class_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # AddClassID
        addclass_label = Label(left_inside_frame, text="Địa chỉ", font=("times new roman", 12, "bold"),
                            bg="white")
        addclass_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        addclass_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id_addclass, state="readonly",
                                font=("times new roman", 12, "bold"), width=22)
        addclass_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # idsv
        idsv = Label(left_inside_frame, text="ID Sinh viên:", font=("times new roman", 12, "bold"),
                     bg="white")
        idsv.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.idsv_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id_student,
                               font=("times new roman", 12, "bold"), width=22)
        self.idsv_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        # time_in
        time_in = Label(left_inside_frame, text="Giờ vào:", font=("times new roman", 12, "bold"),
                     bg="white")
        time_in.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        self.time_in_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time_in,
                               font=("times new roman", 12, "bold"), width=22)
        self.time_in_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # trangthai
        stt = Label(left_inside_frame, text="Trạng thái:", font=("times new roman", 12, "bold"),
                        bg="white")
        stt.grid(row=6, column=0, padx=10, pady=10, sticky=W)

        self.stt_entry = ttk.Entry(left_inside_frame, textvariable=self.var_status,
                                  font=("times new roman", 12, "bold"), width=22)
        self.stt_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)
        # ==================left-down-label========================
        btn_frame = Frame(left_inside_frame, bg="white")
        btn_frame.place(x=0, y=400, width=350, height=115)

        open_cam = Button(btn_frame, text="Mở camera", command=self.open_camera, font=("times new roman", 13, "bold"),
                         bg="#38a6f0", fg="white", width=14)
        open_cam.grid(row=0, column=0, pady=10, padx=10)

        resetdata = Button(btn_frame, text="Làm mới", command=self.reset_data,
                            font=("times new roman", 13, "bold"),
                            bg="#38a6f0", fg="white", width=14)
        resetdata.grid(row=0, column=1, pady=10, padx=10)

        save_csv = Button(btn_frame,text="Lưu file CSV",command=self.savecsv, font=("times new roman",13,"bold"),
                          bg="#38a6f0", fg="white",width=14)
        save_csv.grid(row=1,column=0, pady=10, padx=10)
        # ==================right-label========================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=370, y=5, width=770, height=568)

        self.var_com_search = StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 13, "bold"),
                             bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 12, "bold"), textvariable=self.var_com_search,
                                    state="readonly",
                                    width=12)
        search_combo["values"] = ("Mã lớp", "Địa chỉ")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(Right_frame, textvariable=self.var_search, width=15,
                                 font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Right_frame, command=self.search_data, text="Tìm kiếm",
                            font=("times new roman", 12, "bold"), bg="#38a6f0", fg="white",
                            width=11)
        search_btn.grid(row=0, column=3, padx=10)

        showAll_btn = Button(Right_frame, text="Xem tất cả", command=self.fetch_data,
                             font=("times new roman", 12, "bold"), bg="#38a6f0",
                             fg="white",
                             width=12)
        showAll_btn.grid(row=0, column=5, padx=10)

        # table_frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=55, width=750, height=500)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceTable = ttk.Treeview(table_frame, column=(
            "idclass", "addclass", "tiethoc", "thu"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceTable.xview)
        scroll_y.config(command=self.AttendanceTable.yview)

        self.AttendanceTable.heading("idclass", text="Mã lớp")
        self.AttendanceTable.heading("addclass", text="Địa chỉ")
        self.AttendanceTable.heading("tiethoc", text="Tiết học")
        self.AttendanceTable.heading("thu", text="Thứ")

        self.AttendanceTable["show"] = "headings"
        self.AttendanceTable.column("idclass", width=100)
        self.AttendanceTable.column("addclass", width=100)
        self.AttendanceTable.column("tiethoc", width=100)
        self.AttendanceTable.column("thu", width=100)

        self.AttendanceTable.pack(fill=BOTH, expand=1)

        self.AttendanceTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid
        # ================fetchData======================


    def open_camera(self):
        import face_rec_cam
        face_rec_cam.main_recognition()
        bestname=face_rec_cam.Id_bestface

        self.var_id_student.set(bestname)
        self.idsv_entry.config(textvariable=self.var_id_student)
        self.idsv_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        now = datetime.datetime.now()
        self.var_time_in.set(now.strftime("%H:%M:%S"))
        self.time_in_entry.config(textvariable=self.var_time_in)
        self.time_in_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        self.var_status.set("Success")
        self.stt_entry.config(textvariable=self.var_status)
        self.stt_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        today = date.today()
        self.var_date.set(today.strftime("%d:%m:%Y"))
        self.date_entry.config(textvariable=self.var_date)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def fetch_data(self):
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from class_addclass_timecase")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.AttendanceTable.delete(*self.AttendanceTable.get_children())
                for i in data:
                    self.AttendanceTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
            conn.close()

    def getNextid(self):
        file = pd.read_csv("D:\HOCTAP\Final2\diemdanh.csv")
        lastid = file.ID_ATTENDANCE
        nextid=0
        for i in range(len(lastid)):
            if nextid < lastid[i]:
                nextid=lastid[i]
        nextid+=1
        self.var_id_attendence.set(nextid)
        return self.var_id_attendence
    def savecsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Không có dữ liệu", "Không có dữ liệu để xuất file", parent=self.root)
                return False
            else:
                with open('D:\HOCTAP\Final2\diemdanh.csv','a',newline='') as myfile:
                    row=[self.var_id_attendence.get(),
                         self.var_date.get(),
                         self.var_id_class.get(),
                         self.var_id_addclass.get(),
                         self.var_id_student.get(),
                         self.var_time_in.get(),
                         self.var_status.get()]
                    writer_object = writer(myfile,delimiter=",")
                    writer_object.writerow(row)
                    myfile.close()
                messagebox.showinfo("Thông báo","Lưu dữ liệu thành công")
        except Exception as es:
            messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceTable.focus()
        content=self.AttendanceTable.item(cursor_row)
        data=content['values']
        a=data[0]
        b=data[1]
        self.var_id_class.set(a[1:len(a)-2]),
        self.var_id_addclass.set(b[1:len(b)-2])

    def reset_data(self):
        self.getNextid()
        self.var_date.set("")
        self.var_id_class.set("")
        self.var_id_addclass.set("")
        self.var_id_student.set("")
        self.var_time_in.set("")
        self.var_status.set("")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Lỗi !", "Vui lòng nhập thông tin đầy đủ")

        else:
            try:
                conn = pyodbc.connect(
                    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                my_cursor = conn.cursor()
                if (self.var_com_search.get() == "Mã lớp"):
                    self.var_com_search.set("ID_CLASS")
                elif (self.var_com_search.get() == "Địa chỉ"):
                    self.var_com_search.set("ID_ADDCLASS")

                my_cursor.execute("select * from class_addclass_timecase where " + str(self.var_com_search.get()) + " Like '%" + str(
                    self.var_search.get()) + "%'")
                data = my_cursor.fetchall()
                if (len(data) != 0):
                    self.AttendanceTable.delete(*self.AttendanceTable.get_children())
                    for i in data:
                        self.AttendanceTable.insert("", END, values=i)
                    messagebox.showinfo("Thông báo", "Có " + str(len(data)) + " bản ghi thỏa mãn điều kiện",
                                        parent=self.root)
                    conn.commit()
                else:
                    self.AttendanceTable.delete(*self.AttendanceTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Attendance(root)
    root.mainloop()# cua so hien len