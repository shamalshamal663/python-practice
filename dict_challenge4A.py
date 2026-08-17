probed_ports = [80, 22, 443, 80, 22, 22, 8080, 443]

tally_port = {}

for port in probed_ports:
    if port in tally_port:
        tally_port[port] += 1
    else:
        tally_port[port] = 1
print(tally_port)            