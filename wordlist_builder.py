import os,sys,random

base_words = ["cypher","target_corp","admin","vault","root"]
suffixes = ["!","@2026","#SEC","$123","!pass"]



def create_payload(word):
    num = random.randint(10,99)
    payload = f"{word}{num}{suffixes}"


