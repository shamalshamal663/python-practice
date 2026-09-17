import time, sys , socket

if len(sys.argv) < 2 :
    print(f"Usage : python{sys.argv[0]} <target_domain_or_ip>")
    sys.exit()

target = sys.argv[1]

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"DNS resolution failed for {target}")
    sys.exit()

print(f"[INITIATING SCAN] Target locked:{target} ({target_ip})")

ports_to_scan = [21, 22, 23, 25, 53, 110, 80, 139, 443, 445,3389, 8080]

start_time = time.time()

for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    s.close()   


elapsed = round(time.time()-start_time, 2)
print(f"[COMPLETED] Scan finished in {elapsed} seconds.")
