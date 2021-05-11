from discord.ext import tasks, commands
import discord
import asyncio
import csv
import os

from modules.viewers.graph_viewer import generate_embed
from modules.configs.config import EmbedTitle, FileConfig, Help
from modules.grapher.data_manager import get_moh_data, get_uph_data
from modules.grapher.grapher import bar_plot
from modules.tools.date_modifier import parse_limit
from modules.utils.utils import return_chann_object


EmbedCfg = EmbedTitle()
FileCfg = FileConfig()
HelpCfg = Help()


class StatsReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.daily_report.start()

    def cog_unload(self):
        self.daily_report.cancel()

    @tasks.loop(hours=10)
    async def daily_report(self):
        csv_file = open(f"{os.getcwd()}\\data\\guilds_info.csv", "r", newline="", encoding="utf-8")
        csv_reader = csv.reader(csv_file)
        for l in csv_reader:

            GUILD_ID = int(l[0])
            GUILD = self.bot.get_guild(GUILD_ID)
            DEST_CHANNEL = return_chann_object(self.bot, GUILD_ID, int(l[1]))
            LIMIT = "1j"

            moh_data = get_moh_data(GUILD_ID, LIMIT)
            bar_plot(GUILD_ID, FileCfg.MOH_FILENAME, moh_data[0], moh_data[1])

            uph_data = get_uph_data(GUILD_ID, LIMIT)
            bar_plot(GUILD_ID, FileCfg.UPH_FILENAME, uph_data[0], uph_data[1])

            await DEST_CHANNEL.send(embed=generate_embed(f"{EmbedCfg.UPH_TITLE}", f"Depuis le {parse_limit(LIMIT)}", GUILD_ID, LIMIT, FileCfg.UPH_FILENAME))

            await DEST_CHANNEL.send(embed=generate_embed(f"{EmbedCfg.MOH_TITLE}", f"Depuis le {parse_limit(LIMIT)}", GUILD_ID, LIMIT, FileCfg.MOH_FILENAME))
    
    @daily_report.before_loop
    async def before(self):
        print("Waiting for bot to start")
        await self.bot.wait_until_ready()
def setup(bot):
    bot.add_cog(StatsReport(bot))