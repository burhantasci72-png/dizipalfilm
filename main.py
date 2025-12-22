import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def get_current_domain():
    # Burayı senin çalışan kodunla değiştirebilirsin
    return "https://dizipal1223.com" 

def scrape_dizipal():
    base_url = get_current_domain()
    headers = {'User-Agent': 'Mozilla/5.0'}
    movies = []
    try:
        response = requests.get(base_url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Sitedeki yapıya göre burayı güncellemen gerekebilir
        items = soup.select('.video-block') or soup.select('.post-item') or soup.find_all('div', class_='articleBody')

        for item in items:
            try:
                title = item.find('h3').text.strip() if item.find('h3') else "Film Adı Yok"
                link = item.find('a')['href'] if item.find('a') else "#"
                img = item.find('img')['src'] if item.find('img') else ""
                
                movies.append({'title': title, 'link': link, 'image': img})
            except:
                continue
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
    return movies

def create_html(movies):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    html_template = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Dizipal Listesi</title>
        <style>
            body {{ background: #111; color: white; font-family: sans-serif; text-align: center; }}
            .grid {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; }}
            .card {{ width: 180px; background: #222; padding: 10px; border-radius: 10px; }}
            img {{ width: 100%; height: 250px; border-radius: 5px; object-fit: cover; }}
            a {{ color: #e50914; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Güncel Dizipal Filmleri</h1>
        <p>Son Güncelleme: {now}</p>
        <div class="grid">
    """
    if not movies:
        html_template += "<p>Şu an film çekilemedi, site adresi değişmiş olabilir.</p>"
    else:
        for movie in movies:
            html_template += f"""
                <div class="card">
                    <img src="{movie['image']}">
                    <p style="font-size:12px;">{movie['title']}</p>
                    <a href="{movie['link']}" target="_blank">İzle</a>
                </div>
            """
    html_template += "</div></body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    data = scrape_dizipal()
    create_html(data) # Boş olsa bile dosyayı oluşturur
    print("İşlem tamamlandı.")
