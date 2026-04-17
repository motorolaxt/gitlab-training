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
        print(f"Odpověď od {host}: Wazup")
    else:
        print(f"Odpověď od {host}: Na této IP se žádný počítač ne-e")

# Seznam IP adres k testování
ips = ["8.8.8.8", "1.1.1.1", "0.0.0.0", "666.666.666.666"]

print("get ready for FUBAR in 3.. 2.. 1..")
for ip in ips:
    ping_host(ip)
