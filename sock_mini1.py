import socket

target_host = "scanme.nmap.org"
target_port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Conecting to target {target_host} on port {target_port}")

    s.connect((target_host,target_port))
    print(f"[CONNECTED] Establishing connection with {target_host} on port {target_port}")
except socket.error as e:
    print(f"[ERROR] Conenction failed:{e}")
finally:
    s.close()
