from discord.ext import commands
from discord.utils import get, find
import discord
import csv
from datetime import datetime

import modules.tools.messages as tools


class StatsReport(commands.Cog):
    def __init(self, bot):
        self.bot = bot

        


def setup(bot):
    bot.add_cog(StatsReport(bot))