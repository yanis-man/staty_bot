from discord.ext import commands
from discord.utils import get, find
import discord
import csv
from datetime import datetime

import modules.tools.messages as tools


class MessageEvents(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        tools.register_message(ctx.guild.id, ctx.author.id, ctx.channel.id)
        


def setup(bot):
    bot.add_cog(MessageEvents(bot))