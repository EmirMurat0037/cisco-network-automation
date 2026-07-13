import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("🔐 DevNet Güvenlik Merkezi: Kimlik Doğrulamalı API Çağrısı...\n")

api_adresi="https://jsonplaceholder.typicode.com/todos/1"

gofret_kutusu={
    "Authorization":"Bearer GIZLI_DEVNET_TOKEN_ABC123XYZ", 
    "Content-Type": "application/json",                   
    "X-API-KEY": "sariyer_yazilim_ekibi_ozel_anahtar"
}

try:
    print("Sistem: Güvenlik anahtarları HTTP paketinin kafasına (Header) mühürleniyor...")

    cevap= requests.get(api_adresi, headers=gofret_kutusu, verify=False)

    match cevap.status_code:
        case 200:
            print("Başarılı")
            print(f"Gelen veri:{cevap.json()['title']}")
        case 401:
            print("YETKİSİZ GİRİŞ")
        case _:
            print(f"HATA {cevap.status_code}")

except Exception as e:
    print("Cihaza ulaşılamıyor")

