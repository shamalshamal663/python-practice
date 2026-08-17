threat_feed = [
    "XSS", "SQLi", "Directory Traversal", 
    "SQLi", "Command Injection", "SQLi", "XSS"
]

threat_count = {}


for threat in threat_feed:
    if threat in threat_count:
        threat_count[threat] += 1
    else:
        threat_count[threat] = 1

for threat , count in threat_count.items():
    if count >= 3:
        print(f"CRITICAL FLOOD : {threat} (total:{count})")
    else:
         print(f"Threat logged : {threat} (total:{count})")    
             