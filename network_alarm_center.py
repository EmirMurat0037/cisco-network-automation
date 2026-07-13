import json

print("Devnet Alarm Merkezi: Canlı Port Analizi Başlatılıyor...")

canli_network_verisi={
    "cihaz_id": "Sariyer-Omurga-Switch-01",
    "durum": "UP",
    "arayuzler": {
        "GigabitEthernet0/1": {"hiz": "1Gbps", "trafik_yogunlugu": 85},
        "GigabitEthernet0/2": {"hiz": "10Gbps", "trafik_yogunlugu": 12},
        "GigabitEthernet0/3": {"hiz": "1Gbps", "trafik_yogunlugu": 99},
        "GigabitEthernet0/4": {"hiz": "1Gbps", "trafik_yogunlugu": 45}
    }
}

krizdeki_portlar={}

portlar=canli_network_verisi["arayuzler"]

for port_adi, port_detaylari in portlar.items():
    yogunluk=port_detaylari["trafik_yogunlugu"]

    if yogunluk>=80:
        print(f"🚨 KRİTİK SEVİYE: {port_adi} yoğunluğu %{yogunluk}!")
        krizdeki_portlar[port_adi]=port_detaylari

print("-"*20)

if krizdeki_portlar:
    try:
        print("Sistem: 'krizdeki_portlar.json' dosyası diske mühürleniyor...")

        with open('krizdeki_portlar.json', "w", encoding="utf-8") as rapor_dosyası:

            json.dump(krizdeki_portlar, rapor_dosyası, indent=4)

        print("✅ BAŞARILI: Kriz raporu oluşturuldu!")
    
    except Exception as e:
        print(f"❌ Dosya yazılırken bir hata oluştu: {e}")

else:
    print("😎 Ağ temiz, kritik seviyede port bulunamadı.")