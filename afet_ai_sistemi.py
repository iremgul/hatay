class AfetZedeler:
    def __init__(self, tc_kimlik, ad, soyad, yas, saglik_durumu):
        self.tc_kimlik = tc_kimlik
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.saglik_durumu = saglik_duriku  # 1-5 arası (5=kritik)

class Cadir:
    def __init__(self, cadir_id, konum, kapasite):
        self.cadir_id = cadir_id
        self.konum = konum
        self.kapasite = kapasite
        self.doluluk = 0
        self.zedeler = []
        self.iyilestirme_oncelik = 0  # AI için optimizasyon metriği

    def zede_ekle(self, zede):
        if self.doluluk < self.kapasite:
            self.zedeler.append(zede)
            self.doluluk += 1
            self.iyilestirme_oncelik_hesapla()
            return True
        return False

    def iyilestirme_oncelik_hesapla(self):
        # AI OPTIMIZASYONU: Kritik hasta sayısına göre öncelik belirleme
        kritik_sayisi = sum(1 for z in self.zedeler if z.saglik_durumu >= 4)
        self.iyilestirme_oncelik = kritik_sayisi / self.kapasite * 100

class AfetKampYonetimi:
    def __init__(self):
        self.cadirler = {}
        self.zede_kayit = {}

    def cadir_olustur(self, cadir_id, konum, kapasite):
        self.cadirler[cadir_id] = Cadir(cadir_id, konum, kapasite)

    def zede_kaydet(self, tc, ad, soyad, yas, saglik):
        yeni_zede = AfetZedeler(tc, ad, soyad, yas, saglik)
        self.zede_kayit[tc] = yeni_zede
        return yeni_zede

    def optimizasyon_ai(self):
        """AI DESTEKLİ YERLEŞİM ALGORİTMASI"""
        # Kritik hastaları eşit dağıtma algoritması
        tum_kritikler = [z for z in self.zede_kayit.values() if z.saglik_durumu >= 4]
        
        for z in tum_kritikler:
            en_uygun_cadir = min(
                self.cadirler.values(),
                key=lambda c: (c.iyilestirme_oncelik, -c.kapasite + c.doluluk)
            )
            en_uygun_cadir.zede_ekle(z)

# Örnek Kullanım
if __name__ == "__main__":
    # Kamp kurulumu
    hatay_kampi = AfetKampYonetimi()
    hatay_kampi.cadir_olustur("C1", "Hatay-Merkez", 10)
    hatay_kampi.cadir_olustur("C2", "Hatay-Samandağ", 8)
    
    # Zede kayıtları (gerçek uygulamada veritabanından gelir)
    hatay_kampi.zede_kaydet("12345678901", "Ahmet", "Yılmaz", 35, 2)
    hatay_kampi.zede_kaydet("23456789012", "Ayşe", "Kaya", 67, 5)  # Kritik hasta
    
    # AI optimizasyonu çalıştırma
    hatay_kampi.optimizasyon_ai()
    
    # Sonuçları görüntüleme
    for cadir_id, cadir in hatay_kampi.cadirler.items():
        print(f"{cadir_id} Numaralı Çadır:")
        print(f"  Öncelik Puanı: %{cadir.iyilestirme_oncelik:.1f}")
        print(f"  Yerleşen: {cadir.doluluk}/{cadir.kapasite}")
