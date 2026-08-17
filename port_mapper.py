import time

print(" CHECKING!.... ")
time.sleep(2)


port_lookup = {
    "21": "FTP (Unencrypted)",
    "22": "SSH (Remote Shell)",
    "80": "HTTP (Web Traffic)",
    "3389": "RDP (Remote Desktop)"
}


def identify_services(input_file):
    with open(input_file,"r") as file:
        for line in file:
           port = line.strip()
           if port in port_lookup:
               service = port_lookup[port]
               print(f"port{port} identified as : {service}")
           else :
               print(f"port {port} - unknown service")    
                     


identify_services("scan_result.txt")