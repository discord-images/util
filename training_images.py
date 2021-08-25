import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_API_KEY')
limit = int(os.getenv('MESSAGE_LIMIT'))
channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
client = discord.Client()


async def shutdown():
    await client.close()
    try:
        exit()
    except:
        print("closed")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel: discord.channel.TextChannel = client.get_channel(channel_id)
    if channel is None:
        await shutdown()
    message: discord.Message

    async for message in channel.history(limit=limit):
        if len(message.attachments) > 0:
            att: discord.Attachment
            for att in message.attachments:
                print(att.url)

    await shutdown()


client.run(token)
