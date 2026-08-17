import time


print ("validating")
time.sleep(2)


def audit_password(password):
        
         if len(password) < 8:
            return "WEAK : password is to short"
         elif len(password) >= 8 and len(password) < 12:
            return "MODERATE : Good length,but can be stronger. "
         else:
            return "STRONG : Excellent password length! "

result1 = audit_password ("12345")
result2 = audit_password("cypher2026")
result3 = audit_password("superSecureCyberPassword123")       
            
        
print("----password audit result-----")
print(result1)
print(result2)
print(result3)