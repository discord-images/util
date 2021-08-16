import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_API_KEY')
client = discord.Client()


async def start():
    await client.start(token)


async def last_images():
    channel = client.get_channel(642911304876818453)
    for message in channel.history(limit=20):
        print(message)

start()
last_images()
