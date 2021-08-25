import discord
from dotenv import load_dotenv
import os
import sys

load_dotenv()
token = os.getenv('DISCORD_API_KEY')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel: discord.channel.TextChannel = client.get_channel(
        642911304876818456)
    if channel is None:
        sys.exit()
    for message in channel.history(limit=20).flatten():
        print(message)
    sys.exit()

client.run(token)
