waf_alerts = {"192.168.1.10", "10.0.0.50", "172.16.0.4", "192.168.1.99"}

nids_alerts = {"10.0.0.50", "192.168.1.99", "10.0.0.77", "172.16.0.88"}

confirmed_ip = waf_alerts & nids_alerts
for ip in confirmed_ip:
    print(f"HIGH PRIORITY:{ip} (flagged by both waf_alert and nids_alert)")

unique_ip = waf_alerts | nids_alerts
print(f"Total unique ip added to global block list:{len(unique_ip)}")