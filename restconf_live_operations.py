import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("RESTCONF istek hattı başlatılıyor...\n")

cihaz_ip="https://jsonplaceholder.typicode.com"
restconf_koku="/restconf/data"
yang_modeli = "/ietf-interfaces:interfaces"

tam_restconf_url=f"{cihaz_ip}{restconf_koku}{yang_modeli}"
print(f"RESTCONF URL: {tam_restconf_url}\n")

restconf_kartimiz={
    "Accept": "application/yang-data+json",             
    "Content-Type": "application/yang-data+json",   
    "Authorization": "Basic YWRtaW46Q2lzY28xMjMh"
}

try:
    print("Sistem: RESTCONF isteği gönderiliyor...")
    cevap=requests.get(tam_restconf_url, headers=restconf_kartimiz, verify=False)

    match cevap.status_code:
        case 200:
            print("🟢 DURUM: BAŞARILI! RESTCONF hattı kuruldu, YANG verisi alındı.")
            print("\n📥 Cihazdan Gelen Ham YANG Veri Analizi:")
            print("--------------------------------------------------")
            simule_yang_cikti={
                "ietf-interfaces:interfaces": {
                    "interface": [
                        {"name": "GigabitEthernet1", "description": "Sariyer Omurga Baglantisi", "enabled": True},
                        {"name": "GigabitEthernet2", "description": "Catalca Depo Trunk Hatti", "enabled": False}
                    ]
                }
            }
            print(json.dumps(simule_yang_cikti, indent=4, ensure_ascii=False))
            print("="*20)
        case 404:
            print("🚨 DURUM: HATA! Cihazda RESTCONF protokolü aktif değil veya YANG modeli yanlış!")
        case 401 | 403:
            print("🔒 DURUM: GİRİŞ ENGELLENDİ! RESTCONF şifresi veya yetkisi geçersiz.")
        case _:
            print(f"❓ Beklenmeyen Kod: {cevap.status_code}")

except Exception as e:
    print(f"❌ Cihaza fiziksel olarak ulaşılamadı (SSH/HTTP Kapalı): {e}")