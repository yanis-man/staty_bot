import os 
import asyncio
import discord
from discord.ext import commands
import sys, traceback

import core.log.messages as Log
import modules.utils.utils as utils
from modules.configs.config import BotConfig

cfg = BotConfig()
bot = commands.Bot(command_prefix=cfg.PREFIX)


if __name__ == "__main__":
    #LOAD EXTENSIONS
    commands_files = [f for f in os.listdir(os.getcwd()+"/core/commands") if os.path.isfile(os.path.join(os.getcwd()+"/core/commands", f))]
    events_files = [f for f in os.listdir(os.getcwd()+"/core/events") if os.path.isfile(os.path.join(os.getcwd()+"/core/events", f))]
    cyclic_files = [f for f in os.listdir(os.getcwd()+"/core/cyclic") if os.path.isfile(os.path.join(os.getcwd()+"/core/cyclic", f))]
    #check if the data folder exists, see tools/utils/utils @ check_dir
    #utils.check_dir(f"{os.getcwd()}\data\\", True, "data")

    discord.Intents.all()
    for command in commands_files:
        try:
            bot.load_extension(f"core.commands.{command[:-3]}")

            Log.load_ok_msg(command[:-3])

        except Exception as error:
            print(f'[ERR] Failed to load commands {command[:-3]} : {error}')
            Log.load_error(command[:-3], error)

    for event in events_files:
        try:
            bot.load_extension(f"core.events.{event[:-3]}")
            Log.load_ok_msg(event[:-3])

        except Exception as error:
            print(f'[ERR] Failed to load extension {event[:-3]} : {error}')
            Log.load_error(event[:-3], error)
            traceback.print_exc()
    
    for cycle in cyclic_files:
        try:
            bot.load_extension(f"core.cyclic.{cycle[:-3]}")
            Log.load_ok_msg(event[:-3])

        except Exception as error:
            print(f'[ERR] Failed to load extension {cycle[:-3]} : {error}')
            Log.load_error(cycle[:-3], error)
            traceback.print_exc()
            
print("Logged in")
bot.run(cfg.TOKEN)
