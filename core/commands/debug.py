from discord.ext import commands
import discord
import datetime
from modules.grapher.grapher import *

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def de(self, ctx):
        embed=discord.Embed(title="Rapport journalier", description="06/05/2021")
        embed.set_author(name="Foutu Stats", icon_url="https://cdn.discordapp.com/avatars/746088097422508073/61662580a73bcd3a2c6bc2f07f7ee8c5.png?size=1024")
        embed.add_field(name="Message en fonction des heures", value="rien", inline=False)
        embed.set_image(url="")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Debug(bot))