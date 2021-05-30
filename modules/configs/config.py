import os

class BotConfig():
    TOKEN = os.getenv("BOT_TOKEN")
    PREFIX = "%"
    REPORT_HOUR = 0
    REPORT_TEST_INTERVAL = 1.0

    def data_path(server_id):
        server_id = str(server_id)
        PATH = f"{os.getcwd()}/data/{server_id}"
        return

class GraphConfig():
    #GENERAL
    PLOT_ALPHA = True
    DPI = 300
    LINESTYLE = "-"
    LINEWIDTH = .5
    AXIS_TICKS = 'none'
    BAR_WIDTH = .90

    #ALPHA
    AXIS_ALPHA = 1
    BAR_ALPHA = 1
    GRID_ALPHA = .5

    #COLOR
    GRID_COLOR = "#698474"
    BAR_COLOR = "#698474"
    AXIS_TXT_COLOR = "none"

class MessageConfig():

    OK = "[OK]"
    LOAD = "[LOAD]"
    ERR = "[ERR]"

    #GENERAL
    MODULE_LOADED = f" OK :"
    
    #ERRORS
    PERMS_ERROR = "tu vas où mon reuf?"
    WRONG_CHAN = "t'es khabat ? jpeux pas parler ici"
    ERR_MODULE_LOADING = f" Could not load :"

class FileConfig():

    API_KEY = "3985852a41d56dd254a96c34a5118809"
    API_URL = "https://api.imgbb.com/1/upload"
    FILE_EXTENSION = "jpg"

    MOH_FILENAME = "moh"
    UPH_FILENAME = "uph"
    SEVEN_DAYS_FILENAME = "seven_days"

class EmbedTitle():
    MOH_TITLE = "Messages par heures"
    UPH_TITLE = "Utilisateurs par heures"

    SEVEN_DAYS = "Nombre de messages sur 7 jours"
    MESSAGE_PER_CHANNEL = "Répartition des messages en fonction des salons"

class Help():
    MPH_HELP = "Permet d'afficher le nombre de message par heures ex: %mph 2j"
    UPH_HELP = "Permet d'afficher le nombre d'utilisateur par heures ex: %uph 2j"
