import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from requests.exceptions import ReadTimeout
from retrying import retry
import json

load_dotenv()

discord_token = os.getenv('Discord_Token')
palm_key = os.getenv('PalmAI')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'The bot is ready for use!')
    print('--------------------------')


@retry(
    retry_on_exception=lambda exc: isinstance(exc, ReadTimeout),
    wait_exponential_multiplier=1000,  # Wait for 1 second, then 2 seconds, 4 seconds, etc.
    stop_max_attempt_number=3,  # Maximum of 3 retries
)
def ai_generate_response(message):
    url = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=" + palm_key

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'prompt': {
            'text': message
        }
    }
    # Convert data to JSON format
    json_data = json.dumps(data)

    # Make the API request
    response = requests.post(url, headers=headers, data=json_data)

    # Check if the request was successful (status code 200)
    try:
        if response.status_code == 200:
            # Parse and return the JSON response
            return_response = response.json()['candidates'][0]['output']
            # print(return_response)
            return return_response
        else:
            # If the request was not successful, print an error message and return None
            return None
    except Exception as e:
        # print(e)
        return "We can't Provide you this information here, but you can do your own research on it"


@bot.event
async def on_message(message):
    if not bot.user.mentioned_in(message):
        return
    # print(bot.user.mentioned_in(message))
    if message.author.bot or isinstance(message.channel, discord.DMChannel):
        return
    # if message.channel.name != "girolamo-chat":
    #     return
    await message.channel.typing()

    content = message.content.lower()
    # print("User Message:", content, "\n")

    if content:
        await message.channel.typing()
        your_intro_prompt = (f" You are Bashit, the great guru with the manner of India Vedh/Vyaas and "
                             f"latest technologies. You should have to answer in logical base and precised, "
                             f"below is the information:"
                             f"        human: I am @{message.author.global_name}\n"
                             f"        Prompt: {content}\n"
                             f"\n"
                             f"        always reply to user with {message.author.mention} name when required\n"
                             f"            \n"
                             f"            ")

        async with message.channel.typing():
            palm_response = ai_generate_response(your_intro_prompt)
            await message.channel.typing()

            # Check if the response is too long
            if len(palm_response) > 2000:
                # Split the response into parts
                parts = [palm_response[i:i + 2000] for i in range(0, len(palm_response), 2000)]

                # Send each part in a separate message
                for part in parts:
                    await message.channel.typing()
                    await message.channel.send(part)

            else:
                await message.channel.typing()
                await message.channel.send(palm_response)

            await bot.process_commands(message)
    else:
        await message.channel.send("No search results found.")


bot.run(discord_token)
