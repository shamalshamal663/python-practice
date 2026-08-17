###goal###
#iterate over dictionary of target service and their 
# port number to print to a formatted port audit

open_port = {"SSH" : "22" , "HTTP" : "80", "HTTPS":"443"}


for service,port in open_port.items():
    print(f"port : {port}---> service : {service}")

