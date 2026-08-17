import time

print("Scanning ports ")
time.sleep(2)

allowed_port = [80,443,8080]
incoming_port = [80,22,443,21,8080,3389]

def evaluate_firewall(traffic_list):
    for port in traffic_list:
        if port not in allowed_port:
            print(f"BLOCKED:Unauthorized traffic detected on port {port}")
        else:
            print(f"ALLOWED: Port {port} traffic approved")


evaluate_firewall(incoming_port)
                

