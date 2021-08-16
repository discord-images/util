import discord

counter = 0

async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1
