# Gereksinim Senaryoları

## RS-1: Takip Cihazından Konum Verisi Alımı
**Özet:** Acil durum aracındaki takip cihazı GNSS ile konumu belirler ve mobil veri ile sunucuya iletir.  
**Ön Koşullar:** Takip cihazı aktif, SIM/internet bağlantısı var, cihaz sunucu endpoint bilgisine sahip.  
**Akış:**
1. Takip cihazı lat/lon üretir.
2. Sunucuya JSON formatında konum isteği gönderilir.
3. Sunucu isteği doğrular ve işlemeye alır.
**Başarı Kriteri:** İletim sürekliliği %95+ (test süresince).

## RS-2: 100 Metre Menzil Tespiti
**Özet:** Sunucu, acil durum aracının konumuna göre 100 m içindeki araçları hesaplar.  
**Ön Koşullar:** Kayıtlı araç konumları sisteme alınmış durumda.  
**Akış:**
1. Sunucu mesafe hesaplama algoritmasını çalıştırır (ör. Haversine).
2. 100 m içinde kalan hedefler seçilir.
**Başarı Kriteri:** Menzil içi hedef tespit doğruluğu %80+.

## RS-3: Bildirim Tetikleme
**Özet:** Hedef sürücülere “Acil durum aracı yaklaşıyor, yolu açın” bildirimi gönderilir.  
**Ön Koşullar:** Hedef kullanıcıların bildirim token’ları kayıtlı (gerçek sistemde).  
**Akış:**
1. Sunucu hedef listesini çıkarır.
2. Bildirim modülünü tetikler (Mock/Firebase/APNs).
3. Sonuçlar kayıt altına alınır.
**Başarı Kriteri:** Bildirim gecikmesi ortalama < 2 sn.

## RS-4: Loglama ve İzlenebilirlik
**Özet:** Kritik süreç adımları loglanır (konum alındı, hedef sayısı, bildirim durumu).  
**Başarı Kriteri:** Her isteğin log kaydı oluşması ve hedef sayısının raporlanabilmesi.
