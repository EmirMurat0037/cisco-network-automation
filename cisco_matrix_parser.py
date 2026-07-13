import json

print("Holding Altyapı Analizi Başlatılıyor")

try:
    with open("altyapi.json", "r", encoding="utf-8") as dosya:
        holding_alt_yapisi = json.load(dosya)
    print("Altyapı devreye girdi.")
except Exception as e:
    print(f"Envanter okunamadı!!! {e}")
    exit()

print("Çözümleme başlıyor")
print("="*20)

kriz_alt_yapisi={}

for lokasyon_adi, lokasyon_detay in holding_alt_yapisi["topoloji"].items():
    for cihaz in lokasyon_detay["cihazlar"]:
        cihaz_adi=cihaz["isim"]
        cihaz_rolu=cihaz["rol"]

        if cihaz_rolu in ["Core", "Distribution"]:
            if "portlar" not in cihaz:
                print(f"⚠️ UYARI: {cihaz_adi} cihazının port bilgisi eksik! Pas geçiliyor.")
                continue
            else:
                for port_adi, port_ozellikleri in cihaz["portlar"].items():
                    durum=port_ozellikleri["status"]
                    vlan=port_ozellikleri["vlan"]
                    hata_sayisi=port_ozellikleri["error_count"]

                    if durum == "DOWN" and vlan < 100:
                        print(f"🚨 KRİTİK ALARM [{lokasyon_adi}] -> {cihaz_adi} ({cihaz_rolu})")
                        print(f"   ↳ Port: {port_adi} | Durum: {durum} | VLAN: {vlan} | Hata Paketi: {hata_sayisi}\n")

                        if lokasyon_adi not in kriz_alt_yapisi:
                            kriz_alt_yapisi[lokasyon_adi]=[]

                        kriz_alt_yapisi[lokasyon_adi].append({
                            "cihaz":cihaz_adi,
                            "port":port_adi,
                            "vlan":vlan,
                            "hata":hata_sayisi
                    })

print("="*20)

try:
    with open("holding_kriz_matrisi.json", "w", encoding="utf-8") as f:
        json.dump(kriz_alt_yapisi,f,indent=4,ensure_ascii=False)
    print("✅ OPERASYON BAŞARILI: 'holding_kriz_matrisi.json' dosyası güncellendi!")
except Exception as e:
    print(f"❌ Matris dosyası yazılamadı: {e}")