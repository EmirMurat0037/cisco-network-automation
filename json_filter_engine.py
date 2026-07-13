cisco_output = {
    "ietf-interfaces:interfaces": {
        "interface": [
            {"name": "GigabitEthernet1", "status": "UP", "ip": "10.0.1.1"},    # ✅ Hem UP, hem 10. ile başlıyor -> GEÇER
            {"name": "GigabitEthernet2", "status": "UP"},                     # 🚨 IP yok -> Senin mantıkla NONE olacak ve GEÇER
            {"name": "GigabitEthernet3", "status": "UP", "ip": "192.168.1.1"},# ❌ UP ama 10. ile başlamıyor -> ELENİR
            {"name": "Loopback0", "status": "UP", "ip": "10.255.255.254"}     # ✅ Hem UP, hem 10. ile başlıyor -> GEÇER
        ]
    }
}

interfaces_list = cisco_output["ietf-interfaces:interfaces"]["interface"]

print("Filetring Interfaces (Status: UP | IP: 10.x.x.x or None)")

for interface in interfaces_list:
    if interface["status"] == "UP":
        current_ip = interface.get("ip")

        if current_ip is None:
            print(f"Match found -> Name:{interface['name']} | Status : UP | IP:None")
        
        elif current_ip.startswith("10."):
            print(f"Match found -> Name:{interface['name']} | Status : UP | IP:{current_ip}")