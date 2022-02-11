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
class Teacher:
    def __init__(self,root):
        self.root=root
        scrW=self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" %(scrW/2-600,scrH/2-345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width=False, height=False)
        today = strftime("%d-%m-%Y")

        # ================variable===================
        self.var_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_dbirth = StringVar()
        self.var_address = StringVar()
        self.var_specialized = StringVar()

        # background
        # print(value_from_p1)
        img3 = PIL.Image.open(r"ImageFaceDetect\bg1.png")
        img3 = img3.resize((1200, 653), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1200, height=653)

        ##==================================heading====================================
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
        self.txt = "Quản lý thông tin giảng viên"
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

        # ===================left_label=====================
        self.getNextid()
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=18, y=5, width=344, height=568)

        label_Update_att = Label(Left_frame, bg="#F0FFF0", fg="#483D8B", text="Thông tin giảng viên",
                                 font=("times new roman", 17, "bold"))
        label_Update_att.place(x=0, y=1, width=340, height=45)

        left_inside_frame = Frame(Left_frame, bd=1, bg="white")
        left_inside_frame.place(x=0, y=60, width=340, height=568)

        # idgv
        idgv = Label(left_inside_frame, text="ID Giảng viên:",font=("times new roman", 12, "bold"),
                                    bg="white")
        idgv.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        idgv_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id,state="disabled",
                                        font=("times new roman", 12, "bold"),width=22)
        idgv_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # fname
        fnameLabel = Label(left_inside_frame, text="Họ và tên đệm:", font=("times new roman", 12, "bold"),
                           bg="white")
        fnameLabel.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        fnameLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_fname,
                               font=("times new roman", 12, "bold"))
        fnameLabel_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # lname
        lnameLabel = Label(left_inside_frame, text="Tên:", font=("times new roman", 12, "bold"),
                          bg="white")
        lnameLabel.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        lnameLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_lname,
                                    font=("times new roman", 12, "bold"))
        lnameLabel_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # dbirth
        dbirthLabel = Label(left_inside_frame, text="Ngày sinh:", font=("times new roman", 12, "bold"),
                          bg="white")
        dbirthLabel.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        dbirthLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_dbirth,
                                    font=("times new roman", 12, "bold"))
        dbirthLabel_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # address
        addressLabel = Label(left_inside_frame, text="Địa chỉ:", font=("times new roman", 12, "bold"),
                          bg="white")
        addressLabel.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        addressLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_address,
                                    font=("times new roman", 12, "bold"))
        addressLabel_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # specialized
        specializedLabel = Label(left_inside_frame, text="Chuyên môn:", font=("times new roman", 12, "bold"),
                             bg="white")
        specializedLabel.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        specializedLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_specialized,
                                       font=("times new roman", 12, "bold"))
        specializedLabel_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # =====btn_frame============

        btn_frame = Frame(left_inside_frame, bg="white")
        btn_frame.place(x=0, y=350, width=350, height=115)

        add_btn = Button(btn_frame, text="Thêm mới", command=self.add_data, font=("times new roman", 13, "bold"),
                            bg="#38a6f0", fg="white", width=14)
        add_btn.grid(row=9, column=0, pady=10,padx=10)

        delete_btn = Button(btn_frame, text="Xóa", command=self.delete_data,
                            font=("times new roman", 13, "bold"),
                            bg="#38a6f0", fg="white", width=14)
        delete_btn.grid(row=9, column=1, pady=10,padx=10)

        update_btn = Button(btn_frame, text="Cập nhật", command=self.update_data, font=("times new roman", 13, "bold"),
                            bg="#38a6f0", fg="white", width=14)
        update_btn.grid(row=10, column=0, pady=20, padx=10)

        reset_btn = Button(btn_frame, text="Làm mới", command=self.reset_data, font=("times new roman", 13, "bold"),
                           bg="#38a6f0", fg="white", width=14)
        reset_btn.grid(row=10, column=1, pady=0,padx=10)

        # ==================right_ label========================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=370, y=5, width=770, height=568)

        # search
        self.var_com_search = StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 13, "bold"),
                             bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 12, "bold"), textvariable=self.var_com_search,
                                    state="read only",
                                    width=12)
        search_combo["values"] = ("ID Giảng viên", "Tên Giảng viên ")
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

        self.TeacherTable = ttk.Treeview(table_frame, column=(
        "id", "fname", "lname", "dbirth", "address", "specialized"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.TeacherTable.xview)
        scroll_y.config(command=self.TeacherTable.yview)

        self.TeacherTable.heading("id", text="ID Giảng viên")
        self.TeacherTable.heading("fname", text="Họ và tên đệm")
        self.TeacherTable.heading("lname", text="Tên")
        self.TeacherTable.heading("dbirth", text="Ngày sinh")
        self.TeacherTable.heading("address", text="Địa chỉ")
        self.TeacherTable.heading("specialized", text="Chuyên môn")


        self.TeacherTable["show"] = "headings"
        self.TeacherTable.column("id", width=100)
        self.TeacherTable.column("fname", width=100)
        self.TeacherTable.column("lname", width=100)
        self.TeacherTable.column("dbirth", width=100)
        self.TeacherTable.column("address", width=200)
        self.TeacherTable.column("specialized", width=200)


        self.TeacherTable.pack(fill=BOTH, expand=1)

        self.TeacherTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid
        # ================fetchData======================


    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def getNextid(self):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT MAX(ID_TEACHER) AS max_id FROM teacher")
        lastid=my_cursor.fetchone()
        if (lastid == None):
            self.var_id.set("1")
        else:
            self.var_id.set(lastid[0]+1)
        conn.commit()
        conn.close()
        return  self.var_id

    def get_cursor(self,event=""):
        cursor_row=self.TeacherTable.focus()
        content=self.TeacherTable.item(cursor_row)
        data=content['values']
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        e = data[4]
        f = data[5]
        self.var_id.set(a[1:len(a)-1]),
        self.var_fname.set(b[1:len(b) - 2]),
        self.var_lname.set(c[1:len(c) - 2]),
        self.var_dbirth.set(d[1:len(d) - 2]),
        self.var_address.set(e[1:len(e) - 2]),
        self.var_specialized.set(f[1:len(f) - 2])

    def add_data(self):
        if self.var_id.get()=="" or self.var_lname.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into teacher values(?,?,?,?,?,?)",(
                    self.var_id.get(),
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_dbirth.get(),
                    self.var_address.get(),
                    self.var_specialized.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin giảng viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_dbirth.set("")
        self.var_address.set("")
        self.var_specialized.set("")
        self.getNextid()
    def fetch_data(self):
        global mydata
        # mydata.clear()
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from teacher")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.TeacherTable.delete(*self.TeacherTable.get_children())
            for i in data:
                self.TeacherTable.insert("", END, values=i)
                mydata.append(i)
            conn.commit()
        conn.close()
    def update_data(self):
        if  self.var_id.get()=="" or self.var_lname.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn = pyodbc.connect(
                        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE teacher SET F_NAME=?,L_NAME=?,D_BIRTH=?,Address=?,Specialized=? WHERE ID_TEACHER=?",(
                                            self.var_fname.get(),
                                            self.var_lname.get(),
                                            self.var_dbirth.get(),
                                            self.var_address.get(),
                                            self.var_specialized.get(),
                                            self.var_id.get()
                                        ))
                    messagebox.showinfo("Thành công", "Cập nhật thông tin điểm danh thành công", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Lỗi",f"Due To:{str(es)}",parent=self.root)

    # Delete Function
    def delete_data(self):
            if self.var_id == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                        my_cursor = conn.cursor()
                        sql = "DELETE FROM teacher WHERE ID_TEACHER=?"
                        val = (self.var_id.get(),)
                        my_cursor.execute(sql, val)
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()
                        messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    else:
                        if not delete:
                            return
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ")

        else:
            try:
                conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                my_cursor = conn.cursor()
                if(self.var_com_search.get()=="ID Giảng viên"):
                    self.var_com_search.set("ID_TEACHER")
                elif(self.var_com_search.get()=="Tên Giảng viên"):
                    self.var_com_search.set("L_NAME")

                my_cursor.execute("select * from teacher where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                    self.TeacherTable.delete(*self.TeacherTable.get_children())
                    for i in data:
                        self.TeacherTable.insert("",END,values=i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.TeacherTable.delete(*self.TeacherTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Teacher(root)
    root.mainloop()# cua so hien len