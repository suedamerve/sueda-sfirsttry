# tkinterin orneklenmesi
from tkinter import * 
# tarih icin orneklenen kutuphane
from tkcalendar import DateEntry
master = Tk()

canvas = Canvas(master, height = 450 , width = 750)
# canvasi ebeveyn widget e ekleme metotlari
# pack
# place 
# grid
canvas.pack()   

# frameler icerisindeki objelere ebeveyn gibi davranabilir

#*************** PART1

# hatirlatma tipi ve tarihin bulundugu kisim
frame_ust = Frame(master , bg = "#add8e6")
frame_ust.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

# hatirlatma yonteminin bulunacagi kisim
frame_alt_sol = Frame(master , bg = "#add8e6")
frame_alt_sol.place(relx = 0.1, rely = 0.21, relwidth = 0.23, relheight = 0.5)

# hatirlatma mesajinin bulunacagi kisim
frame_alt_sag = Frame(master , bg = "#add8e6")
frame_alt_sag.place(relx = 0.34, rely = 0.21, relwidth = 0.56, relheight = 0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg = "#add8e6", text= "Hatirlatma tipi:", font= "Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side= LEFT)   


# hatirlatma tipi kisminda gozukecek tipler 
hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t") #default bos bir deger olusturduk
hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust, 
    hatirlatma_tipi_opsiyon,
    "Dogum Gunu",
    "Alisveris",
    "odeme")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side= LEFT)

# hatirlatma tarih secici olusturucu
hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background="orange", foreground="black", borderwidth=1, locale="de_DE")
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)

# hatirlatma tarihinin etiketi
hatirlatma_tarihi_etiket = Label(frame_ust, bg = "#add8e6", text= "Hatirlatma Tarihi:", font= "Verdana 12 bold")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side= RIGHT)   

#************** PART2

Label(frame_alt_sol,text="Hatirlatma Yontemi",bg = "#add8e6", font= "Verdana 10 bold").pack(padx=10, pady=10,anchor=NW)
#anchor pusula gibi ve yonleriyle calisir

var = IntVar()
##radiobutton yuvarlak olan secicileri olusturmaya yarar
R1= Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable= var, value= 1, bg = "#add8e6", font= "Verdana 10 ")
R1.pack(anchor= NW, padx= 15, pady= 5)

R2= Radiobutton(frame_alt_sol, text="E-Posta Gonder", variable= var, value= 2, bg = "#add8e6", font= "Verdana 10 ")
R2.pack(anchor= NW, padx= 15, pady= 5)

## checkbutton kare seklindeki kutucuklari yapmaya yarar
## chechbox lar bir arada secilebilir birbirlerine baglidirlar
### secili andaki seneryo icin onvalue olmayan anindaki senaryo icin offvalue kullandim
### 1 ise varieble uzerinden atama islemi yapiyorum
var1= IntVar()
C1 = Checkbutton(frame_alt_sol, text= "1 Hafta Once", variable= var1 , onvalue= 1, offvalue= 0,  bg = "#add8e6", font= "Verdana 10 ")
C1.pack(anchor= NW, padx = 30, pady= 2)

#ayri ayri tam sayi degeri olusturulur --= var 
var2= IntVar()
C2 = Checkbutton(frame_alt_sol, text= "1 Gun Once", variable= var2 , onvalue= 1, offvalue= 0,  bg = "#add8e6", font= "Verdana 10 ")
C2.pack(anchor= NW, padx = 30, pady= 2)

var3= IntVar()
C3 = Checkbutton(frame_alt_sol, text= "Ayni Gun", variable= var3 , onvalue= 1, offvalue= 0,  bg = "#add8e6", font= "Verdana 10 ")
C3.pack(anchor= NW, padx = 30, pady= 2)



#PART4
# gonder tusuna basildiginda olusacak islemler
from tkinter import messagebox

def gonder():
    try:
        son_mesaj = ""
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz basariyla sisteme kaydedilmistir"
                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() != "" else "Genel"
                tarih = hatirlatma_tarih_secici.get()
                mesaj = metin_alani.get("1.0", "end")
                
                # with komutu islem yapilirken ac sonra kapat anlamina gelir
                with open("hatirlatmalar.txt", "a") as dosya:  # Append mode
                    dosya.write(
                        "{} kategorisinde, {} tarihine ve {} notuyla hatirlatma\n".format(tip, tarih, mesaj)
                    )
                    
            elif var.get() == 2:
                son_mesaj += "E-posta ile hatirlatma size ulasacaktir"
                
            messagebox.showinfo("Basarili islem", son_mesaj)
        else:
            son_mesaj += "Gerekli alanlarin dolduruldugundan emin olun"
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)
    except Exception as e:
        son_mesaj += "Islem basarisiz oldu: " + str(e)
        messagebox.showerror("Basarisiz islem", son_mesaj)
    finally:
        master.destroy()  # Make sure 'master' is defined somewhere in your code
   
 
    
   
#PART3 
# hatirlatma mesaji ve gonderme butonu
Label(frame_alt_sag, text= "Hatirlatma Mesaji", bg = "#add8e6", font= "Verdana 10 bold").pack(padx=10, pady=10,anchor=NW)

# text alani eklemek#
metin_alani = Text(frame_alt_sag, height= 9, width= 50)
metin_alani.tag_configure("style", foreground="#bfbfbf", font= "Verdana 7 bold")
metin_alani.pack()

karsilama_metin = "Mesajını buraya gir..."
metin_alani.insert(END, karsilama_metin, "style")

## buton ekleme 
# buton mantigi nerede olsun ne yazsin ne yapsin
gonder_butonu = Button(frame_alt_sag, text= "Gonder", command= gonder)
gonder_butonu.pack(anchor=S)






# calistiginda ekranda durmasi icin loop a sokma
master.mainloop()