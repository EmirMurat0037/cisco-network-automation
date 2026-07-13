import json
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def tek_cihaz_pingle(cihaz):
    su_an=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ip=cihaz['ip_adresi']
    isim=cihaz['cihaz_adi']

    print(f"🚀 [İşçi Başladı] -> {isim} ({ip}) taranıyor...")

    sonuc= subprocess.call(["ping","-n","1", ip], stdout=subprocess.DEVNULL)

    if sonuc==0:
        print(f"🟢 [UP] {isim} tamamlandı.")
        return f"[{su_an}] [UP] {isim} ({ip}) - Stabil.\n"
    else:
        print(f"🔴 [DOWN] {isim} cevap vermedi!")
        return f"[{su_an}] [DOWN] CRITICAL - {isim} ({ip}) ULAŞILAMIYOR!\n"

def sistemi_paralel_calistir():
    print("⚡ DevNet Multi-Threading Otomasyonu Başlatıldı...\n")

    try:
        with open("cihazlar.json", "r", encoding="utf-8") as dosya:
            cihazlar=json.load(dosya)
    except Exception as e:
        print(f"❌ Envanter dosyası yüklenemedi: {e}")
        return
    baslangic_zamani=datetime.now()

    print(f"Sistem: {len(cihazlar)} cihaz için 3'lü işçi kuruluyor...\n")

    with ThreadPoolExecutor(max_workers=3) as havuz:
        rapor_satirlari = list(havuz.map(tek_cihaz_pingle, cihazlar))

    try:
        with open("canli_ag_raporlari.txt", "a", encoding="utf-8") as rapor:
            rapor.write(f"\n==== Paralel Tarama Seansı: {baslangic_zamani.strftime('%d-%m-%Y %H:%M:%S')} ====\n")
            for satir in rapor_satirlari:
                rapor.write(satir)
    except Exception as e:
        print(f"Hata günlüğe yazılamadı: {e}")

    bitis_zamani=datetime.now()
    toplam_sure=(bitis_zamani - baslangic_zamani).total_seconds()
    print(f"\n✅ BAŞARILI: Tüm ağ {toplam_sure} saniyede tarandı ve loglandı!")

sistemi_paralel_calistir()