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
    AXIS_TICKS = 'white'
    BAR_WIDTH = .90

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

class FileConfig():

    API_KEY = "3985852a41d56dd254a96c34a5118809"
    FILE_EXTENSION = "png"
    MOH_FILENAME = "moh"
    SEVEN_DAYS_FILENAME = "seven_days"

class EmbedTitle():
    MOH_TITLE = "Messages en fonction des heures"
    SEVEN_DAYS = "Nombre de messages sur 7 jours"
    MESSAGE_PER_CHANNEL = "Répartition des messages en fonction des salons"

