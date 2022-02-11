import os
import random
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
import pyodbc
mydata=[]
class Subject:
    def __init__(self, root):
        self.root = root
        scrW = self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" % (scrW / 2 - 600, scrH / 2 - 345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width=False, height=False)
        today = strftime("%d-%m-%Y")

        # ================variable===================
        self.var_idhocphan = StringVar()
        self.var_tenhocphan = StringVar()
        self.var_soluong = StringVar()

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
        self.txt = "Lớp học trong kì "
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d"]
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 18, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=250, y=15, width=500)
        # self.slider()
        self.heading_color()
        #tạo frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=18, y=60, width=1160, height=568)

        img4 = PIL.Image.open(r"ImageFaceDetect\hust.jpg")
        img4 = img4.resize((440, 568), PIL.Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img4_1 = Label(main_frame, image=self.photoimg4)
        img4_1.place(x=710, y=5, width=440, height=568)
        # search
        self.var_com_search = StringVar()
        search_label = Label(main_frame, text="Tìm kiếm theo :", font=("times new roman", 13, "bold"),
                             bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(main_frame, font=("times new roman", 12, "bold"), textvariable=self.var_com_search,
                                    state="read only",
                                    width=12)
        search_combo["values"] = ("Mã học phần", "Tên học phần")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(main_frame, textvariable=self.var_search, width=15,
                                 font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(main_frame, command=self.search_data, text="Tìm kiếm",
                            font=("times new roman", 12, "bold"), bg="#38a6f0", fg="white",
                            width=11)
        search_btn.grid(row=0, column=3, padx=10)

        showAll_btn = Button(main_frame, text="Xem tất cả", command=self.fetch_data,
                             font=("times new roman", 12, "bold"), bg="#38a6f0",
                             fg="white",
                             width=12)
        showAll_btn.grid(row=0, column=5, padx=10)

        # table_frame
        table_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=55, width=680, height=500)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "idhocphan", "tenhocphan", "soluong"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("idhocphan", text="Mã học phần")
        self.AttendanceReportTable.heading("tenhocphan", text="Tên học phần")
        self.AttendanceReportTable.heading("soluong", text="Số lượng sinh viên")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("idhocphan", width=100)
        self.AttendanceReportTable.column("tenhocphan", width=100)
        self.AttendanceReportTable.column("soluong", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ")

        else:
            try:
                conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                my_cursor = conn.cursor()
                if(self.var_com_search.get()=="Mã học phần"):
                    self.var_com_search.set("ID_SUBJECT")
                elif(self.var_com_search.get()=="Tên học phần"):
                    self.var_com_search.set("NAME_SUBJECT")

                my_cursor.execute("select * from subject where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)
    def fetch_data(self):
            # global mydata
            # mydata.clear()
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from subject")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_idhocphan.set(rows[0])
        self.var_tenhocphan.set(rows[1])
        self.var_soluong.set(rows[2])
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Subject(root)
    root.mainloop()# cua so hien len