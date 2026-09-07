import socket

target_host = "10.255.255.1"
target_port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.settimeout(3.0)
    print(f"probing {target_host}:{target_port} with timeout of 3s")

    s.connect((target_host,target_port))
    print(f"[SUCCESS] Port open !")

except socket.timeout:
    print(f"[TIMEOUT] Host {target_host} dropped the connection or it's offline")

except socket.error as e:
    print(f"[ERROR] General socket error : {e}") 

finally:
    s.close()
    print("socket probing complete")           






