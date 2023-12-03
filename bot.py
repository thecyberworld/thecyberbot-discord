import discord

from discord.ext import commands
import requests
from bardapi import Bard
from dotenv import load_dotenv
from requests.exceptions import ReadTimeout
from retrying import retry
import os
import logging

# Create a Discord bot instance with the correct command_prefix
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

token = os.getenv("BARD_API_KEY")
print(token)
BARD_API_KEY = os.getenv("BARD_API_KEY")

Discord_Token = os.getenv("TOKEN")
discord_token = Discord_Token

if not token:
    raise ValueError("BARD_API_KEY environment variable not set")

bard = Bard(token=token)


@retry(
    retry_on_exception=lambda exc: isinstance(exc, ReadTimeout),
    wait_exponential_multiplier=1000,  # Wait for 1 second, then 2 seconds, 4 seconds, etc.
    stop_max_attempt_number=3,  # Maximum of 3 retries
)
@bot.event
async def on_message(message):
    print(message)
    if message.author.bot or isinstance(message.channel, discord.DMChannel):
        return

    content = message.content.lower()
    if content:
        your_intro_prompt = f"""
        human: I am @{message.author.global_name}
        Prompt: {content}

        always reply to user with {message.author.mention} name when required
        """

        bard_response = perform_search(your_intro_prompt)

        # Check if the response is too long
        if len(bard_response) > 2000:
            # Split the response into parts
            parts = [bard_response[i:i + 2000] for i in range(0, len(bard_response), 2000)]

            # Send each part in a separate message
            for part in parts:
                await message.channel.send(part)
        else:
            await message.channel.send(bard_response)
    else:
        await message.channel.send("No search results found.")


def perform_search(query):
    try:
        response = bard.get_answer(query)
        print("check perform response:\n\n", response)
        if response:
            return response['content']
        else:
            return "No search results found."
    except ReadTimeout as e:
        print(f"Error in perform_search: {str(e)}")


bot.run(discord_token)
