import discord
from discord.ext import commands
from apikey import *
from datetime import datetime

import responses
from colors import *


def run_discord_bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = discord.Client(intents=intents)

    bot = commands.Bot(command_prefix='!', intents=intents)

    self_roles_1_id = 1027668015791214673

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')
        dash_len = len(f'{bot.user} is now running!')
        print('-' * dash_len)

    @bot.event
    async def on_raw_reaction_add(payload):
        our_message_id = self_roles_1_id
        if our_message_id == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name

            if emoji == 'Student':
                role = discord.utils.get(guild.roles, name='Student')
            elif emoji == 'SystemAdministrator':
                role = discord.utils.get(guild.roles, name='System Administrator')
            elif emoji == 'MalwareAnalyst':
                role = discord.utils.get(guild.roles, name='Malware Analyst')
            elif emoji == 'PenetrationTester':
                role = discord.utils.get(guild.roles, name='Penetration Tester')
            elif emoji == 'BugHunter':
                role = discord.utils.get(guild.roles, name='Bug Hunter')
            elif emoji == 'CTFPlayer':
                role = discord.utils.get(guild.roles, name='CTF Player')
            elif emoji == 'OpenSourceContributor':
                role = discord.utils.get(guild.roles, name='Opensource Contributor')

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await member.add_roles(role)

    @bot.event
    async def on_raw_reaction_remove(payload):
        our_message_id = self_roles_1_id

        if our_message_id == payload.message_id:
            guild = await(bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == 'Student':
                role = discord.utils.get(guild.roles, name='Student')
            elif emoji == 'SystemAdministrator':
                role = discord.utils.get(guild.roles, name='System Administrator')
            elif emoji == 'MalwareAnalyst':
                role = discord.utils.get(guild.roles, name='Malware Analyst')
            elif emoji == 'PenetrationTester':
                role = discord.utils.get(guild.roles, name='Penetration Tester')
            elif emoji == 'BugHunter':
                role = discord.utils.get(guild.roles, name='Bug Hunter')
            elif emoji == 'CTFPlayer':
                role = discord.utils.get(guild.roles, name='CTF Player')
            elif emoji == 'OpenSourceContributor':
                role = discord.utils.get(guild.roles, name='Opensource Contributor')

            member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)
                print(f"Remove: {role}.")

            else:
                print("Member not found")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello, I am thecyberbot")

    @bot.command(pass_context=True)
    async def self_roles_1(ctx):
        embed = discord.Embed(
            title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
            description="\n\n"
                        "**Self service Role Assignment!** \n"
                        "------------------------------------- \n\n"
                        "<:Student:1027660619287113799> - For **<@&1027661690386522152>** \n\n"
                        "<:SystemAdministrator:1027660624295120986> - For **<@&1027661680269861006>** \n\n"
                        "<:MalwareAnalyst:1027660606918111312> - For **<@&1023117371700936726>** \n\n"
                        "<:PenetrationTester:1027660611275989112> - For **<@&1027661584161574982>** \n\n"
                        "<:BugHunter:1027660593232097320> - For **<@&1027661563760480346>** \n\n"
                        "<:CTFPlayer:1027660596453331094> - For **<@&1021757268246659102>** \n\n"
                        "<:OpenSourceContributor:1027662647589601434> - For **<@&1000649830466584656>** \n\n"
                        "------------------------------------- \n"
                        "**Represent Who YOU ARE!!!**"
                        "",
            url="https://www.thecyberhub.org/",
            # timestamp=datetime.now(tz=None),
            color=0x2ecc71
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("<:Student:1027660619287113799>")
        await msg.add_reaction("<:SystemAdministrator:1027660624295120986>")
        await msg.add_reaction("<:MalwareAnalyst:1027660606918111312>")
        await msg.add_reaction("<:PenetrationTester:1027660611275989112>")
        await msg.add_reaction("<:BugHunter:1027660593232097320>")
        await msg.add_reaction("<:CTFPlayer:1027660596453331094>")
        await msg.add_reaction("<:OpenSourceContributor:1027662647589601434>")

        await ctx.message.add_reaction("<:BugHunter:1027642614775816242>")

    @bot.event
    async def on_member_join(member):
        channel_id = 920989002054656042
        channel = bot.get_channel(channel_id)
        await channel.send(f"Hello {member}.\nWelcome to the thecyberworld community")

    # Remember to run your bot with your personal TOKEN
    bot.run(TOKEN)
