# Sınıf 1: Ana Sınıf (Kişi)
class Kisi:
    def __init__(self, isim):
        # Kapsülleme (Encapsulation): İsim değişkeni dışarıdan doğrudan değiştirilemez
        self.__isim = isim 
    
    # Kapsüllenen veriyi okumak için Getter metodu
    def get_isim(self):
        return self.__isim

# Sınıf 2: Kalıtım Alan Sınıf (Kullanici)
# Kalıtım (Inheritance): Kullanici sınıfı, Kisi sınıfının özelliklerini miras alıyor
class Kullanici(Kisi):
    def __init__(self, isim, gunluk_hedef):
        super().__init__(isim) # Üst sınıfın isim özelliğini çalıştırır
        self.gunluk_hedef = gunluk_hedef
        self.icilen_su = 0
    
    # Çok Biçimlilik (Polymorphism) için temel metod
    def durum_bilgisi(self):
        return f"{self.get_isim()} isimli kullanici oluşturuldu."

# Sınıf 3: İş Mantığı Sınıfı (SuTakipSistemi)
class SuTakipSistemi:
    def __init__(self, kullanici):
        self.kullanici = kullanici
        
    def su_ekle(self, miktar):
        self.kullanici.icilen_su += miktar
        print(f"\nHarika! {miktar} ml su eklendi.")
        
    def kalan_hedef_hesapla(self):
        kalan = self.kullanici.gunluk_hedef - self.kullanici.icilen_su
        if kalan <= 0:
            print("\nTebrikler! Günlük su hedefinize ulaştınız!")
        else:
            print(f"\nGünlük hedefinize ulaşmak için {kalan} ml daha su içmelisiniz.")