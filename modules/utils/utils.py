import os

from modules.configs.config import BotConfig
#USED TO CHECK IF A DIR EXIST, IF NOT IT POSSIBLE TO ASK TO DO IT

BotCfg = BotConfig()

def check_dir(server_id, do_create = True):
    PATH = BotCfg.data_path(server_id)

    if not os.path.isdir(PATH):
        if do_create:
            setup_dir(server_id)
            return True
        return False
    return False

def setup_dir(server_id):
    PATH = BotCfg.data_path(server_id)
    os.mkdir(server_path)
    os.mkdir(f"{PATH}/charts")
    
    f = open(f"{PATH}/ignore_cat_n_chat.csv", "w+")
    f.close()

def return_chann_object(bot, guild_id, chann_id):
    CHANN = bot.get_guild(int(guild_id)).get_channel(int(chann_id))
    return CHANN