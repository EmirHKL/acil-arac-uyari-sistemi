# Akış Diyagramı

```mermaid
flowchart TD
  A[GNSS ile konum al] --> B[API'ye konum gönder]
  B --> C{Veri doğrulama OK?}
  C -- Hayır --> X[Hata logla / reddet]
  C -- Evet --> D[Konumu işleme al]
  D --> E[100 m mesafe hesapla (Haversine)]
  E --> F{Hedef araç var mı?}
  F -- Hayır --> Y[Logla / bekle]
  F -- Evet --> G[Uyarı bildirimi tetikle]
  G --> H[Push bildirimi gönder (Mock/Firebase/APNs)]
  H --> I[Sonuçları logla]
