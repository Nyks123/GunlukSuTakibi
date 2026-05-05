import sys
import os

# core klasöründeki kodlarımızı bu dosyaya dahil ediyoruz (Modüler yapı kuralı)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.models import Kullanici, SuTakipSistemi

def arayuzu_baslat():
    print("=== Günlük Su Takibi Uygulamasına Hoş Geldiniz ===")
    isim = input("Lütfen adınızı girin: ")
    
    # Try-Catch (Hata Yönetimi): Kullanıcı harf girerse program çökmez
    while True:
        try:
            hedef = int(input("Günlük su hedefinizi (ml) olarak girin (Örn: 2500): "))
            break # Doğru girilirse döngüden çık
        except ValueError:
            print("Hata: Lütfen sadece sayı giriniz!")
            
    # Sınıflarımızı (nesnelerimizi) çalıştırıyoruz
    aktif_kullanici = Kullanici(isim, hedef)
    takip_sistemi = SuTakipSistemi(aktif_kullanici)
    
    # Ana menü döngüsü
    while True:
        print("\n1. Su İçtim Ekle")
        print("2. Kalan Hedefimi Gör")
        print("3. Çıkış")
        
        secim = input("Seçiminiz (1/2/3): ")
        
        if secim == '1':
            try:
                miktar = int(input("Kaç ml su içtiniz? : "))
                takip_sistemi.su_ekle(miktar)
            except ValueError:
                # Kullanıcı hatalarına karşı kontrol kuralı
                print("Hata: Su miktarı sayı olmalıdır! Lütfen tekrar deneyin.") 
        elif secim == '2':
            takip_sistemi.kalan_hedef_hesapla()
        elif secim == '3':
            print("Sağlıklı günler dileriz! Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    arayuzu_baslat()