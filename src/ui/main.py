import sys
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import winsound # Windows için ses kütüphanesi eklendi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.models import Kullanici, SuTakipSistemi

def arayuzu_baslat():
    root = tk.Tk()
    root.withdraw()

    isim = simpledialog.askstring("Giriş", "Lütfen adınızı girin:")
    if not isim: return

    while True:
        hedef_str = simpledialog.askstring("Hedef", "Günlük su hedefinizi (ml) girin (Örn: 2500):")
        if not hedef_str: return
        try:
            hedef = int(hedef_str)
            break
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sadece sayı giriniz!")
            
    aktif_kullanici = Kullanici(isim, hedef)
    takip_sistemi = SuTakipSistemi(aktif_kullanici)

    ana_pencere = tk.Toplevel()
    ana_pencere.title("Günlük Su Takibi")
    ana_pencere.geometry("300x250")
    ana_pencere.configure(bg="#f0f8ff")

    # İkon Yükleme
    try:
        ikon_yolu = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../assets/icons/icon.ico'))
        ana_pencere.iconbitmap(ikon_yolu)
    except:
        pass

    tk.Label(ana_pencere, text=f"Hoş geldin, {isim}!", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(pady=10)
    tk.Label(ana_pencere, text=f"Günlük Hedefin: {aktif_kullanici.gunluk_hedef} ml", font=("Arial", 10), bg="#f0f8ff").pack()

    # Eğer JSON'dan veri geldiyse 0 yerine kaldığı yerden başlar
    durum_etiketi = tk.Label(ana_pencere, text=f"İçilen Su: {aktif_kullanici.icilen_su} ml", font=("Arial", 12, "bold"), fg="blue", bg="#f0f8ff")
    durum_etiketi.pack(pady=15)

    def su_ekle_buton_tiklandi():
        miktar_str = simpledialog.askstring("Su Ekle", "Kaç ml su içtiniz?", parent=ana_pencere)
        if miktar_str:
            try:
                miktar = int(miktar_str)
                takip_sistemi.su_ekle(miktar)
                durum_etiketi.config(text=f"İçilen Su: {aktif_kullanici.icilen_su} ml")
                
                # SES EFEKTİ ÇALMA KISMI
                try:
                    ses_yolu = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../assets/sounds/su_sesi.wav'))
                    winsound.PlaySound(ses_yolu, winsound.SND_FILENAME | winsound.SND_ASYNC)
                except:
                    pass 
                
                kalan = takip_sistemi.kalan_hedef_hesapla()
                if kalan <= 0:
                    messagebox.showinfo("Tebrikler!", "Günlük su hedefinize ulaştınız!")
                else:
                    messagebox.showinfo("Bilgi", f"Hedefe ulaşmak için {kalan} ml daha içmelisiniz.")
            except ValueError:
                messagebox.showerror("Hata", "Su miktarı sadece sayı olmalıdır!")

    btn_ekle = tk.Button(ana_pencere, text="Su İçtim Ekle (+)", command=su_ekle_buton_tiklandi, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    btn_ekle.pack(pady=5)

    btn_cikis = tk.Button(ana_pencere, text="Çıkış Yap", command=root.quit, bg="#f44336", fg="white")
    btn_cikis.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    arayuzu_baslat()