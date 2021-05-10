import os
import csv

from modules.tools.date_modifier import parse_limit, first_less_second, first_more_second
import modules.utils.utils as utils

def get_moh_data(server_id, limit):

    server_id = str(server_id)
    LIMIT = parse_limit(limit)
    PATH = f"{os.getcwd()}\data\{server_id}"

    utils.check_dir(server_id)

    csv_file = open(f"{PATH}\messages.csv", "r", newline="", encoding="utf-8")
    csv_reader = csv.reader(csv_file)

    data = {}
    for line in csv_reader:
        if first_less_second(line[2], LIMIT):
            pass
        if first_more_second(line[2], LIMIT):
            hour = line[2].split("/")[1].split(":")[0] + "h"
            if hour not in data: data[hour] = 0 
            data[hour] += 1

    hours_on_x = []
    message_count = []
    hours_on_x[:]= data.keys()
    message_count[:]= data.values()

    proper_data = [hours_on_x, message_count]
    return proper_data

def get_uph_data(server_id, limit="1j"):

    server_id = str(server_id)
    LIMIT = parse_limit(limit)
    PATH = f"{os.getcwd()}\data\{server_id}"

    utils.check_dir(server_id)

    csv_file = open(f"{PATH}\messages.csv", "r", newline="", encoding="utf-8")
    csv_reader = csv.reader(csv_file)

    data = {}
    for line in csv_reader:
        if first_less_second(line[2], LIMIT):
            pass
        if first_more_second(line[2], LIMIT):
            hour = line[2].split("/")[1].split(":")[0] + "h"
            if hour not in data: data[hour] = [] 
            if line[0] not in data[hour]: data[hour].append(line[0])

    hours_on_x = []
    author_count = []
    hours_on_x[:]= data.keys()
    for hour in data:
        author_count.append(len(data[hour]))

    proper_data = [hours_on_x, author_count]
    return proper_data