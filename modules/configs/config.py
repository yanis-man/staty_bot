import configparser as CP
from enum import Enum

class BotConfig():
    TOKEN = "Nzk5OTkxMDYzODc1Mjg5MTA4.YALnvA.RvbsaSFvsv3UoLUwgNU711yYrQg"
    PREFIX = "%"

class GraphConfig():
    #GENERAL
    PLOT_ALPHA = True
    DPI = 300
    LINESTYLE = "-"
    LINEWIDTH = .5
    AXIS_TICKS = "none"

    #ALPHA
    AXIS_ALPHA = 0
    BAR_ALPHA = .7
    GRID_ALPHA = .2

    #COLOR
    GRID_COLOR = "royalblue"
    BAR_COLOR = "royalblue"
    AXIS_TXT_COLOR = "white"

class MessageConfig():
    #GENERAL

    #ERROR
    PERMS_ERROR = "tu vas où mon reuf?"
    WRONG_CHAN = "t'es khabat ? jpeux pas parler ici"