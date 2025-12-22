import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# 1. GÜNCEL DOMAIN BULUCU (Dizipal adresleri sürekli değiştiği için)
def get_current_domain():
    # Burası senin orijinal kodundaki domain bulma mantığıyla değiştirilebilir
    # Örnek: Genelde dizipal araması yaparak veya sabit bir yönlendiriciden çekilir.
    # Şimdilik manuel bir başlangıç noktası veriyoruz.
    return "https://dizipal738.com" # Burayı botun bulduğu güncel adrese bağlayabilirsin.

def scrape_dizipal():
    base_url = get_current_domain()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    movies = []
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Orijinal kodundaki kart yapısına göre burayı düzenleyebilirsin
        # Standart Dizipal kart yapısı genelde 'video-block' veya 'post-item' içindedir.
        items = soup.find_all('div', class_='video-block') or soup.select('.post-item')

        for item in items:
            title = item.find('a').get('title') or item.find('h3').text.strip()
            link = item.find('a').get('href')
            if not link.startswith('http'):
                link = base_url + link
            
            img = item.find('img').get('data-src') or item.find('img').get('src')
            
            movies.append({
                'title': title,
                'link': link,
                'image': img
            })
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    return movies

def create_html(movies):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dizipal Güncel Filmler</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background-color: #0f0f0f; color: #fff; margin: 0; padding: 20px; }}
            h1 {{ text-align: center; color: #e50914; }}
            .update-time {{ text-align: center; color: #aaa; font-size: 0.9em; margin-bottom: 30px; }}
            .movie-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }}
            .movie-card {{ background: #1f1f1f; border-radius: 10px; overflow: hidden; transition: transform 0.3s; border: 1px solid #333; }}
            .movie-card:hover {{ transform: scale(1.05); border-color: #e50914; }}
            .movie-card img {{ width: 100%; height: 260px; object-fit: cover; }}
            .movie-info {{ padding: 10px; text-align: center; }}
            .movie-info h3 {{ font-size: 0.9em; margin: 10px 0; height: 40px; overflow: hidden; }}
            .btn-watch {{ display: inline-block; background: #e50914; color: #fff; padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 0.8em; }}
        </style>
    </head>
    <body>
        <h1>Dizipal Güncel Liste</h1>
        <p class="update-time">Son Güncelleme: {now}</p>
        <div class="movie-grid">
    """

    for movie in movies:
        html_template += f"""
            <div class="movie-card">
                <img src="{movie['image']}" alt="{movie['title']}">
                <div class="movie-info">
                    <h3>{movie['title']}</h3>
                    <a href="{movie['link']}" target="_blank" class="btn-watch">Şimdi İzle</a>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    movie_data = scrape_dizipal()
    if movie_data:
        create_html(movie_data)
        print("Bütün detaylar işlendi, index.html hazırlandı.")
