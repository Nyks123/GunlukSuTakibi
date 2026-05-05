import json
import os

# Hocanın istediği 'data/' klasörünün yolunu buluyoruz
DOSYA_YOLU = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/veri.json'))

class Kisi:
    def __init__(self, isim):
        self.__isim = isim 
    def get_isim(self):
        return self.__isim

class Kullanici(Kisi):
    def __init__(self, isim, gunluk_hedef):
        super().__init__(isim)
        self.gunluk_hedef = gunluk_hedef
        self.icilen_su = 0
        self.verileri_yukle() # Program açıldığında eski verileri yükle

    # JSON Okuma Fonksiyonu
    def verileri_yukle(self):
        if os.path.exists(DOSYA_YOLU):
            with open(DOSYA_YOLU, 'r', encoding='utf-8') as dosya:
                veri = json.load(dosya)
                if veri.get("isim") == self.get_isim():
                    self.gunluk_hedef = veri.get("hedef", self.gunluk_hedef)
                    self.icilen_su = veri.get("icilen", 0)

    # JSON Yazma Fonksiyonu
    def verileri_kaydet(self):
        veri = {
            "isim": self.get_isim(),
            "hedef": self.gunluk_hedef,
            "icilen": self.icilen_su
        }
        with open(DOSYA_YOLU, 'w', encoding='utf-8') as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=4)

    def durum_bilgisi(self):
        return f"{self.get_isim()} isimli kullanici oluşturuldu."

class SuTakipSistemi:
    def __init__(self, kullanici):
        self.kullanici = kullanici
        
    def su_ekle(self, miktar):
        self.kullanici.icilen_su += miktar
        self.kullanici.verileri_kaydet() # Su eklenince anında JSON'a kaydet!
        
    def kalan_hedef_hesapla(self):
        return self.kullanici.gunluk_hedef - self.kullanici.icilen_su