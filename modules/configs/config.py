import os

class BotConfig():
    TOKEN = os.getenv("BOT_TOKEN")
    PREFIX = "%"

class GraphConfig():
    #GENERAL
    PLOT_ALPHA = True
    DPI = 700
    LINESTYLE = "-"
    LINEWIDTH = .5
    AXIS_TICKS = 'none'

    #ALPHA
    AXIS_ALPHA = 1.0
    BAR_ALPHA = .7
    GRID_ALPHA = .2

    #COLOR
    GRID_COLOR = "royalblue"
    BAR_COLOR = "royalblue"
    AXIS_TXT_COLOR = "white"

class MessageConfig():
    OK = None
    LOAD = None 
    ERR = None
    def __init__(self):
        #PREFIX
        OK = "[OK]"
        LOAD = "[LOAD]"
        ERR = "[ERR]"

    #GENERAL
    MODULE_LOADED = f"{LOAD} Load OK :"
    
    #ERRORS
    PERMS_ERROR = "tu vas où mon reuf?"
    WRONG_CHAN = "t'es khabat ? jpeux pas parler ici"
    ERR_MODULE_LOADING = f"{ERR} Could not load :"
