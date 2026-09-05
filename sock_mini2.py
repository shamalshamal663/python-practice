import socket

target_host = "10.255.255.1"
target_port = 80

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    s.settimeout(2.0)
    print(f"Probbing {target_host}:{target_port} (timeout = 2s)")

    s.connect((target_host,target_port))
    print(f"Port Open !")
except socket.timeout:
    print(f"[TIMEOUT] Host {target_host} dropped the connection or it's offline")
except socket.error as e:
    print(f"[ERROR] Genearal socket erro: {e}")
finally:
    s.close()
    print(f"socket teardown complete")
       
    

