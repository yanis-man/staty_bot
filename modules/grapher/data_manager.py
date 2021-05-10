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

    data = {}
    for line in csv_reader:
        hour = line[2].split("/")[1].split(":")[0] + "h"
        if hour not in data: data[hour] = 0 
        data[hour] += 1

    hours_on_x = []
    message_count = []
    hours_on_x[:]= data.keys()
    message_count[:]= data.values()

    proper_data = [hours_on_x, message_count]
    return proper_data