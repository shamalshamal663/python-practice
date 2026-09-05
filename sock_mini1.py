import socket

target_host = "scanme.nmap.org"
target_port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_host, target_port))
    print(f"[CONNECTED] TCP Handshake established with {target_host} on {target_port}")
    s.close()
    print(f"[DISCONNECTED] Socket closed cleanly")
except socket.error as e:
       print(f"[ERROR] : Given exception as {e}")

        