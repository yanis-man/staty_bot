from datetime import datetime
import re

MODEL = "%d-%m-%y/%H:%M:%S"
CENTURY = 2000

def parse_limit(limit):
    duration = re.findall(r"^\d+", limit)
    types = re.findall(r"[hjma]$", limit)
    if duration and types:
        RETURN_DATE = compute_limit_date(int(duration[0]), types[0])
        return RETURN_DATE

#Date & Time substraction
def compute_limit_date(duration, types):
    today = datetime.now()
    FINAL_DATE = None

    zero_m = ""
    zero_d = ""
    if today.month < 10:
        zero_m = "0"
    if today.day < 10:
        zero_d = "0"
    if types == "h":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month}-{today.year - CENTURY}/{today.hour - duration}:{today.minute}:{today.second}", MODEL).strftime(MODEL)
    if types == "j":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day - duration}-{zero_m}{today.month}-{today.year - CENTURY}/{today.hour}:{today.minute}:{today.second}", MODEL).strftime(MODEL)
    if types == "m":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month - duration}-{today.year - CENTURY}/{today.hour}:{today.minute}:{today.second}", MODEL).strftime(MODEL)
    if types == "a":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month}-{(today.year - CENTURY) - duration}/{today.hour}:{today.minute}:{today.second}", MODEL).strftime(MODEL)
        
    return FINAL_DATE

def compare(firstDate, secondDate):
    if datetime.strptime(firstDate, MODEL).timestamp() < datetime.strptime(secondDate, MODEL).timestamp():
        #if secondDate's ts is greater than first one, then secondDate is older.
        return False