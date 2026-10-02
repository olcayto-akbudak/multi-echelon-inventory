# Tasarım kararları

## Alan motorunu CLI'dan ayırmak

`run(config)` orkestrasyonu kaynak kodun doğrudan test edilebilmesini sağlar. JSON arayüz taşınabilirliği artırır; bu sürüm kullanıcı arayüzü barındırmaz.

## Seçilen yöntem

Merkez/depo, lead time, stok pozisyonu, adil tahsis. Günlük deterministik zaman adımı ve seeded sentetik talep; satış kaybı backorder olmaz.

## Bilinçli sınır

Talep korelasyonu, kapasite kesintileri ve optimizasyon dışarıdan eklenmelidir.

## Önerilen sonraki doğrulama

Gerçek kullanım hacmiyle testten önce mevcut kabul ve ret örneklerinin alan uzmanı tarafından onaylanması gerekir. Sonraki sürüm performans ölçümleri, dış adaptör sözleşmesi ve üretim gözlemlenebilirliğini ayrı karar kayıtlarında ele almalıdır.
