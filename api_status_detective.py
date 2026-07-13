import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("DevNet Durum kodu analiz merkezi başlatıldı...\n")

test_senaryolari={
    "Başarılı Port İsteği": "https://jsonplaceholder.typicode.com/todos/1",
    "Yanlış API Adresi (404 Testi)": "https://jsonplaceholder.typicode.com/bu-adres-cihazda-yok",
    "Yetkisiz Erişim (401/403 Testi)": "https://httpbin.org/status/401"
}

for senaryo_adi, url in test_senaryolari.items():
    print(f"\nSenaryo {senaryo_adi} başlatılıyor")

    try:
        cevap=requests.get(url, verify=False)
        kod=cevap.status_code

        print(f"Cihazda dönen HTTP kodu:{kod}")
        match kod:
            case 200:
                print("🟢 Durum: Mükemmel! Cihaz veriyi teslim etti.")
            case 401 | 403:  # Tek satırda "Veya" (OR) mantığı! Çok havalı.
                print("🚨 Durum: KRİTİK! Yetki hatası. Şifre veya Token geçersiz!")
            case 404:
                print("🟡 Durum: UYARI! İstediğiniz port veya servis cihazda mevcut değil.")
            case _ if kod >= 500:  # Case içinde özel şart (Guard) yazımı
                print("💥 Durum: FELAKET! Ağ cihazı çöktü veya servis dışı.")
            case _:  # Switch-case dünyasındaki "default" yani yukarıdakilerin hiçbiri uymazsa
                print(f"❓ Durum: Tanımlanamayan kod: {kod}")

    except Exception as e:
        print(f"❌ Cihaza fiziksel olarak ulaşılamadı: {e}")

print("\n--------------------------------------------------")
print("✅ Tüm senaryolar analiz edildi. Operasyon başarılı!")