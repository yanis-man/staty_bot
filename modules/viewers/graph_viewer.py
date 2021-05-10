from discord import Embed
import os

from modules.grapher.grapher import graph
from modules.tools.file_uploader import upload_image
from modules.configs.config import FileConfig

FileCfg = FileConfig()

def generate_embed(title, server_id, limit, filename):
    graph_url = upload_image(f"{os.getcwd()}\\data\\{server_id}\\charts\\{filename}.{FileCfg.FILE_EXTENSION}")

    embed=Embed(title=title, description=" ")
    embed.set_author(name=" ")
    embed.set_image(url=graph_url)

    return embed