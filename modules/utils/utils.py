import os
#USED TO CHECK IF A DIR EXIST, IF NOT IT POSSIBLE TO ASK TO DO IT

PATH = f"{os.getcwd()}\data\\"

def check_dir(server_id, do_create = True):
    if not os.path.isdir(PATH+f"{server_id}"):
        if do_create:
            setup_dir(server_id)
            return True
        return False
    return False

def setup_dir(server_id):
    server_path = PATH+f"{server_id}"
    os.mkdir(server_path)
    os.mkdir(f"{server_path}\charts")

def return_chann_object(bot, guild_id, chann_id):
    NAME = bot.get_guild(int(guild_id)).get_channel(int(chann_id))
    return NAME