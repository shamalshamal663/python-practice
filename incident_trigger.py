alert_stream = [
    "CVE-2024-001", "PORT_SCAN", "CVE-2024-001", 
    "SQLI_ATTEMPT", "PORT_SCAN", "CVE-2024-001", "SSH_BRUTE"
]

threat_db = {
    "CVE-2024-001": {"title": "Auth Bypass RCE", "severity": "Critical"},
    "PORT_SCAN": {"title": "Recon Probing", "severity": "Low"},
    "SQLI_ATTEMPT": {"title": "Database Injection", "severity": "High"},
    "SSH_BRUTE": {"title": "Password Guessing", "severity": "Medium"}
}

event_count = {}

for id in alert_stream:
    if id in event_count:
        event_count[id] += 1
    else :
         event_count[id] = 1    


print("====INCIDENT TRIAGE REPORT====")
for event_id ,count in event_count.items():
    info = threat_db.get(event_id,{})
    title = info.get("title","Unknown Alert" )
    severity = info.get("severity","info")
    if severity == "Critical":
        print(f"[CRITICAL] {title} {event_id} | Total hits : {count}")
    elif severity == "High":
        print(f"[HIGH] {title} {event_id} | Total hits : {count}")
    else:
        print(f"[NORMAL] {title} {event_id} | Total hits : {count}")