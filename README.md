# 🎬 Dizipal Film Arşivi Botu

Otomatik olarak film bilgilerini çeken ve modern bir HTML arayüzü ile sunan GitHub Pages tabanlı film arşivi.

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/USERNAME/REPO/update-films.yml?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/USERNAME/REPO?style=for-the-badge)
![Films Count](https://img.shields.io/badge/Films-500+-blue?style=for-the-badge)

## ✨ Özellikler

- 🤖 **Otomatik Güncelleme**: Her gün otomatik olarak yeni filmler eklenir
- 🎨 **Modern Arayüz**: Responsive ve kullanıcı dostu tasarım
- 🔍 **Gelişmiş Arama**: Film adı ve türe göre arama
- 🎭 **Tür Filtreleme**: Kategorilere göre film filtreleme
- ⭐ **IMDB Puanları**: Film puanlarını görüntüleme
- 📱 **Mobil Uyumlu**: Tüm cihazlarda mükemmel çalışır
- 🚀 **Hızlı Yükleme**: Lazy loading ile optimize edilmiş

## 🚀 Kurulum

### 1. Repository'yi Fork Edin

Sağ üstteki "Fork" butonuna tıklayarak kendi hesabınıza kopyalayın.

### 2. GitHub Pages'i Aktif Edin

1. Repository ayarlarına gidin (Settings)
2. Sol menüden "Pages" seçeneğini seçin
3. Source olarak "GitHub Actions" seçin
4. Kaydedin

### 3. (Opsiyonel) URL'yi Özelleştirin

Farklı bir Dizipal adresi kullanmak isterseniz:

1. Repository Settings → Secrets and variables → Actions
2. "New repository secret" butonuna tıklayın
3. Name: `DIZIPAL_URL`
4. Secret: `https://yeni-dizipal-adresi.com/filmler`
5. Add secret

### 4. Manuel Güncelleme

- Actions sekmesine gidin
- "Film Güncelleme Botu" workflow'unu seçin
- "Run workflow" butonuna tıklayın

## 📁 Proje Yapısı

```
dizipal-film-bot/
├── .github/
│   └── workflows/
│       └── update-films.yml      # GitHub Actions workflow
├── dizipal_scraper.py             # Ana scraper script
├── index.html                     # Oluşturulan film sitesi
├── films.json                     # Film verileri (JSON)
├── requirements.txt               # Python bağımlılıkları
└── README.md                      # Bu dosya
```

## 🛠️ Yerel Kullanım

### Gereksinimler

```bash
pip install -r requirements.txt
```

### Çalıştırma

```bash
python dizipal_scraper.py
```

Varsayılan olarak `index.html` dosyası oluşturulur.

### Özelleştirme

Ortam değişkenleri ile özelleştirebilirsiniz:

```bash
# Farklı URL kullan
export DIZIPAL_URL="https://dizipal-yeni-adres.com/filmler"

# Maksimum film sayısını değiştir
export MAX_FILMS=1000

# Çıktı dosyasını değiştir
export OUTPUT_PATH="filmler.html"

python dizipal_scraper.py
```

## 🎨 Arayüz Özellikleri

### Ana Ekran
- Modern gradient arka plan
- Film kartları grid düzeni
- Hover efektleri
- IMDB puanları

### Arama ve Filtreleme
- Gerçek zamanlı arama
- Tür bazlı filtreleme
- Kombine filtreler

### Film Detayları
- Modal pencerede detaylı bilgi
- IMDB puanı, yıl, süre
- Film özeti
- Direkt izleme linki

## 📊 Güncelleme Sıklığı

- **Otomatik**: Her gün saat 03:00 (UTC)
- **Manuel**: Actions sekmesinden istediğiniz zaman
- **Push ile**: main branch'e her push'ta

## 🔧 Yapılandırma

### GitHub Secrets

| Secret | Açıklama | Zorunlu |
|--------|----------|---------|
| `DIZIPAL_URL` | Dizipal film sayfası URL'si | Hayır |

### Environment Variables

| Değişken | Varsayılan | Açıklama |
|----------|-----------|----------|
| `DIZIPAL_URL` | `https://dizipal1223.com/filmler` | Kaynak URL |
| `MAX_FILMS` | `500` | Maksimum film sayısı |
| `OUTPUT_PATH` | `index.html` | Çıktı dosyası adı |

## 🐛 Sorun Giderme

### Filmler Güncellenmiyor

1. Actions sekmesini kontrol edin
2. Son workflow çalışmasını inceleyin
3. Hata mesajlarını okuyun

### Site Açılmıyor

1. GitHub Pages ayarlarını kontrol edin
2. `index.html` dosyasının oluştuğunu doğrulayın
3. Birkaç dakika bekleyin (deployment süresi)

### URL Değişti

1. Repository Settings → Secrets
2. `DIZIPAL_URL` secret'ını güncelleyin
3. Workflow'u manuel çalıştırın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## ⚠️ Yasal Uyarı

Bu bot yalnızca eğitim amaçlıdır. Web scraping yaparken:
- Sitenin robots.txt dosyasına uyun
- Rate limiting uygulayın
- Telif haklarına saygı gösterin
- Sorumlu kullanın

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing`)
5. Pull Request açın

## 📞 İletişim

Sorularınız için issue açabilirsiniz.

## 🌟 Yıldız Vermeyi Unutmayın!

Bu projeyi beğendiyseniz ⭐ vermeyi unutmayın!

---

**Not**: Site adresi değişirse `DIZIPAL_URL` secret'ını güncellemeyi unutmayın.
