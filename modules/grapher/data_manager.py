import os
import csv

from modules.tools.date_modifier import parse_limit, compare
import modules.utils.utils as utils
def get_data(server_id, limit="1j"):

    server_id = str(server_id)
    LIMIT = parse_limit(limit)
    PATH = f"{os.getcwd()}\data\{server_id}"

    utils.check_dir(server_id)

    csv_file = open(f"{PATH}\messages.csv", "r", newline="", encoding="utf-8")
    csv_reader = csv.reader(csv_file)

    hours_c = {}
    h = []
    
    for line in csv_reader:
        if compare(line[2], LIMIT) == False:
            break
        hours = line[2].split("/")[1].split(":")[0] + "h"
        if hours not in hours_c: hours_c[hours] = 0 
        hours_c[hours] += 1
    
    csv_file.close()
    hours = []
    message_count = []    
    message_count[:] = hours_c.values()
    hours[:] = hours_c.keys()
    return [hours, message_count]