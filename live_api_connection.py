import requests

print("🌐 DevNet REST API Operasyonu: Canlı Cihaz Bağlantısı Kuruluyor...\n")

api_adresi="https://jsonplaceholder.typicode.com/todos/1"

try:
    print(F"Sistem: {api_adresi} adresine GET isteği gönderiliyor...")

    cevap = requests.get(api_adresi, verify=False)

    if cevap.status_code==200:
        gelen_json_veri = cevap.json()

        print("📊 Cihazdan Gelen Canlı Veri Paketi:")
        print("-"*20)
        print(gelen_json_veri)
        print("-"*20)
    else:
        print(f"⚠️ Cihaz hata döndürdü! HTTP Durum Kodu: {cevap.status_code}")

except Exception as e:
    print(f"❌ Fiziksel Bağlantı Hatası! Cihaza ulaşılamıyor: {e}")