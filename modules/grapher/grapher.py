import matplotlib.pyplot as plt
import csv
import os

import modules.utils.utils as utils
from modules.configs.config import GraphConfig

def graph(server_id):

    cfg = GraphConfig()

    PATH = f"{os.getcwd()}\data\{str(server_id)}"
    server_id = str(server_id)

    utils.check_dir(server_id)

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

    plt.bar(hours, message_count, color=cfg.BAR_COLOR, alpha=cfg.BAR_ALPHA)

    plt.grid(True, linewidth=cfg.LINEWIDTH, color=cfg.GRID_COLOR, linestyle=cfg.LINESTYLE, alpha=cfg.GRID_ALPHA)

    ax = plt.axes()


    ax.set(facecolor = "grey")
    ax.patch.set_alpha(0)

    #MAKES AXIS TRANSPARENT
    axis_alpha = cfg.AXIS_ALPHA

    ax.spines['bottom'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['top'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['left'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['right'].set_color(cfg.AXIS_TXT_COLOR)

    #COLOR THE AXIS TEXT
    ax.tick_params(axis='x', colors=cfg.AXIS_TICKS)
    ax.tick_params(axis='y', colors=cfg.AXIS_TICKS)

    plt.savefig(f"{PATH}\charts\moh-1_day.png", transparent=cfg.PLOT_ALPHA, dpi=cfg.DPI)
    plt.clf()
    plt.close()
