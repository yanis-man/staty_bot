import matplotlib.pyplot as plt
import csv
import os

import modules.utils.utils as utils
from modules.configs.config import GraphConfig
from modules.grapher.data_manager import get_data

def graph(server_id, limit, filename):
    PATH = f"{os.getcwd()}\data\{server_id}"
    cfg = GraphConfig()

    proper_data = get_data(server_id, limit)

    plt.bar(proper_data[0], proper_data[1], color=cfg.BAR_COLOR, alpha=cfg.BAR_ALPHA, width=cfg.BAR_WIDTH)

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
    plt.xticks([r + cfg.BAR_WIDTH for r in range(len(proper_data[1]))],
        proper_data[0])
    plt.yticks([r for r in range(len(proper_data[1]))],
        proper_data[1])

    ax.tick_params(axis='x', colors=cfg.AXIS_TICKS)
    ax.tick_params(axis='y', colors=cfg.AXIS_TICKS)

    plt.savefig(f"{PATH}\charts\{filename}.png", transparent=cfg.PLOT_ALPHA, dpi=cfg.DPI)
    plt.clf()
    plt.close()
