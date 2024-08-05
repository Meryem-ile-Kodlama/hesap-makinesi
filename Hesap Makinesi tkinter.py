from tkinter import *

def butona_basildi(giris):
    global denklem
    denklem = denklem + str(giris)
    denklem_degeri.set(denklem)

def sonuc():
    global denklem
    try:
        islem_sonucu = str(eval(denklem))
        denklem_degeri.set(islem_sonucu)
        denklem = islem_sonucu
    except:
        denklem_degeri.set("HATA")
        denklem = ""

def ekrani_temizle():
    global denklem
    denklem_degeri.set("")
    denklem = ""

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x480")

denklem = ""

denklem_degeri = StringVar()

denklem_yazisi = Label(pencere, textvariable=denklem_degeri, font=("consolas",20),bg="white", width=24, height=2)
denklem_yazisi.pack()

cerceve = Frame(pencere)
cerceve.pack(pady=5)

buton1 = Button(cerceve, text="1", height=4, width=7, font= 35,
                command= lambda: butona_basildi(1))
buton1.grid(row=0, column=0)

buton2 = Button(cerceve, text="2", height=4, width=7, font= 35,
                command= lambda: butona_basildi(2))
buton2.grid(row=0, column=1)

buton3 = Button(cerceve, text="3", height=4, width=7, font= 35,
                command= lambda: butona_basildi(3))
buton3.grid(row=0, column=2)

buton4 = Button(cerceve, text="4", height=4, width=7, font= 35,
                command= lambda: butona_basildi(4))
buton4.grid(row=1, column=0)

buton5 = Button(cerceve, text="5", height=4, width=7, font= 35,
                command= lambda: butona_basildi(5))
buton5.grid(row=1, column=1)

buton6 = Button(cerceve, text="6", height=4, width=7, font= 35,
                command= lambda: butona_basildi(6))
buton6.grid(row=1, column=2)

buton7 = Button(cerceve, text="7", height=4, width=7, font= 35,
                command= lambda: butona_basildi(7))
buton7.grid(row=2, column=0)

buton8 = Button(cerceve, text="8", height=4, width=7, font= 35,
                command= lambda: butona_basildi(8))
buton8.grid(row=2, column=1)

buton9 = Button(cerceve, text="9", height=4, width=7, font= 35,
                command= lambda: butona_basildi(9))
buton9.grid(row=2, column=2)

buton0 = Button(cerceve, text="0", height=4, width=7, font= 35,
                command= lambda: butona_basildi(0))
buton0.grid(row=3, column=0)

toplama = Button(cerceve, text="+", height=4, width=7, font= 35,
                command= lambda: butona_basildi("+"))
toplama.grid(row=0, column=3)

cikarma = Button(cerceve, text="-", height=4, width=7, font= 35,
                command= lambda: butona_basildi("-"))
cikarma.grid(row=1, column=3)

carpma = Button(cerceve, text="*", height=4, width=7, font= 35,
                command= lambda: butona_basildi("*"))
carpma.grid(row=2, column=3)

bolme = Button(cerceve, text="/", height=4, width=7, font= 35,
                command= lambda: butona_basildi("/"))
bolme.grid(row=3, column=3)

esittir = Button(cerceve, text="=", height=4, width=7, font= 35,
                command= sonuc)
esittir.grid(row=3, column=2)

virgul = Button(cerceve, text=",", height=4, width=7, font= 35,
                command= lambda: butona_basildi("."))
virgul.grid(row=3, column=1)

temizle = Button(pencere, text="Temizle", height=2, width=28, font=35,
                 command=ekrani_temizle)
temizle.pack()

pencere.mainloop()