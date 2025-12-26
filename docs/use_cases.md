# Use Case’ler

## UC-1: Konum Gönderimi
**Aktör:** Araç Takip Cihazı  
**Amaç:** Acil aracın konumunu sunucuya iletmek  
**Ön Koşullar:** Cihaz aktif, internet var  
**Ana Akış:** Konum alınır → API’ye gönderilir → doğrulanır  
**Çıktı:** Sunucu konumu işler ve hedef tespiti başlatır

## UC-2: 100 m İçindeki Araçları Tespit Etme
**Aktör:** Sunucu  
**Amaç:** 100 m içindeki araçları belirlemek  
**Ön Koşullar:** Acil araç konumu ve kayıtlı araç konumları mevcut  
**Ana Akış:** Mesafe hesaplanır → hedefler seçilir  
**Çıktı:** Hedef araç listesi oluşur

## UC-3: Uyarı Bildirimi Gönderme
**Aktör:** Bildirim Servisi (Mock/Firebase/APNs)  
**Amaç:** Hedef sürücülere uyarı iletmek  
**Ön Koşullar:** Kullanıcı token bilgisi mevcut (gerçek sistemde)  
**Ana Akış:** Bildirim tetiklenir → sonuç loglanır  
**Çıktı:** Bildirim gönderimi tamamlanır

## UC-4: Performans Ölçümü ve Raporlama
**Aktör:** Test Ekibi  
**Amaç:** Gecikme, doğruluk ve kararlılığı değerlendirmek  
**Ana Akış:** Test sürüşü → metrik toplama → analiz  
**Çıktı:** Performans raporu (gecikme, hedef doğruluğu, stabilite)
