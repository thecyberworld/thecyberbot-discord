import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from self_roles import self_roles_all

load_dotenv()
TOKEN = os.getenv('TOKEN')


def thecyberbot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Add new functions below
    self_roles_all(bot, discord)

    bot.run(TOKEN)
