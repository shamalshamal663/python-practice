findings = {"SQLi": 3, "XSS": 2}

metadata = {
    "SQLi": {"severity": "Critical", "cvss": 9.8},
    "XSS": {"severity": "Medium", "cvss": 6.1}
}

for vuln,count in findings.items():
    info = metadata.get(vuln,{})
    severity = info.get("severity")
    cvss = info.get("cvss")
    if severity == "Critical":
        print(f"CRITICAL:{vuln} (found:{count}) -CVSS:{cvss}")
    else:
        print(f"INFO:{vuln} (found:{count}) -CVSS:{cvss}")
             
             