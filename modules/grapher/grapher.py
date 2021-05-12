import matplotlib.pyplot as plt
import csv
import os

import modules.utils.utils as utils
from modules.configs.config import GraphConfig

def bar_plot(server_id,filename, data_on_x = None, data_on_y = None):
    
    if (data_on_x or data_on_y) is None: 
        return False
    PATH = f"{os.getcwd()}/data/{server_id}"
    cfg = GraphConfig()

    

    plt.bar(data_on_x, data_on_y, color=cfg.BAR_COLOR, alpha=cfg.BAR_ALPHA, width=cfg.BAR_WIDTH)

    plt.grid(True, linewidth=cfg.LINEWIDTH, color=cfg.GRID_COLOR, linestyle=cfg.LINESTYLE, alpha=cfg.GRID_ALPHA)

    ax = plt.axes()

    ax.set(facecolor = "grey")
    ax.patch.set_alpha(0)

    #MAKES AXIS TRANSPARENT
    axis_alpha = cfg.AXIS_ALPHA

    #ax.set_xticklabels(hours_on_x, color="white")

    ax.spines['bottom'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['top'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['left'].set_color(cfg.AXIS_TXT_COLOR)
    ax.spines['right'].set_color(cfg.AXIS_TXT_COLOR)

    #COLOR THE AXIS TEXT

    ax.tick_params(axis='x', colors=cfg.AXIS_TICKS)
    ax.tick_params(axis='y', colors=cfg.AXIS_TICKS)

    plt.savefig(f"{PATH}/charts/{filename}.jpg", transparent=cfg.PLOT_ALPHA, dpi=cfg.DPI)
    plt.close()
