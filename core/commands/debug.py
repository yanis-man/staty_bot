from discord.ext import commands
import discord
from discord import Guild

from modules.grapher.data_manager import get_message_stat_data
from modules.utils.utils import return_chann_object

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def de(self, ctx):
        GUILD_ID = ctx.guild.id
        await ctx.send(get_message_stat_data(self.bot, GUILD_ID))
def setup(bot):
    bot.add_cog(Debug(bot))