# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `days` | `int` | 90 |
| `lead_time` | `int` | 4 |
| `daily_supply` | `int` | 12 |
| `daily_capacity` | `int` | 18 |
| `central_stock` | `int` | 50 |
| `stores` | `list` | [{'id': 'A', 'initial': 20, 'base_stock': 30, 'max_demand': 12}, {'id': 'B', 'initial': 15, 'base_stock': 25, 'max_demand': 10}] |

## Semantik

Günlük deterministik zaman adımı ve seeded sentetik talep; satış kaybı backorder olmaz.

Alan motorunun doğrulamaları `app.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
