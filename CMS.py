from tkinter import *
from tkinter import ttk
import rows
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x720+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        root.resizable(False, False)
        #===============Variable===================
        self.case_id=StringVar()
        self.criminal_no=StringVar()
        self.criminal_name=StringVar()
        self.nick_name=StringVar()
        self.father_name=StringVar()
        self.cnic_no=StringVar()
        self.age=StringVar()
        self.birth_mark=StringVar()
        self.address=StringVar()
        self.occupation=StringVar()
        self.arrest_date=StringVar()
        self.crime_type=StringVar()
        self.date_of_crime=StringVar()
        self.gender=StringVar()
        self.most_wanted=StringVar()
        #===========Color==============
        bg_color = "#36454F"
        frame_color="lightgray"
        font_bg_color="#36454F"
        font_color='white'
        frame_hading="gold"

        #==============Icon============
        image_icon = PhotoImage(file="icon.png")
        root.iconphoto(False, image_icon)
        #===============Title===============
        title = Label(self.root, text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE", bd=10, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        #==============lOGO================
        img_logo=Image.open('logo.png')
        img_logo=img_logo.resize((45,45),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo,bg=bg_color,)
        self.logo.place(x=50,y=12,width=45,height=45)
        #===============Image Frame==============
        img_frame = Label(self.root, relief=RIDGE, bg="white", )
        img_frame.place(x=0, y=70, width=1350, height=140)

        #============Image 01================
        img1 = Image.open('police2.jpg')
        img1 = img1.resize((450, 140), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img_1 = Label(img_frame, image=self.photo1, )
        self.img_1.place(x=0, y=0, width=450, height=140)
        # ============Image 02================
        img2 = Image.open('police3.png')
        img2 = img2.resize((450, 140), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img_2 = Label(img_frame, image=self.photo2, )
        self.img_2.place(x=450, y=0, width=450, height=140)
        # ============Image 03================
        img3 = Image.open('police3.jpg')
        img3 = img3.resize((450, 140), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img_3 = Label(img_frame, image=self.photo3, )
        self.img_3.place(x=900, y=0, width=450, height=140)

        #============== Criminal Data Frame=================
        main_frame = Label(self.root, relief=RIDGE, bg="white",)
        main_frame.place(x=10, y=210, width=1330, height=500)
        # ============== Criminal Data Insert Frame=================
        insert_data_frame = LabelFrame(main_frame, relief=GROOVE, text="Criminal Information",fg=frame_hading,bg=bg_color,font=("times new roman",11,"bold"),bd=5)
        insert_data_frame.place(x=10, y=10, width=1305, height=240)

        #========Case ID===============
        case_id = Label(insert_data_frame, text="Case ID :",bg=font_bg_color,font=("arial", 10, "bold"), fg=font_color).grid(row=0, column=0, padx=2, sticky=W)
        case_id_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.case_id ,font=("arial", 10),).grid(row=0,column=1, padx=5,sticky=W)

        #========Criminal No===============
        criminal_no = Label(insert_data_frame, text="Criminal No :",fg=font_color,bg=font_bg_color,font=("arial", 10, "bold"), ).grid(row=0, column=2, padx=2, sticky=W,pady=7)
        criminal_no_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.criminal_no, font=("arial", 10),).grid(row=0,column=3, padx=5,sticky=W,pady=7)

        #========Criminal Name===============
        criminal_name = Label(insert_data_frame, text="Criminal Name :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=1, column=0, padx=2, sticky=W,pady=7)
        criminal_name_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.criminal_name, font=("arial", 10),).grid(row=1,column=1, padx=5,sticky=W,pady=7)

        #========Criminal Nick Name===============
        c_nickname = Label(insert_data_frame, text="Nick Name :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=1, column=2, padx=2, sticky=W,pady=7)
        c_nickname_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.nick_name, font=("arial", 10),).grid(row=1,column=3, padx=5,sticky=W,pady=7)

        #========Criminal Father Name===============
        c_father_name = Label(insert_data_frame, text="Father Name :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=2, column=0, padx=2, sticky=W,pady=7)
        c_father_name_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.father_name, font=("arial", 10),).grid(row=2,column=1, padx=5,sticky=W,pady=7)

        #========CNIC No===============
        cnic_no = Label(insert_data_frame, text="CNIC No :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=2, column=2, padx=2, sticky=W,pady=7)
        cnic_no_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.cnic_no, font=("arial", 10),).grid(row=2,column=3, padx=5,sticky=W,pady=7)

        #========Birth Mark ===============
        B_mark = Label(insert_data_frame, text="Birth Mark :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=3, column=2, padx=2, sticky=W,pady=7)
        B_mark_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.birth_mark, font=("arial", 10),).grid(row=3,column=3, padx=5,sticky=W,pady=7)

        #========Criminal Age ===============
        c_age = Label(insert_data_frame, text="Age :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=3, column=0, padx=2, sticky=W,pady=7)
        c_age_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.age, font=("arial", 10),).grid(row=3,column=1, padx=5,sticky=W,pady=7)

        #========Occupation ===============
        occupution = Label(insert_data_frame, text="Occupation :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=4, column=2, padx=2, sticky=W,pady=7)
        occupution_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.occupation, font=("arial", 10),).grid(row=4,column=3, padx=5,sticky=W,pady=7)

        #========Address ===============
        address = Label(insert_data_frame, text="Address :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=4, column=0, padx=2, sticky=W,pady=7)
        address_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.address, font=("arial", 10),).grid(row=4,column=1,columnspan=1, padx=5,sticky=W,pady=7)

        #========Arrest Date ===============
        arrest_date = Label(insert_data_frame, text="Arrest Date :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=0, column=6, padx=2, sticky=W,pady=7)
        arrest_date_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.arrest_date, font=("arial", 10),).grid(row=0,column=7, padx=5,sticky=W,pady=7)

        #========Crime Type ===============
        crime_type = Label(insert_data_frame, text="Crime Type :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=1, column=6, padx=2, sticky=W,pady=7)
        crime_type_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.crime_type, font=("arial", 10),).grid(row=1,column=7, padx=5,sticky=W,pady=7)

        #========Date Of Crime ===============
        crime_date = Label(insert_data_frame, text="Date Of Crime :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=2, column=6, padx=2, sticky=W,pady=7)
        crime_date_entry = ttk.Entry(insert_data_frame, width=20,textvariable=self.date_of_crime, font=("arial", 10),).grid(row=2,column=7, padx=5,sticky=W,pady=7)

        #========Gender ===============
        crime_date = Label(insert_data_frame, text="Gender :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=3, column=6, padx=2, sticky=W,pady=7)

        radio_frame_gender=Frame(insert_data_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_gender.place(x=630,y=110,width=150,height=30)
        male=Radiobutton(radio_frame_gender,text="Male",variable=self.gender,value='Male',font=("arial", 9, "bold"),).grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.gender.set('Male')
        female=Radiobutton(radio_frame_gender,text="Female",variable=self.gender,value='Female',font=("arial", 9, "bold"),).grid(row=0,column=1,pady=2,padx=5,sticky=W)
        # self.gender.set('female')

        #========Most Wanted ===============
        crime_date = Label(insert_data_frame, text="Most Wanted :",bg=font_bg_color,fg=font_color,font=("arial", 10, "bold"), ).grid(row=4, column=6, padx=2, sticky=W,pady=7)

        radio_frame_wanted=Frame(insert_data_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_wanted.place(x=630,y=150,width=150,height=30)
        yes=Radiobutton(radio_frame_wanted,text="Yes",variable=self.most_wanted,value='Yes',font=("arial", 9, "bold"),).grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.most_wanted.set('Yes')
        no=Radiobutton(radio_frame_wanted,text="No",variable=self.most_wanted,value='No',font=("arial", 9, "bold"),).grid(row=0,column=1,pady=2,padx=20,sticky=W)
        # self.most_wanted.set('no')

        #=================Button Farame===============
        button_frame=Frame(insert_data_frame,bd=2,relief=GROOVE,bg=bg_color)
        button_frame.place(x=10,y=180,width=500,height=37)
        #================== Save Button==================
        save_btn=Button(button_frame,text="Record Save",command=self.add_data,font=("arial", 9, "bold"),width=14,bg="blue",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=0,padx=5,pady=1)
        #================== Update Button==================
        update_btn=Button(button_frame,text="Update",font=("arial", 9, "bold"),width=14,bg="blue",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=1,padx=5,pady=1)
        #================== Delete Button==================
        delete_btn=Button(button_frame,text="Delete",font=("arial", 9, "bold"),width=14,bg="blue",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=2,padx=5,pady=1)
        #================== Clear Button==================
        clear_btn=Button(button_frame,text="Clear",font=("arial", 9, "bold"),width=14,bg="blue",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=3,padx=5,pady=1)

        #============Side BG Image================
        side_bg_img = Image.open('side image.jpg')
        side_bg_img = side_bg_img.resize((450, 200), Image.ANTIALIAS)
        self.photo_crime = ImageTk.PhotoImage(side_bg_img)
        self.img_crime = Label(insert_data_frame, image=self.photo_crime, )
        self.img_crime.place(x=820, y=7, width=450, height=200)



        # ============== Criminal Data Detail Frame=================
        data_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Criminal Detail", fg="red",bg="white", font=("times new roman", 11, "bold"))
        data_frame.place(x=10, y=250, width=1305, height=80)

        # ============== Criminal Search Frame=================
        search_frame = LabelFrame(data_frame, bd=5, relief=GROOVE, text="Search Criminal Record", fg=frame_hading, bg=bg_color,font=("times new roman", 11, "bold"))
        search_frame.place(x=5, y=0, width=1290, height=60)
        search_by = Label(search_frame, text="Search By :", bg="red",fg="white", font=("arial", 10, "bold"), ).grid(row=0, column=0, padx=5, sticky=W, pady=7)
        combo_search_box=ttk.Combobox(search_frame,font=("arial", 10, "bold"),width=18,state='read')
        combo_search_box['value']=('Select Option','Case ID','Criminal No','CNIC No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=5, sticky=W, pady=7)
        #============Search Entry Button============
        search_entry = ttk.Entry(search_frame, width=20, font=("arial", 10),).grid(row=0,column=2, padx=5,sticky=W,pady=7)
        #================== Search Button==================
        search_btn=Button(search_frame,text="Search",font=("arial", 9, "bold"),width=14,bg="green",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=3,padx=5,pady=1)
        #================== All Search Button==================
        all_search_btn=Button(search_frame,text="Clear",font=("arial", 9, "bold"),width=14,bg="green",fg="white", bd=5, relief=GROOVE,).grid(row=0,column=4,padx=5,pady=1)

        lable_logo = Label(search_frame, text="Intelligence Bureau of Pakistan", fg="White",bg=bg_color, font=("times new roman", 22, "bold"), ).grid(row=0, column=5, padx=100, sticky=W, pady=0)

        #==============Table Frame===============
        criminal_data_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,  fg="red",bg="white", font=("times new roman", 11, "bold"))
        criminal_data_frame.place(x=10, y=340, width=1305, height=150)
        #===============Scrol Bar=====================
        scroll_x=ttk.Scrollbar(criminal_data_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(criminal_data_frame, orient=VERTICAL)

        self.criminal_data_table=ttk.Treeview(criminal_data_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_data_table.xview)
        scroll_y.config(command=self.criminal_data_table.yview)

        self.criminal_data_table.heading('1',text="Case ID")
        self.criminal_data_table.heading('2',text="Criminal No")
        self.criminal_data_table.heading('3',text="Criminal Name")
        self.criminal_data_table.heading('4',text="Nick Name")
        self.criminal_data_table.heading('5',text="Father Name")
        self.criminal_data_table.heading('6',text="CNIC No")
        self.criminal_data_table.heading('7',text="Criminal Age")
        self.criminal_data_table.heading('8',text="Birth Mark")
        self.criminal_data_table.heading('9',text="Address")
        self.criminal_data_table.heading('10',text="Occupation")
        self.criminal_data_table.heading('11',text="Arrest Date")
        self.criminal_data_table.heading('12',text="Crime Type")
        self.criminal_data_table.heading('13',text="Date Of Crime")
        self.criminal_data_table.heading('14',text="Gender")
        self.criminal_data_table.heading('15',text="Most Wanted")

        self.criminal_data_table['show']='headings'

        self.criminal_data_table.column("1",width=100)
        self.criminal_data_table.column("2",width=100)
        self.criminal_data_table.column("3",width=150)
        self.criminal_data_table.column("4",width=100)
        self.criminal_data_table.column("5",width=150)
        self.criminal_data_table.column("6",width=150)
        self.criminal_data_table.column("7",width=150)
        self.criminal_data_table.column("8",width=100)
        self.criminal_data_table.column("9",width=200)
        self.criminal_data_table.column("10",width=150)
        self.criminal_data_table.column("11",width=150)
        self.criminal_data_table.column("12",width=150)
        self.criminal_data_table.column("13",width=150)
        self.criminal_data_table.column("14",width=100)
        self.criminal_data_table.column("15",width=100)


        self.criminal_data_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    #================= Add Function===============
    def add_data(self):
        if self.case_id.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.criminal_no.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.criminal_name.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.nick_name.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.father_name.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.cnic_no.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.age.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.birth_mark.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.address.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.occupation.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.arrest_date.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.crime_type.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.date_of_crime.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.gender.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.most_wanted.get()=="":
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host='localhost',username='root',password='Sallu410802',database='menagement')
                my_cursor=connection.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.case_id.get(),
                                                                                                                self.criminal_no.get(),
                                                                                                                self.criminal_name.get(),
                                                                                                                self.nick_name.get(),
                                                                                                                self.father_name.get(),
                                                                                                                self.cnic_no.get(),
                                                                                                                self.age.get(),
                                                                                                                self.birth_mark.get(),
                                                                                                                self.address.get(),
                                                                                                                self.occupation.get(),
                                                                                                                self.arrest_date.get(),
                                                                                                                self.crime_type.get(),
                                                                                                                self.date_of_crime.get(),
                                                                                                                self.gender.get(),
                                                                                                                self.most_wanted.get()

                                                                                                                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Criminal Record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')
        #=================== Fatch Data=================
    def fetch_data(self):
        connection = mysql.connector.connect(host='localhost', username='root', password='Sallu410802',database='menagement')
        my_cursor = connection.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(rows)!=0:
            self.criminal_data_table.delete(*self.criminal_data_table.get_children())
            for i in rows:
                self.criminal_data_table("",END,values=i)
            connection.commit()
        connection.close()




if __name__ == '__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()