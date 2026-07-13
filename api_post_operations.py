import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("🚀 DevNet POST Operasyonu: Cihaza Yeni Yapılandırma Gönderiliyor...\n")

api_adresi = "https://jsonplaceholder.typicode.com/todos"

yeni_ag_gorevi = {
    "title": "Sariyer-Omurga-Switch Port 5 Kapatılacak",
    "completed": False,
    "userId": 99
}

try:
    print("Sistem: JSON paketi hazırlanıyor ve POST isteği fırlatılıyor...")
    cevap=requests.post(api_adresi, json=yeni_ag_gorevi, verify=False)

    print(f"📊 Cihazdan Dönen HTTP Kodu: {cevap.status_code}")

    match cevap.status_code:
        case 201:
            print("🟢 DURUM: BAŞARILI! Yeni yapılandırma cihazda başarıyla YARATILDI (201).")
            print("\n📥 Cihazın Kabul Edip Mühürlediği Yeni Veri:")
            print("--------------------------------------------------")
            print(cevap.json())
            print("--------------------------------------------------")
        case 400:
            print("🚨 DURUM: HATA! Gönderilen JSON paketinin formatı bozuk (400).")
        case 401 | 403:
            print("🔒 DURUM: YETKİ HATASI! Bu yapılandırmayı yapmaya rütbeniz yetmiyor.")
        case _:
            print(f"❓ DURUM: Beklenmeyen bir kod alındı: {cevap.status_code}")

except Exception as e:
    print(f"❌ Cihaza fiziksel erişim sağlanamadı: {e}")
