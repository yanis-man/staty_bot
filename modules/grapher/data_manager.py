import os
import csv

from modules.tools.date_modifier import parse_limit, first_less_second, first_more_second
import modules.utils.utils as utils

def get_moh_data(server_id, limit):

    server_id = str(server_id)
    LIMIT = parse_limit(limit)

    utils.check_dir(server_id)

    PATH = f"{os.getcwd()}/data/{server_id}"

    csv_file = open(f"{PATH}/messages.csv", "r", newline="", encoding="utf-8")
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

    PATH = f"{os.getcwd()}/data/{server_id}"

    utils.check_dir(server_id)

    csv_file = open(f"{PATH}/messages.csv", "r", newline="", encoding="utf-8")
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

def get_message_stat_data(bot, server_id, limit="1j"):
    PATH = f"{os.getcwd()}/data/{server_id}"
    LIMIT = parse_limit(limit)
    channel_msg_count = {}
    channel_msg_percentage = {}
    total = 0
    top_5_channel = "Rien à signaler"

        #check if the file is empty

    csv_file = open(f"{PATH}/messages.csv", "r", newline="", encoding="utf-8")
    csv_reader = csv.reader(csv_file)

    if os.stat(f"{PATH}/messages.csv").st_size != 0:
        #count message in each channel
        for line in csv_reader:
            if line is None: pass
            if first_less_second(line[2], LIMIT):
                pass
            if first_more_second(line[2], LIMIT):
                CHANN_NAME = utils.return_chann_object(bot, server_id, int(line[1])).name
                if CHANN_NAME not in channel_msg_count: channel_msg_count[CHANN_NAME] = 0  #ICI
                channel_msg_count[CHANN_NAME] += 1
                total += 1

            #compute % of each channel activity
        for elem in channel_msg_count:
            channel_msg_percentage[elem] = round(channel_msg_count[elem] / total * 100, 2)

            #order by greatest to lowest
        sorted_tuple_message_percentage = sorted(channel_msg_percentage.items() ,  key=lambda x: x[1], reverse=True)

            #as we display top 5 channel, if when the request come the 'channel_msg_percentage' contain less than 5 it will send an error
        print(channel_msg_count)
        if len(sorted_tuple_message_percentage) < 5 and len(sorted_tuple_message_percentage) > 0:
            top_5_channel = " " 
            for sorted_items in range(0, len(sorted_tuple_message_percentage)): 
                top_5_channel += f"{sorted_tuple_message_percentage[sorted_items][0]} : {sorted_tuple_message_percentage[sorted_items][1]} % `{int(sorted_tuple_message_percentage[sorted_items][1] * total / 100)} messages`/n"
        else:
            top_5_channel = " "
            for sorted_items in range(0,5):
                top_5_channel += f"{sorted_tuple_message_percentage[sorted_items][0]} : {sorted_tuple_message_percentage[sorted_items][1]} % ({int(sorted_tuple_message_percentage[sorted_items][1] * total / 100)} messages)/n"

    return [top_5_channel, total]

        