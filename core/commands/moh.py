from discord.ext import commands
import discord

from modules.viewers.graph_viewer import generate_embed
from modules.configs.config import EmbedTitle, FileConfig

EmbedCfg = EmbedTitle()
FileCfg = FileConfig()

class Moh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def moh(self, ctx, limit = "1j"):
        await ctx.send(embed=generate_embed(EmbedCfg.MOH_TITLE, ctx.guild.id, limit, FileCfg.MOH_FILENAME))
def setup(bot):
    bot.add_cog(Moh(bot))