import subprocess
import platform

def ping_host(host):
    # Určení parametru podle operačního systému (-n pro Windows, -c pro Unix)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Sestavení příkazu: pošle 1 paket
    command = ['ping', param, '1', host]
    
    # Spuštění příkazu a zachycení výsledku
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print(f"Odpověď od {host}: OK")
    else:
        print(f"Odpověď od {host}: CHYBA (Hostitel je nedostupný)")

# Seznam IP adres k testování
ips = ["8.8.8.8", "1.1.1.1"]

print("Spouštím test připojení...")
for ip in ips:
    ping_host(ip)
