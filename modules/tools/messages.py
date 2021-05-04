import csv
from datetime import datetime
import os
import  tools.utils.utils as utils

def register_message(server_id, author_id, channel_id):

    server_id = str(server_id)
    PATH = f"{os.getcwd()}\data\{server_id}"

    if not utils.check_dir(PATH, False, None):
        utils.setup_dir(server_id)

    utils.check_dir(PATH, True, server_id)

    csv_file = open(f"{PATH}\messages.csv", "a", newline="", encoding="utf-8")
    
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([(author_id), (channel_id), (datetime.today().strftime('%d-%m-%y/%H:%M:%S'))])

    csv_file.close()
