 status_codes = [200, 404, 200, 500, 404, 200, 403, 404, 200]

status_count = {}


for code in status_codes:
    if code in status_count:
        status_count[code] += 1
    else:
        status_count[code] = 1

for code ,count in status_count.items():
    print(f"[HTTP {code}] count:{count}")



