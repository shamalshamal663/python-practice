import time 

print("creating!...")
time.sleep(2)

def daily_report_generator(input_file,report_file):
    error_count = 0
    with open(input_file,"r") as file:
        for line in file:
            if "ERROR" in line :
                error_count += 1
                with open(report_file,"w") as out_file:
                    out_file.write("===SYSTEM AUDITING===\n")
                    out_file.write(f"ERROR COUNT {error_count}\n")

daily_report_generator("server.log","daily_report.txt")                    