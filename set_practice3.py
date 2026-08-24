baseline_ports = {80, 443, 22, 21, 8080}

current_ports = {80, 443, 22, 3389, 9000}

drifted_port = baseline_ports ^ current_ports

for port in drifted_port:
    print(f"STATE CHANGE:Port {port} changed status between scans")

baseline_ports.add(9000)
baseline_ports.discard(21)

length = len(baseline_ports)

print(f"Updated baseline port count:{length}")
