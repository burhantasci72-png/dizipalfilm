name: Film Güncelleme Botu

on:
  schedule:
    # Her gün saat 03:00'te çalışır (UTC)
    - cron: '0 3 * * *'
  workflow_dispatch:  # Manuel tetikleme seçeneği
  push:
    branches:
      - main

jobs:
  update-films:
    runs-on: ubuntu-latest
    
    steps:
    - name: 📥 Repository'yi çek
      uses: actions/checkout@v4
      
    - name: 🐍 Python kurulumu
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
        
    - name: 📦 Bağımlılıkları yükle
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4 lxml
        
    - name: 🎬 Filmleri çek ve HTML oluştur
      env:
        DIZIPAL_URL: ${{ secrets.DIZIPAL_URL || 'https://dizipal1223.com/filmler' }}
        MAX_FILMS: 500
        OUTPUT_PATH: index.html
      run: |
        python dizipal_scraper.py
        
    - name: 📊 İstatistikleri göster
      run: |
        echo "📈 Oluşturulan dosyalar:"
        ls -lh index.html 2>/dev/null || echo "index.html bulunamadı"
        ls -lh *.json 2>/dev/null || echo "JSON dosyası bulunamadı"
        
    - name: 💾 Değişiklikleri kaydet
      run: |
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git add -A
        git diff --quiet && git diff --staged --quiet || (git commit -m "🎬 Film listesi güncellendi - $(date +'%Y-%m-%d %H:%M:%S')" && git push)
        
    - name: 📤 GitHub Pages için deploy
      uses: actions/upload-pages-artifact@v3
      with:
        path: '.'
        
  deploy:
    needs: update-films
    runs-on: ubuntu-latest
    
    permissions:
      pages: write
      id-token: write
      
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
      
    steps:
    - name: 🚀 GitHub Pages'e deploy
      id: deployment
      uses: actions/deploy-pages@v4
