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
class SubjectClass:
    def __init__(self,root):
        self.root=root
        scrW = self.root.winfo_screenwidth()
        scrH = self.root.winfo_screenheight()
        self.root.geometry("1200x653+%d+%d" % (scrW / 2 - 600, scrH / 2 - 345))
        self.root.title("Phần mềm điểm danh sinh viên")
        self.root.resizable(width=False, height=False)
        today = strftime("%d-%m-%Y")

        # ================variable===================
        self.var_id_sub = StringVar()
        self.var_id_class = StringVar()
        self.var_year = StringVar()
        self.var_term = StringVar()

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
        self.txt = "Các buổi học đang diễn ra"
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

        label_Update_att = Label(Left_frame, bg="#F0FFF0", fg="#483D8B", text="Thông tin buổi học",
                                 font=("times new roman", 17, "bold"))
        label_Update_att.place(x=0, y=1, width=340, height=45)

        left_inside_frame = Frame(Left_frame, bd=1, bg="white")
        left_inside_frame.place(x=0, y=60, width=340, height=568)

        # idsub
        idsub = Label(left_inside_frame, text="Mã học phần:",font=("times new roman", 12, "bold"),
                                    bg="white")
        idsub.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        idsub_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id_sub,
                                        font=("times new roman", 12, "bold"),width=22)
        idsub_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # id_class
        id_class = Label(left_inside_frame, text="Mã lớp học:", font=("times new roman", 12, "bold"),
                         bg="white")
        id_class.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        id_class_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_id_class,
                                   font=("times new roman", 12, "bold"))
        id_class_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # year
        year = Label(left_inside_frame, text="Năm học:", font=("times new roman", 12, "bold"),
                          bg="white")
        year.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        year_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_year,
                                    font=("times new roman", 12, "bold"))
        year_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # dbirth
        term_lbl = Label(left_inside_frame, text="Kì học:", font=("times new roman", 12, "bold"),
                          bg="white")
        term_lbl.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        term_lbl_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_term,
                                    font=("times new roman", 12, "bold"))
        term_lbl_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

       
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
        search_combo["values"] = ("Mã học phần", "Mã lớp học")
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

        self.Subject_Class_Table = ttk.Treeview(table_frame, column=(
        "id_sub", "id_class", "year", "term"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Subject_Class_Table.xview)
        scroll_y.config(command=self.Subject_Class_Table.yview)

        self.Subject_Class_Table.heading("id_sub", text="Mã học phần")
        self.Subject_Class_Table.heading("id_class", text="Mã lớp học")
        self.Subject_Class_Table.heading("year", text="Năm học")
        self.Subject_Class_Table.heading("term", text="Kì học")


        self.Subject_Class_Table["show"] = "headings"
        self.Subject_Class_Table.column("id_sub", width=100)
        self.Subject_Class_Table.column("id_class", width=100)
        self.Subject_Class_Table.column("year", width=100)
        self.Subject_Class_Table.column("term", width=100)


        self.Subject_Class_Table.pack(fill=BOTH, expand=1)

        self.Subject_Class_Table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid
  

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def getNextid(self):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT MAX(ID_CLASS) AS max_id FROM subject_class")
        lastid=my_cursor.fetchone()
        if (lastid == None):
            self.var_id_class.set("1")
        else:
            self.var_id_class.set(lastid[0])
        conn.commit()
        conn.close()
        return self.var_id_class

    def get_cursor(self,event=""):
        cursor_row=self.Subject_Class_Table.focus()
        content=self.Subject_Class_Table.item(cursor_row)
        rows=content['values']
        a = rows[0]
        b = rows[1]
        c = rows[2]
        d = rows[3]
        self.var_id_sub.set(a[2:len(a)-2]),
        self.var_id_class.set(b[:len(b)-1]),
        self.var_year.set(c[1:len(c)-2]),
        self.var_term.set(d[1:len(d)-2])
    #
    def add_data(self):
        if self.var_id_class.get()=="Select" or self.var_id_sub.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into teacher values(?,?,?,?)",(
                    self.var_id_class.get(),
                    self.var_id_sub.get(),
                    self.var_year.get(),
                    self.var_term.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin giảng viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_id_class.set("")
        self.var_id_sub.set("")
        self.var_year.set("")
        self.var_term.set("")
        self.getNextid()

    def fetch_data(self):
            # global mydata
            # mydata.clear()
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from subject_class")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.Subject_Class_Table.delete(*self.Subject_Class_Table.get_children())
                for i in data:
                    self.Subject_Class_Table.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
            conn.close()

    def update_data(self):
        if  self.var_id_class.get()=="" or self.var_id_sub.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn = pyodbc.connect(
                        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update subject_class set ID_SUBJECT=?,Year_class=?,Term_class=? where ID_CLASS=?",(
                                            self.var_id_sub.get(),
                                            self.var_year.get(),
                                            self.var_term.get(),
                                            self.var_id_class.get()
                                        ))
                    messagebox.showinfo("Thành công", "Cập nhật thông tin lớp học thành công", parent=self.root)
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
        if self.var_id_class == "":
            messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                if delete > 0:
                    conn = pyodbc.connect(
                        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\HOCTAP\Final2\database.accdb;')
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM subject_class WHERE ID_CLASS=?"
                    val = (self.var_id_class.get(),)
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
                if(self.var_com_search.get()=="Mã lớp học"):
                    self.var_com_search.set("ID_CLASS")
                elif(self.var_com_search.get()=="Mã học phần"):
                    self.var_com_search.set("ID_SUBJECT")

                my_cursor.execute("select * from subject_class where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                    self.Subject_Class_Table.delete(*self.Subject_Class_Table.get_children())
                    for i in data:
                        self.Subject_Class_Table.insert("",END,values=i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.Subject_Class_Table.delete(*self.Subject_Class_Table.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=SubjectClass(root)
    root.mainloop()# cua so hien len