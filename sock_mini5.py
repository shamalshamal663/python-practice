import socket

domain ="scanme.nmap.org"
target_ip = socket.gethostbyname(domain)
print(f"Starting banner grab scan on {domain} ({target_ip})")

ports = [21, 22, 80]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    try :
        s.connect((target_ip, port))
        if port == 80:
            s.send(f"HEAD / HTTP/1.1\r\nHost: {domain}\r\n\r\n".encode())
        raw_data = s.recv(1024)
        banner = raw_data.decode().strip()
        print(f"[PORT] {port} OPEN | Banner {banner.splitlines()[0]}")
    except socket.timeout:
        print(f"[PORT {port}] OPEN | No banner returned /timeout")
    except socket.error:
        print(f"[PORT :{port}] CLOSED")
    finally:
        s.close()
      

    

            