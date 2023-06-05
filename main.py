import urllib

import discord
from discord.ext import commands
import requests
import configparser
from discord import Intents
import urllib.parse

# Getting Token
config = configparser.ConfigParser()
config.read('config.ini')

# Setting up intents
intents = Intents.all()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable the messages intent

bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def cleanurl(ctx):
    original_url = ctx.message.content.replace(f'{ctx.prefix}cleanurl', '').strip()
    parsed_url = urllib.parse.urlparse(original_url)
    cleaned_url = parsed_url._replace(query='', fragment='').geturl()
    await ctx.send(f'Cleaned URL: {cleaned_url}')


bot.run(config['Bot']['token'])
