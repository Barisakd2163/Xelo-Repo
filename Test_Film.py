import cloudscraper
try:
    from bs4 import BeautifulSoup
except ImportError:
    import os
    os.system('pip install beautifulsoup4')
    from bs4 import BeautifulSoup

def search_dizibox(query):
    scraper = cloudscraper.create_scraper()
    # Dizibox'un güncel adresi
    url = f"https://www.dizibox.live/?s={query}"
    
    print(f"\n[DiziBox] {url} adresinde '{query}' aranıyor...\n")
    try:
        response = scraper.get(url, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # DiziBox.kt dosyasındaki aynı seçici (article.detailed-article)
        results = soup.select("article.detailed-article")
        if not results:
            print("Sonuç bulunamadı veya Cloudflare engeline takıldı.")
            return

        print("--- BULUNAN SONUÇLAR ---")
        for idx, result in enumerate(results, 1):
            title = result.select_first("h3 a")
            if title:
                print(f"{idx}. {title.text}")
                print(f"   Link: {title['href']}")
            
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    aranacak = input("Test etmek için bir dizi/film adı yazın (örn: Breaking Bad): ")
    search_dizibox(aranacak)
    input('\nÇıkmak için Enter a basın...')
