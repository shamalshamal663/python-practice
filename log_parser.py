import time


print("validating logs!")
time.sleep(2)



def filter_alert(log_list):
    alert = []
    for log in  log_list:
        if "CRITICAL" in log or "WARNING" in log:
            alert.append(log)
    return alert
            
        
raw_logs = [
    "INFO: User admin logged in",
    "WARNING: Failed login attempt on Port 22",
    "INFO: System update complete",
    "CRITICAL: Unauthorized access detected!"
]

flagged_alerts = filter_alert(raw_logs)
print(flagged_alerts)
    