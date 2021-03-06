import csv
from datetime import datetime, timedelta
import os
import  modules.utils.utils as Utils
from modules.configs.config import BotConfig

def register_message(server_id, author_id, channel_id):

    BotCfg = BotConfig()
    PATH = BotCfg.data_path(server_id)

    Utils.check_dir(server_id)

    csv_file = open(f"{PATH}/messages.csv", "a", newline="", encoding="utf-8")
    
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([(author_id), (channel_id), ( ( datetime.today() + timedelta(hours=2) ).strftime('%d-%m-%y/%H:%M:%S') ) ])

    csv_file.close()
