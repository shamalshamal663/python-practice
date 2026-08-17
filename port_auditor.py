import time

print("auditing port ... !")
time.sleep(2)

dangerous_port = ["21","22","3389"]


def audit_port_from_file(input_file,output_file):
    with open(input_file,"r") as file:
        for line in file:
            port = line.strip()
            if port in dangerous_port:
                with open(output_file,"a") as out_file:
                    out_file.write(f"CRITICAL RISK : port {port} exposed!\n")

audit_port_from_file("open_port.txt","flagged_port.txt")

