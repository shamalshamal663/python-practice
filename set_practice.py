raw_endpoints = [
    "/admin", "/login", "/users", "/admin", 
    "/dashboard", "/users", "/api/v1", "/login"
]


approved_routes = {"/login", "/users", "/dashboard"}



unique_endpoint = set(raw_endpoints)
length = len(unique_endpoint)
print(f"Total unique endpoints found {length}")

unauthorized_port = unique_endpoint - approved_routes
for route in unauthorized_port:
    print(f"ALERT: Unapproved endpoint exposed:{route}")
