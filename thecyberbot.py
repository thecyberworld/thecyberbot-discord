import discord
import responses
from discord.ext import commands
from apikey import *
import colorama
from colors import *

def run_discord_bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    client = discord.Client(intents=intents)

    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        dash_len = len(f'{client.user} is now running!')
        print('-' * dash_len)

    @client.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 1026806386694307851:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            if payload.emoji.name == 'thecyberbotdiscord':
                role = discord.utils.get(guild.roles, name='cybersecurity')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(role.name)
                else:
                    print("Member not found.")
            else:
                print("Role not found.")

    @client.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 1026806386694307851:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            if payload.emoji.name == 'Student':
                role = discord.utils.get(guild.roles, name='Student')
            elif payload.emoji.name == 'BugHunter':
                role = discord.utils.get(guild.roles, name='Bug Hunter')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(role.name)
                else:
                    print("Member not found.")
            else:
                print("Role not found.")

    @client.event
    async def on_raw_reaction_remove(role):
        print("remove hello")

    @client.command()
    async def hello(ctx):
        await ctx.send("Hello, I am thecyberbot")

    @client.command()
    async def self_roles(display_roles):
        await display_roles.send(""
                                 "<:Student:1026898913724207165> for Student role\n"
                                 "<:BugHunter:1026898877523181648> for", RED, " Bug Hunter role\n"
                                 "")

    @client.event
    async def on_member_join(member):
        channel_id = 920989002054656042
        channel = client.get_channel(channel_id)
        await channel.send(f"Hello {member}.\nWelcome to the thecyberworld community")

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
