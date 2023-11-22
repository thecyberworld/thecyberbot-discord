import discord
import asyncio

async def ready(bot):
    dash_len = len(f'{bot.user} is now running!')
    print('-' * dash_len)
    print(f'{bot.user} is now running!')
    print('-' * dash_len)
    while True:
        channel = bot.get_channel(1065245064613343313)
        async for message in channel.history(limit=1):
            latest_message = message
            content = latest_message.content
            if content.isnumeric():
                latest_message = await channel.fetch_message(channel.last_message_id)
                number = int(latest_message.content) + 1
                await channel.send(str(number))
            await asyncio.sleep(60 * 30)
