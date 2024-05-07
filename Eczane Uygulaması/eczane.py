

from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from tkinter import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_msgbox(hata_kodu,mesaj_text,icon,pencere):
    mesaj = tk.Toplevel(pencere)

    mesaj.title(hata_kodu)
    mesaj.geometry("300x100")

    l1 = tk.Label(mesaj, image="::tk::icons::"+icon)
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(mesaj, text=mesaj_text)
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(mesaj, text="Tamam", command=mesaj.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")


    mesaj.update_idletasks()
    x = pencere.winfo_rootx() + (pencere.winfo_width() - mesaj.winfo_width()) // 2
    y = pencere.winfo_rooty() + (pencere.winfo_height() - mesaj.winfo_height()) // 2
    mesaj.geometry(f"300x100+{x}+{y}")





class Uygulama():
    def __init__(self):
        self.ana_panel()


    def veritabani(self):

        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_ecza"
            )


    ##################################  ANA PENCERE VE FONKSİYONLARI  #####################################
    def ana_panel(self):
        self.window = Tk()

        self.window.geometry("1000x600")
        self.window.configure(bg="#A0B2B0")
        self.window.title("Eczane")

        self.canvas = Canvas(
            self.window,
            bg="#A0B2B0",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=1, y=1)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("wall.png"))
        image_1 = self.canvas.create_image(
            500.0,
            250.0,
            image=self.image_image_1
        )

        self.anti = IntVar()
        self.agri = IntVar()
        self.vitamin = IntVar()
        self.tablet=IntVar()
        self.surup=IntVar()
        self.krem=IntVar()


        self.c_anti = tk.Checkbutton(self.window, text='Antibiyotik',variable=self.anti, onvalue=1, offvalue=0,bg='yellow',command=self.anti_call)
        self.c_anti.place(x=50, y = 10)
        self.c_agri = tk.Checkbutton(self.window, text='Ağrı kesici', variable=self.agri,onvalue=1, offvalue=0, bg='yellow',command=self.agri_call)
        self.c_agri.place(x=170, y=10)
        self.c_vitamin = tk.Checkbutton(self.window, text='Vitamin', variable=self.vitamin,onvalue=1, offvalue=0, bg='yellow',command=self.vitamin_call)
        self.c_vitamin.place(x=290, y=10)
        self.c_tablet = tk.Checkbutton(self.window, text='Tablet',variable=self.tablet, onvalue=1, offvalue=0, bg='light blue',command=self.tablet_call)
        self.c_tablet.place(x=50, y=60)
        self.c_surup = tk.Checkbutton(self.window, text='Şurup', variable=self.surup,onvalue=1, offvalue=0, bg='light blue',command=self.surup_call)
        self.c_surup.place(x=170, y=60)
        self.c_krem = tk.Checkbutton(self.window, text='Krem',variable=self.krem, onvalue=1, offvalue=0, bg='light blue',command=self.krem_call)
        self.c_krem.place(x=280, y=60)






        self.table_frame=Frame(self.window,bd=10,relief=RIDGE,bg="Light blue")
        self.table_frame.place(x=400,y=0,width=600,height=600)

        self.scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=ttk.Scrollbar(self.table_frame, orient=VERTICAL)
        self.ilac_tablo=ttk.Treeview(self.table_frame,columns=("id","a_m","a_km","a_vites",
        "saatlik","haftalik","kira"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.ilac_tablo.xview)
        self.scroll_y.config(command=self.ilac_tablo.yview)

        self.ilac_tablo.heading("id",text="İlaç id",anchor=W)
        self.ilac_tablo.heading("a_m", text="İlaç adı",anchor=W)
        self.ilac_tablo.heading("a_km", text="Türü",anchor=W)
        self.ilac_tablo.heading("a_vites", text="Kategori",anchor=W)
        self.ilac_tablo.heading("saatlik", text="Kullanım",anchor=W)
        self.ilac_tablo.heading("haftalik", text="STK",anchor=W)
        self.ilac_tablo.heading("kira", text="Stok",anchor=W)

        self.ilac_tablo.column("id", width=60)
        self.ilac_tablo.column("a_m", width=70)
        self.ilac_tablo.column("a_km", width=80)
        self.ilac_tablo.column("a_vites", width=60)
        self.ilac_tablo.column("saatlik", width=170)
        self.ilac_tablo.column("haftalik", width=80)
        self.ilac_tablo.column("kira", width=90)

        self.ilac_tablo["show"]="headings"
        self.ilac_tablo.pack(fill=BOTH,expand=1)

        self.canvas.create_text(60, 200, text="İlaç adı:",font=("Impact", 25),  fill="#024452")
        self.entry_ilac = tk.Entry(self.window,width=30,bg="Light Blue")
        self.entry_ilac.place(x=10, y=230)

        self.ara_image_1 = PhotoImage(
            file=relative_to_assets("ara.png"))
        self.ara = Button(
            image=self.ara_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.ara,
            relief="flat"
        )
        self.ara.place(
            x=90.0,
            y=285.0,
            width=100.0,
            height=44.0
        )
        self.guncelle_image=PhotoImage(
            file=relative_to_assets("guncelle.png"))
        self.guncelle = Button(
            image=self.guncelle_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.guncelleme_pencere_cagir,
            relief="flat"
        )
        self.guncelle.place(
            x=280.0,
            y=500.0,
            width=100.0,
            height=50.0
        )


        self.window.resizable(False, False)
        self.window.mainloop()

    def ara(self):
        ilac_ismi = self.entry_ilac.get()
        self.veritabani()
        self.sql = "SELECT * FROM ilaclar WHERE ilac_adi = %s"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql, (ilac_ismi,))
        self.rows = self.mycursor.fetchall()
        if not ilac_ismi.strip():
            login_msgbox("HATA!", "İlaç adı giriniz!", "warning",self.window)
        try:
            if len(self.rows) > 0:
                self.ilac_tablo.delete(*self.ilac_tablo.get_children())
                for i in self.rows:
                    self.ilac_tablo.insert("", END, values=i)
                self.mydb.commit()
        except Exception as e:
            login_msgbox("Hata", f"Kiralama işlemi sırasında bir hata oluştu: {e}", "error", self.kullanici_window)

    def sql_veri(self, turu, kategori, kategori2=None):
        self.veritabani()
        if kategori2:
            self.sql = f"SELECT * FROM ilaclar WHERE turu='{turu}' AND (kategori='{kategori}' OR kategori='{kategori2}')"
        else:
            self.sql = f"SELECT * FROM ilaclar WHERE turu='{turu}' AND kategori='{kategori}'"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql)

        self.rows = self.my_cursor1.fetchall()
        if len(self.rows)>=0:
            self.ilac_tablo.delete(*self.ilac_tablo.get_children())
            for i in self.rows:
                self.ilac_tablo.insert("",END,values=i)
            self.mydb.commit()

    def anti_call(self):
        if self.anti.get() == 1:
            self.agri.set(0)
            self.vitamin.set(0)
            self.veritabani()
            self.sql="Select * from ilaclar where turu='Antibiyotik'"
            self.my_cursor1 = self.mydb.cursor()
            self.my_cursor1.execute(self.sql,)

            self.rows = self.my_cursor1.fetchall()

            if len(self.rows) != 0:
                self.ilac_tablo.delete(*self.ilac_tablo.get_children())
                for i in self.rows:
                    self.ilac_tablo.insert("", END, values=i)
                self.mydb.commit()

    def agri_call(self):
        if self.agri.get() == 1:
            self.anti.set(0)
            self.vitamin.set(0)
            self.veritabani()
            self.sql="Select * from ilaclar where turu='Ağrı kesici'"
            self.my_cursor1 = self.mydb.cursor()
            self.my_cursor1.execute(self.sql,)

            self.rows = self.my_cursor1.fetchall()

            if len(self.rows) != 0:
                self.ilac_tablo.delete(*self.ilac_tablo.get_children())
                for i in self.rows:
                    self.ilac_tablo.insert("", END, values=i)
                self.mydb.commit()

    def tablet_call(self):
        if self.tablet.get() == 1:
            if self.surup.get() == 1:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Tablet", "Şurup")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Tablet", "Şurup")
                    else:
                        self.sql_veri("Ağrı kesici", "Tablet", "Şurup")
            elif self.krem.get() == 1:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Tablet", "Krem")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Tablet", "Krem")
                    else:
                        self.sql_veri("Ağrı kesici", "Tablet", "Krem")
            else:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Tablet")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Tablet")
                    else:
                        self.sql_veri("Ağrı kesici", "Tablet")

    def surup_call(self):
        if self.surup.get() == 1:
            if self.tablet.get() == 1:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Şurup", "Tablet")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Şurup", "Tablet")
                    else:
                        self.sql_veri("Ağrı kesici", "Şurup", "Tablet")
            elif self.krem.get() == 1:  # Burası krem checkbox'unun durumunu kontrol ediyor
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Şurup", "Krem")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Şurup", "Krem")
                    else:
                        self.sql_veri("Ağrı kesici", "Şurup", "Krem")
            else:  # Eğer tablet veya krem seçili değilse, sadece şurup ilaçları getirilir
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Şurup")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Şurup")
                    else:
                        self.sql_veri("Ağrı kesici", "Şurup")

    def krem_call(self):
        if self.krem.get() == 1:
            if self.tablet.get() == 1:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Krem", "Tablet")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Krem", "Tablet")
                    else:
                        self.sql_veri("Ağrı kesici", "Krem", "Tablet")
            elif self.surup.get() == 1:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Krem", "Şurup")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Krem", "Şurup")
                    else:
                        self.sql_veri("Ağrı kesici", "Krem", "Şurup")
            else:
                if self.anti.get() == 1:
                    self.sql_veri("Antibiyotik", "Krem")
                elif self.anti.get() == 0:
                    if self.vitamin.get() == 1:
                        self.sql_veri("Vitamin", "Krem")
                    else:
                        self.sql_veri("Ağrı kesici", "Krem")

    def vitamin_call(self):
        if self.vitamin.get() ==1:
            self.agri.set(0)
            self.anti.set(0)
            self.veritabani()
            self.sql="Select * from ilaclar where turu='Vitamin'"
            self.my_cursor1 = self.mydb.cursor()
            self.my_cursor1.execute(self.sql,)

            self.rows = self.my_cursor1.fetchall()

            if len(self.rows) != 0:
                self.ilac_tablo.delete(*self.ilac_tablo.get_children())
                for i in self.rows:
                    self.ilac_tablo.insert("", END, values=i)
                self.mydb.commit()

    def guncelleme_pencere_cagir(self):
        self.window.destroy()
        self.guncelleme_panel()
##################################  GUNCELLEME PENCERESİ VE FONKSİYONLARI  #####################################

    def guncelleme_panel(self):
        self.guncelle_win = Tk()

        self.guncelle_win.geometry("1000x600")
        self.guncelle_win.configure(bg="#FFFFFF")
        self.guncelle_win.title("Eczane")

        self.main_canvas = Canvas(
        self.guncelle_win,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.main_canvas.place(x = 1, y = 1)
        self.main_image_image_1 = PhotoImage(
            file=relative_to_assets("wall.png"))
        self.main_image_1 = self.main_canvas.create_image(
            500.0,
            250.0,
            image=self.main_image_image_1
        )

        self.main_canvas.create_text(
            182.0,
            5.0,
            anchor="nw",
            text="       EMRE ECZANE",
            fill="#2d1ba1",
            font=("KumarOne Regular", 25 * -1)
        )

        self.main_entry_image_1 = PhotoImage(
            file=relative_to_assets("main_entry_3.png"))
        self.main_entry_bg_1 = self.main_canvas.create_image(
            112.0,
            139.0,
            image=self.main_entry_image_1
        )
        self.main_entry_1 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_1.place(
            x=44.0,
            y=120.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            31.0,
            96.0,
            anchor="nw",
            text="İlaç adı:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_entry_image_2 = PhotoImage(
            file=relative_to_assets("main_entry_3.png"))
        self.main_entry_bg_2 = self.main_canvas.create_image(
            110.0,
            220.0,
            image=self.main_entry_image_2
        )
        self.main_entry_2 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_2.place(
            x=42.0,
            y=199.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            165.0,
            anchor="nw",
            text="İlaç türü:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_entry_image_3 = PhotoImage(
            file=relative_to_assets("main_entry_3.png"))
        self.main_entry_bg_3 = self.main_canvas.create_image(
            110.0,
            275.0,
            image=self.main_entry_image_3
        )
        self.main_entry_3 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_3.place(
            x=42.0,
            y=258.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            234.0,
            anchor="nw",
            text="Kategori:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_entry_image_4 = PhotoImage(
            file=relative_to_assets("main_entry_4.png"))
        self.main_entry_bg_4 = self.main_canvas.create_image(
            110.0,
            352.0,
            image=self.main_entry_image_4
        )
        self.main_entry_4 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_4.place(
            x=42.0,
            y=334.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            31.0,
            302.0,
            anchor="nw",
            text="Kullanım:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_entry_image_5 = PhotoImage(
            file=relative_to_assets("main_entry_5.png"))
        self.main_entry_bg_5 = self.main_canvas.create_image(
            110.0,
            415.0,
            image=self.main_entry_image_5
        )
        self.main_entry_5 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_5.place(
            x=42.0,
            y=396.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            373.0,
            anchor="nw",
            text="Stk:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_entry_image_6 = PhotoImage(
            file=relative_to_assets("main_entry_6.png"))
        self.main_entry_bg_6 = self.main_canvas.create_image(
            110.0,
            484.0,
            image=self.main_entry_image_6
        )
        self.main_entry_6 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_6.place(
            x=42.0,
            y=465.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            438.0,
            anchor="nw",
            text="Stok:",
            fill="#000000",
            font=("İmpact", 20 * -1)
        )

        self.main_button_image_1 = PhotoImage(
            file=relative_to_assets("main_button_1.png"))
        self.main_button_1 = Button(
            image=self.main_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.tablo_kayit_button,
            relief="flat"
        )
        self.main_button_1.place(
            x=248.0,
            y=480.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_2 = PhotoImage(
            file=relative_to_assets("main_button_2.png"))
        self.main_button_2 = Button(
            image=self.main_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.guncelle_ilac,
            relief="flat"
        )
        self.main_button_2.place(
            x=248.0,
            y=420.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_3 = PhotoImage(
            file=relative_to_assets("main_button_3.png"))
        self.main_button_3 = Button(
            image=self.main_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.silme_islemi,
            relief="flat"
        )
        self.main_button_3.place(
            x=248.0,
            y=360.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_4 = PhotoImage(
            file=relative_to_assets("geri.png"))
        self.main_button_4 = Button(
            image=self.main_button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.geri_gel,
            relief="flat"
        )
        self.main_button_4.place(
            x=0.0,
            y=0.0,
            width=104.0,
            height=44.0
        )


        self.table_frame1=Frame(self.guncelle_win,bd=10,relief=RIDGE,bg="Light blue")
        self.table_frame1.place(x=400,y=0,width=600,height=600)

        self.scroll_x1=ttk.Scrollbar(self.table_frame1,orient=HORIZONTAL)
        self.scroll_y1=ttk.Scrollbar(self.table_frame1, orient=VERTICAL)
        self.ilac_tablo1=ttk.Treeview(self.table_frame1,columns=("id","a_m","a_km","a_vites",
        "saatlik","haftalik","kira"), xscrollcommand=self.scroll_x1.set, yscrollcommand=self.scroll_y1.set)

        self.scroll_x1.pack(side=BOTTOM, fill=X)
        self.scroll_y1.pack(side=RIGHT, fill=Y)

        self.scroll_x1.config(command=self.ilac_tablo1.xview)
        self.scroll_y1.config(command=self.ilac_tablo1.yview)

        self.ilac_tablo1.heading("id",text="İlaç id",anchor=W)
        self.ilac_tablo1.heading("a_m", text="İlaç adı",anchor=W)
        self.ilac_tablo1.heading("a_km", text="Türü",anchor=W)
        self.ilac_tablo1.heading("a_vites", text="Kategori",anchor=W)
        self.ilac_tablo1.heading("saatlik", text="Kullanım",anchor=W)
        self.ilac_tablo1.heading("haftalik", text="STK",anchor=W)
        self.ilac_tablo1.heading("kira", text="Stok",anchor=W)

        self.ilac_tablo1.column("id", width=60)
        self.ilac_tablo1.column("a_m", width=70)
        self.ilac_tablo1.column("a_km", width=80)
        self.ilac_tablo1.column("a_vites", width=60)
        self.ilac_tablo1.column("saatlik", width=170)
        self.ilac_tablo1.column("haftalik", width=80)
        self.ilac_tablo1.column("kira", width=90)

        self.veri_aktarimi()

        self.ilac_tablo1["show"]="headings"
        self.ilac_tablo1.pack(fill=BOTH,expand=1)

        self.ilac_tablo1.bind("<ButtonRelease-1>", self.get_cursor_row)


        self.guncelle_win.resizable(False, False)
        self.guncelle_win.mainloop()

    def guncelle_ilac(self):
        selected_item = self.ilac_tablo1.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.guncelle_win)
            return

        ilac_id = self.ilac_tablo1.item(selected_item)['values'][0]

        yeni_ilac = self.main_entry_1.get()
        yeni_turu = self.main_entry_2.get()
        yeni_kategori = self.main_entry_3.get()
        yeni_kullanim = self.main_entry_4.get()
        yeni_stk = self.main_entry_5.get()
        yeni_stok = self.main_entry_6.get()

        guncelle_query_parts = []


        if not ilac_id:  # Eğer seçilmediyse
            login_msgbox("HATA!", "Güncellenecek bir alan seçilmedi!", "error", self.guncelle_win)
            return

        update_query = "UPDATE ilaclar SET ilac_adi=%s , turu=%s , kategori=%s , kullanim=%s , stk=%s , Stok=%s WHERE id = %s"
        #self.my_cursor.execute(update_query, (yeni_marka, yeni_km,yeni_vites,yeni_saatlik_ucret,yeni_gunluk_ucret,yeni_kira_durumu))

        print("Sorgu:", update_query)

        try:
            self.my_cursor.execute(update_query, (yeni_ilac, yeni_turu,yeni_kategori,yeni_kullanim,yeni_stk,yeni_stok,ilac_id))
            self.mydb.commit()
            login_msgbox("BAŞARILI", "İlaç bilgileri güncellendi!", "information", self.guncelle_win)
            # Veri tablosunu güncelle
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"İla. bilgileri güncellenemedi: {e}", "error", self.guncelle_win)

    def silme_islemi(self):

        selected_item = self.ilac_tablo1.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir araç seçin!", "warning", self.guncelle_win)
            return

        select = self.ilac_tablo1.item(selected_item)['values'][0]


        self.sql_guncelle_delete = "DELETE from ilaclar WHERE id = %s"

        try:
            self.my_cursor.execute(self.sql_guncelle_delete, ( select,))
            self.mydb.commit()

            # Güncelleme başarılıysa Treeview'daki veriyi güncelle
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"Kayıt silinemedi: {e}", "error", self.guncelle_win)

    def tablo_kayit_button(self):
        self.veritabani()

        self.giris1 = self.main_entry_1.get()
        self.giris2 = self.main_entry_2.get()
        self.giris3 = self.main_entry_3.get()
        self.giris4 = self.main_entry_4.get()
        self.giris5 = self.main_entry_5.get()
        self.giris6 = self.main_entry_6.get()

        # Eğer `self.mydb` değeri `None` ise, cursor oluşturmayın
        if self.mydb:
            self.my_cursor = self.mydb.cursor()
            self.sql_tablo_veri = "INSERT INTO ilaclar (ilac_adi, turu, kategori, kullanim, stk, Stok) VALUES (%s, %s, %s, %s, %s, %s)"
            if not self.giris1.strip() or not self.giris2.strip() or not self.giris3.strip() or not self.giris4.strip() or not self.giris5.strip() or not self.giris6.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.guncelle_win)
            else:
                self.my_cursor.execute(self.sql_tablo_veri,
                                       (self.giris1, self.giris2, self.giris3, self.giris4, self.giris5, self.giris6))
                self.mydb.commit()
                self.veri_aktarimi()
                login_msgbox("Tebrikler!","Kayıt başarılı!","information",self.guncelle_win)
        else:
            login_msgbox("HATA!", "Veritabanı bağlantı hatası!", "error", self.guncelle_win)

    def veri_aktarimi(self):
        self.veritabani()
        self.sql_veri_aktarimi="select * from ilaclar"
        self.my_cursor = self.mydb.cursor()
        self.my_cursor.execute(self.sql_veri_aktarimi)
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.ilac_tablo1.delete(*self.ilac_tablo1.get_children())
            for i in self.rows:
                self.ilac_tablo1.insert("",END,values=i)
            self.mydb.commit()

    def get_cursor_row(self, event=""):
        cursor_row = self.ilac_tablo1.focus()
        content = self.ilac_tablo1.item(cursor_row)
        row = content["values"]

        # Entry widget'larını güncelle
        self.main_entry_1.delete(0, END)
        self.main_entry_1.insert(0, row[1] if row and len(row) > 0 else "")

        self.main_entry_2.delete(0, END)
        self.main_entry_2.insert(0, row[2] if row and len(row) > 1 else "")

        self.main_entry_3.delete(0, END)
        self.main_entry_3.insert(0, row[3] if row and len(row) > 2 else "")

        self.main_entry_4.delete(0, END)
        self.main_entry_4.insert(0, row[4] if row and len(row) > 3 else "")

        self.main_entry_5.delete(0, END)
        self.main_entry_5.insert(0, row[5] if row and len(row) > 4 else "")

        self.main_entry_6.delete(0, END)
        self.main_entry_6.insert(0, row[6] if row and len(row) > 5 else "")

    def geri_gel(self):
        self.guncelle_win.destroy()
        self.ana_panel()




app=Uygulama()