import matplotlib.pyplot as plt
import csv
import os
import modules.utils.utils as utils
from modules.configs.config_parser import getGraphConfig

def graph(server_id):

    CONFIG = getGraphConfig()

    PATH = f"{os.getcwd()}\data\{str(server_id)}"
    server_id = str(server_id)

    utils.check_dir(PATH, True, "charts")

    csv_file = open(f"{PATH}\messages.csv", "r", newline="", encoding="utf-8")
    csv_reader = csv.reader(csv_file)

    hours_c = {}
    h = []

    for line in csv_reader:
        hours = line[2].split("/")[1].split(":")[0] + "h"
        if hours not in hours_c: hours_c[hours] = 0 
        hours_c[hours] += 1
    
    csv_file.close()
    hours = []
    message_count = []    
    message_count[:] = hours_c.values()
    hours[:] = hours_c.keys()

    plt.bar(hours, message_count, color=CONFIG['color']['bar_color'], alpha=CONFIG['alpha']['bar_alpha'])

    plt.grid(True, linewidth=CONFIG['general']['linewidth'], color=CONFIG['color']['grid_color'], linestyle=CONFIG['general']['linestyle'], alpha=CONFIG['alpha']['grid_alpha'])

    ax = plt.axes()


    ax.set(facecolor = "grey")
    ax.patch.set_alpha(0)

    #REMOVE TICKS FROM AXIS
    axis_ticks = CONFIG['general']['axis_tick_p']

    ax.xaxis.set_ticks_position(axis_ticks) 
    ax.yaxis.set_ticks_position(axis_ticks) 

    #MAKES AXIS TRANSPARENT
    axis_alpha = CONFIG['alpha']['axis_alpha']

    ax.spines['bottom'].set_alpha(axis_alpha)
    ax.spines['top'].set_alpha(axis_alpha)
    ax.spines['left'].set_alpha(axis_alpha)
    ax.spines['right'].set_alpha(axis_alpha)
    ax.xaxis.label.set_color('white')

    #COLOR THE AXIS TEXT
    ax.tick_params(axis='x', colors=CONFIG['color']['axis_text_color'])
    ax.tick_params(axis='y', colors=CONFIG['color']['axis_text_color'])

    utils.check_dir(f"{PATH}\charts", True, "charts")

    plt.savefig(f"{PATH}\charts\moh-1_day.png", transparent=CONFIG['general']['plot_alpha'], dpi=CONFIG['general']['dpi'])
    plt.clf()
    plt.close()
