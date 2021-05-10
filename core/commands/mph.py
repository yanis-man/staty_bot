from discord.ext import commands
import discord

from modules.viewers.graph_viewer import generate_embed
from modules.configs.config import EmbedTitle, FileConfig, Help
from modules.grapher.data_manager import get_moh_data, get_uph_data
from modules.grapher.grapher import bar_plot
from modules.tools.date_modifier import parse_limit


EmbedCfg = EmbedTitle()
FileCfg = FileConfig()
HelpCfg = Help()

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help=HelpCfg.MPH_HELP)
    async def mph(self, ctx, limit = "1j"):

        moh_data = get_moh_data(ctx.guild.id, limit)
        bar_plot(ctx.guild.id, FileCfg.MOH_FILENAME, moh_data[0], moh_data[1])

        await ctx.send(embed=generate_embed(f"{EmbedCfg.MOH_TITLE} du {parse_limit(limit)} à Aujourd'hui", ctx.guild.id, limit, FileCfg.MOH_FILENAME))

    @commands.command(help=HelpCfg.UPH_HELP)
    async def uph(self, ctx, limit = "1j"):
        uph_data = get_uph_data(ctx.guild.id, limit)
        bar_plot(ctx.guild.id, FileCfg.UPH_FILENAME, uph_data[0], uph_data[1])

        await ctx.send(embed=generate_embed(f"{EmbedCfg.UPH_TITLE} du {parse_limit(limit)} à Aujourd'hui", ctx.guild.id, limit, FileCfg.UPH_FILENAME))
def setup(bot):
    bot.add_cog(Stats(bot))