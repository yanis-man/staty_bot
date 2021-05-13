from discord.ext import tasks, commands
import discord
import asyncio
import csv
import os
from datetime import datetime

from modules.viewers.graph_viewer import generate_embed, generate_msg_stats_embed
from modules.configs.config import EmbedTitle, FileConfig, BotConfig
from modules.grapher.data_manager import get_moh_data, get_uph_data, get_message_stat_data
from modules.grapher.grapher import bar_plot
from modules.tools.date_modifier import parse_limit
from modules.utils.utils import return_chann_object


EmbedCfg = EmbedTitle()
FileCfg = FileConfig()
BotCfg = BotConfig()

class StatsReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.daily_report.start()

    def cog_unload(self):
        self.daily_report.cancel()

    @tasks.loop(minutes=1.0)
    async def daily_report(self):
        if str(datetime.now().hour) == BotCfg.REPORT_HOUR:
            csv_file = open(f"{os.getcwd()}/data/guilds_info.csv", "r", newline="", encoding="utf-8")
            csv_reader = csv.reader(csv_file)
            for l in csv_reader:
            
                #Useful variables
                GUILD_ID = int(l[0])
                GUILD = self.bot.get_guild(GUILD_ID)
                DEST_CHANNEL = return_chann_object(self.bot, GUILD_ID, int(l[1]))
                LIMIT = "1j"

                #Message over hours plot
                moh_data = get_moh_data(GUILD_ID, LIMIT)
                bar_plot(GUILD_ID, FileCfg.MOH_FILENAME, moh_data[0], moh_data[1])
            
                #Users per hours plot
                uph_data = get_uph_data(GUILD_ID, LIMIT)
                bar_plot(GUILD_ID, FileCfg.UPH_FILENAME, uph_data[0], uph_data[1])

                #Messages statistics
                DATA = get_message_stat_data(self.bot, GUILD_ID, LIMIT)

                await DEST_CHANNEL.send(embed=generate_msg_stats_embed(["Répartition des messages"], [DATA[0]], DATA[1]))
                await DEST_CHANNEL.send(embed=generate_embed(f"{EmbedCfg.MOH_TITLE}", f"Depuis le {parse_limit(LIMIT)}", GUILD_ID, LIMIT, FileCfg.MOH_FILENAME))
                await DEST_CHANNEL.send(embed=generate_embed(f"{EmbedCfg.UPH_TITLE}", f"Depuis le {parse_limit(LIMIT)}", GUILD_ID, LIMIT, FileCfg.UPH_FILENAME))
    
    @daily_report.before_loop
    async def before(self):
        print("Waiting for bot to start")
        await self.bot.wait_until_ready()
def setup(bot):
    bot.add_cog(StatsReport(bot))
