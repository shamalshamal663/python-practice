import socket

service_db = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP"
}

domain = "scanme.nmap.org"
target_ip = socket.gethostbyname(domain)

open_ports = []

print(f"[INITIATING RECON] scaniing {domain} on {target_ip}")

for port in service_db:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    try :
        s.connect((target_ip, port))
        service = service_db.get(port, "services")
        print(f"[PORT {port} OPEN({service})]")
        open_ports.append(port)
    except (socket.timeout,socket.error):
        pass   
    finally:
        s.close()

print(f"----SCANNING SUMMARY----")
print(f"Total open port discovered {len(open_ports)}")
print(f"Discovered open port list {open_ports}")                    
