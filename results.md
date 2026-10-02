# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

A: fill rate %91.71, kayıp 45; B: fill rate %90.69, kayıp 42

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_capacity` | capacity |
| `test_nonnegative` | nonnegative |
| `test_demand_conservation` | demand conservation |
| `test_seed` | seed |
| `test_lead` | lead |
| `test_duplicate_store` | duplicate store |
| `test_negative_supply` | negative supply |
| `test_supply_conservation` | supply conservation |

## Gelişmiş deney planı

1. Merkez tedarik kesintisi ve rastgele lead time ekleyin.
2. Mağaza taleplerini korelasyonlu üreterek kapasite darboğazını ölçün.
3. Base-stock politikalarını ortak random stream ile kıyaslayın.
4. Tutma, kayıp satış ve taşıma maliyetlerini hedef fonksiyonuna ekleyin.
