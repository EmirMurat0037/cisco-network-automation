import json
import subprocess
from datetime import datetime

def envanteri_yukle(dosya_yolu="cihazlar.json"):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        print(f"❌ HATA: '{dosya_yolu}' dosyası bulunamadı!")
        return[]
    except json.JSONDecodeError:
        return[]
    
def cihaz_pingle(ip_adresi):
    donen_kod=subprocess.call(["ping", "-n", "1", ip_adresi], stdout=subprocess.DEVNULL)
    return[]

def sistemi_calistir():
    print("Sistem: Profesyonel Ağ Otomasyonu Başlatıldı...\n")
    
    cihazlar = envanteri_yukle("cihazlar.json")
    
    if not cihazlar:
        print("Sistem: Taranacak geçerli bir cihaz bulunamadığından çıkış yapılıyor.")
        return

    with open("canli_ag_raporu.txt", "a", encoding="utf-8") as rapor:
        
        for cihaz in cihazlar:
            su_an = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Kontrol Ediliyor: {cihaz['cihaz_adi']} ({cihaz['ip_adresi']})")
            
            donen_kod = subprocess.call(["ping", "-n", "1", cihaz['ip_adresi']], stdout=subprocess.DEVNULL)
            print(f"DEBUG -> İşletim sisteminden gelen ham ping kodu: {donen_kod}")
            
            ayakta_mi = (donen_kod == 0)
            
            if ayakta_mi:
                rapor.write(f"[{su_an}] [UP] {cihaz['cihaz_adi']} ({cihaz['ip_adresi']}) - Stabil.\n")
                print("Durum: [UP] 🟢")
            else:
                rapor.write(f"[{su_an}] [DOWN] CRITICAL - {cihaz['cihaz_adi']} ({cihaz['ip_adresi']}) ULAŞILAMIYOR!\n")
                print("Durum: [DOWN] 🔴")
                
            print("-" * 30)

    print("\n[BAŞARILI] Tarama döngüsü tamamlandı.")

sistemi_calistir()