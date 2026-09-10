import socket

domain = "scanme.nmap.org"
target_ip = socket.gethostbyname(domain)
print(f"scan on {domain} ({target_ip})")

ports = [21,22,80,443,9999]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    try:
        s.connect((target_ip, port))
        print(f"[PORT] {port} [OPEN]")
    except socket.timeout:
        print(f"[PORT] {port} FILTERED (Timeout)")
    except socket.error:
        print(f"[PORT] {port} CLOSED")
    finally:
        s.close()           

