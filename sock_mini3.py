import socket

domain = "scanme.nmap.org"
target_ip = socket.gethostbyname(domain)
print(f"Resolved {domain} to the ip : {target_ip}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

try:
    s.settimeout(3.0)
    s.connect((target_ip, 80))

    probe = f"GET / HTTP/1.1\r\nHost: {domain}\r\n\r\n"

    s.send(probe.encode())

    raw_banner = s.recv(1024)
    print(f"Banner recieved \n {raw_banner.decode().strip()}")
except socket.timeout:
    print(f"[TIMEOUT] : Unable to connect to the domain timeout")
except socket.error as e:
    print(f"[ERROR] : Generall socket exeption {e}")
finally:
    s.close()
    print(f"Socket teardown complete")    

        


    


