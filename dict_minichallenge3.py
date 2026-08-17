system_users = {
    "alice": "user",
    "bob": "admin",
    "charlie": "guest",
    "cypher": "admin"
}



for user , role in system_users.items():
    if role == "admin":
        print(f"ADMIN FOUND:{user} ")
    else:
        print(f"STANDARD USER : {user} ({role})")    