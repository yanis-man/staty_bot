import os
#USED TO CHECK IF A DIR EXIST, IF NOT IT POSSIBLE TO ASK TO DO IT
def check_dir(path, do_create=False, dir_name=None):
    if not os.path.isdir(path):
        if do_create and dir_name != None:
            os.mkdir(f"{path}\+{dir_name}")
            return True
        return False
    return True

def setup_dir(server_id):
    PATH = f"{os.getcwd()}\data\{server_id}"
    check_dir(PATH, True, server_id)
    os.mkdir(f"{PATH}\charts")