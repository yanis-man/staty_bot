from datetime import datetime, timedelta
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
    today = datetime.now() + timedelta(hours=2)
    FINAL_DATE = None

    zero_m = ""
    zero_d = ""
    if today.month < 10:
        zero_m = "0"
    if today.day < 10:
        zero_d = "0"
    if types == "h":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month}-{today.year - CENTURY}/{today.hour - duration}:0:0", MODEL).strftime(MODEL)
    if types == "j":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day - duration}-{zero_m}{today.month}-{today.year - CENTURY}/00:0:0", MODEL).strftime(MODEL)
    if types == "m":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month - duration}-{today.year - CENTURY}/00:0:0", MODEL).strftime(MODEL)
    if types == "a":
        FINAL_DATE = datetime.strptime(f"{zero_d}{today.day}-{zero_m}{today.month}-{(today.year - CENTURY) - duration}/00:0:0", MODEL).strftime(MODEL)
        
    return FINAL_DATE

def first_less_second(firstDate, secondDate):
    if datetime.strptime(firstDate, MODEL).timestamp() < datetime.strptime(secondDate, MODEL).timestamp():
        #if firstDate's ts is less than secondDate's one, then firstDate is older than secondDate
        return True
    else:
        return False

def first_more_second(firstDate, secondDate):
    if datetime.strptime(firstDate, MODEL).timestamp() >= datetime.strptime(secondDate, MODEL).timestamp():
        #if firstDate's ts is less than secondDate's one, then firstDate is older than secondDate
        return True
    else:
        return False
