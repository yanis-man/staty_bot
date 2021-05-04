from discord.ext import commands
import discord
import datetime
from modules.grapher.grapher import *

class Moh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def moh(self, ctx):
        graph(ctx.guild.id)
def setup(bot):
    bot.add_cog(Moh(bot))