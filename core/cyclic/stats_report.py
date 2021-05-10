from discord.ext import tasks, commands
import asyncio

class StatsReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.daily_report.start()

    def cog_unload(self):
        self.daily_report.cancel()

    @tasks.loop(hours=24.0)
    async def daily_report(self):
        print(self.index)
        self.index += 1
    
    @daily_report.before_loop
    async def wait_bot(self):
        print("waiting for bot to start")
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(StatsReport(bot))