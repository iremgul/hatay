# hatay
# Deprem Afet Yönetim Sistemi (OOP Projesi)
**Hatay bölgesi için AI destekli çadır optimizasyon sistemi**

## Sınıf Yapısı
- `AfetZedeler`: Depremzedelerin kimlik ve sağlık bilgileri
- `Cadir`: Çadır özellikleri ve AI optimizasyon metriği
- `AfetKampYonetimi`: AI optimizasyon algoritmasını içeren yönetim sistemi

## Nasıl Çalışır?
1. Çadırlar ve depremzedeler kaydedilir
2. `optimizasyon_ai()` metodu kritik hastaları çadırlara dengeli dağıtır
3. Her çadırın `iyilestirme_oncelik` puanı AI ile güncellenir

## Kullanım
```python
hatay_kampi = AfetKampYonetimi()
hatay_kampi.cadir_olustur("C1", "Hatay-Merkez", 10)
hatay_kampi.zede_kaydet("12345678901", "Ahmet", "Yılmaz", 35, 2)
hatay_kampi.optimizasyon_ai()
