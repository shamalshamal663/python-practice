failed_ips = [
    "192.168.1.5", "10.0.0.1", "192.168.1.5", 
    "172.16.0.4", "192.168.1.5", "10.0.0.1"
]


ip_count = {} 

for ip in failed_ips:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
         ip_count[ip] = 1 
print(ip_count)            