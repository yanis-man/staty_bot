from discord.ext import tasks, commands
import asyncio
import csv

class StatsReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.daily_report.start()

    def cog_unload(self):
        self.daily_report.cancel()

    @tasks.loop(hours=24.0)
    async def daily_report(self):
        

def setup(bot):
    bot.add_cog(StatsReport(bot))