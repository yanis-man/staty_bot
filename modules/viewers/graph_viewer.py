from discord import Embed
import os

from modules.tools.file_uploader import upload_image
from modules.configs.config import FileConfig

FileCfg = FileConfig()

def generate_embed(title, desc, server_id, limit, filename):
    graph_url = upload_image(f"{os.getcwd()}\\data\\{server_id}\\charts\\{filename}.{FileCfg.FILE_EXTENSION}")

    embed=Embed(title=title, description=desc)
    embed.set_author(name=" ")
    embed.set_image(url=graph_url)

    return embed

def generate_msg_stats_embed(fields_titles, fields_values, total):
        embed=Embed(title="Statistiques du serveur", description=f"Statistiques d \n Nombres total de messages : {total} ")
        for i in range(len(fields_titles)):
            embed.add_field(name=fields_titles[i], value=fields_values[i], inline=False)
        
        return embed