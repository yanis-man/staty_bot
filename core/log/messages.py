from termcolor import colored, cprint
from modules.configs.config import MessageConfig

MSG = MessageConfig()

def load_ok_msg(module_name):
    cprint(f"{MSG.MODULE_LOADED} {module_name}", "cyan")

def load_error(module_name, err):
    cprint(f"{MSG.ERR_MODULE_LOADING} {module_name} : \n {err}", "red")

def ok_msg(ok_text):
    cprint(f"{MSG.OK} {ok_text}", 'green')

def error_msg(error_text, err):
    cprint(f"{MSG.ERR} {error_msg} : \n {err}", 'red')
