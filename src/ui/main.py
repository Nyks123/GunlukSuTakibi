import sys
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# core klasöründeki OOP kodlarımızı dahil ediyoruz (Modüler yapı)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.models import Kullanici, SuTakipSistemi

def arayuzu_baslat():
    # Ana pencereyi oluştur
    root = tk.Tk()
    root.withdraw() # İlk baştaki boş siyah pencereyi gizle

    # Kullanıcıdan isim al
    isim = simpledialog.askstring("Giriş", "Lütfen adınızı girin:")
    if not isim: return

    # Try-Catch (Hata Yönetimi): Kullanıcı harf girerse hata mesajı verilir
    while True:
        hedef_str = simpledialog.askstring("Hedef", "Günlük su hedefinizi (ml) girin (Örn: 2500):")
        if not hedef_str: return
        try:
            hedef = int(hedef_str)
            break
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sadece sayı giriniz!")
            
    # OOP Sınıflarımızı çalıştırıyoruz
    aktif_kullanici = Kullanici(isim, hedef)
    takip_sistemi = SuTakipSistemi(aktif_kullanici)

    # Asıl uygulama penceresini aç
    ana_pencere = tk.Toplevel()
    ana_pencere.title("Günlük Su Takibi")
    ana_pencere.geometry("300x250")
    ana_pencere.configure(bg="#f0f8ff") # Açık mavi arka plan

    # İkon kuralını yerine getirmek için ikon yükleme denemesi
    try:
        ikon_yolu = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../assets/icons/icon.ico'))
        ana_pencere.iconbitmap(ikon_yolu)
    except:
        pass # Eğer ikon dosyası yoksa program çökmez, devam eder

    # Arayüz tasarımları (Etiketler ve Butonlar)
    tk.Label(ana_pencere, text=f"Hoş geldin, {isim}!", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(pady=10)
    tk.Label(ana_pencere, text=f"Günlük Hedefin: {hedef} ml", font=("Arial", 10), bg="#f0f8ff").pack()

    durum_etiketi = tk.Label(ana_pencere, text="İçilen Su: 0 ml", font=("Arial", 12, "bold"), fg="blue", bg="#f0f8ff")
    durum_etiketi.pack(pady=15)

    def su_ekle_buton_tiklandi():
        miktar_str = simpledialog.askstring("Su Ekle", "Kaç ml su içtiniz?", parent=ana_pencere)
        if miktar_str:
            try:
                miktar = int(miktar_str)
                takip_sistemi.su_ekle(miktar) # Arka plandaki asıl işlem
                durum_etiketi.config(text=f"İçilen Su: {aktif_kullanici.icilen_su} ml")
                
                # Kalanı hesapla ve bilgi ver
                kalan = aktif_kullanici.gunluk_hedef - aktif_kullanici.icilen_su
                if kalan <= 0:
                    messagebox.showinfo("Tebrikler!", "Günlük su hedefinize ulaştınız!")
                else:
                    messagebox.showinfo("Bilgi", f"Hedefe ulaşmak için {kalan} ml daha içmelisiniz.")
            except ValueError:
                messagebox.showerror("Hata", "Su miktarı sadece sayı olmalıdır!") # Hata Yönetimi

    # Su Ekleme Butonu
    btn_ekle = tk.Button(ana_pencere, text="Su İçtim Ekle (+)", command=su_ekle_buton_tiklandi, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    btn_ekle.pack(pady=5)

    # Çıkış Butonu
    btn_cikis = tk.Button(ana_pencere, text="Çıkış Yap", command=root.quit, bg="#f44336", fg="white")
    btn_cikis.pack(pady=10)

    # Pencereyi açık tut
    root.mainloop()

if __name__ == "__main__":
    arayuzu_baslat()