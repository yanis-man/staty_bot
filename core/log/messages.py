from termcolor import colored, cprint

def load_ok_msg(module_name):
    cprint(f"[LOAD] {module_name} correctly loaded", "cyan")

def ok_msg(ok_text):
    cprint(f"[OK] {ok_text}", 'green')

def error_msg(error_text):
    cprint(f"[ERR] {error_msg}", 'red')
