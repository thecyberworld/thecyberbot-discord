import discord
from discord.ext import commands
from apikey import *
import asyncio
import random
# import pafy
import youtube_dl

colors = [
    0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694,
    0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e,
    0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b,
    0x979c9f, 0x546e7a, 0x7289da, 0x99aab5
]


def run_discord_bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)
    discord_bot = discord.Client(intents=intents)
    self_roles_1_id = 1027668015791214673
    self_roles_cyber_team_id = 1031750672141537352
    self_roles_helper_id = 1031755073128247397
    self_roles_verify_id = 1059559943071608853

    # self_roles_pro_id = 1027668015791214673

    @bot.event
    async def on_ready():
        dash_len = len(f'{bot.user} is now running!')
        print('-' * dash_len)
        print(f'{bot.user} is now running!')
        print('-' * dash_len)

        # channel_lofi = bot.get_channel(1066752630333919373)
        # vc = await channel_lofi.connect()
        # video = pafy.new("https://www.youtube.com/watch?v=8nXqcugV2Y4")
        # bestaudio = video.getbestaudio()
        # playurl = bestaudio.url
        while True:
            # vc.play(discord.FFmpegOpusAudio(playurl))
            # await asyncio.sleep(1)

            channel = bot.get_channel(1065245064613343313)
            async for message in channel.history(limit=1):
                latest_message = message
                content = latest_message.content
                if content.isnumeric():
                    latest_message = await channel.fetch_message(channel.last_message_id)
                    number = int(latest_message.content) + 1
                    await channel.send(str(number))
                await asyncio.sleep(60 * 30)

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

        # These roles can be given by the admins only
        # pro_message_id = self_roles_pro_id
        # if pro_message_id == payload.message_id:
        #     member = payload.member
        #     guild = member.guild
        #     emoji = payload.emoji.name
        #
        #     if emoji == 'Volunteer':
        #         role = discord.utils.get(guild.roles, name='Student')
        #     elif emoji == 'Professional':
        #         role = discord.utils.get(guild.roles, name='Professional')
        #     elif emoji == 'Volunteer':
        #         role = discord.utils.get(guild.roles, name='System Administrator')
        #     else:
        #         role = discord.utils.get(guild.roles, name=payload.emoji.name)
        #     await member.add_roles(role)

        # RedTeam roles
        cyber_teams_message_id = self_roles_cyber_team_id
        if cyber_teams_message_id == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name

            if emoji == 'BlueTeam':
                role = discord.utils.get(guild.roles, name='Blue Team')
            elif emoji == 'RedTeam':
                role = discord.utils.get(guild.roles, name='Red Team')
            elif emoji == 'PurpleTeam':
                role = discord.utils.get(guild.roles, name='Purple Team')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await member.add_roles(role)

        # Helper roles
        helper_message_id = self_roles_helper_id
        if helper_message_id == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == 'Helper':
                role = discord.utils.get(guild.roles, name='Helper')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await member.add_roles(role)

        # Verify roles
        verify_message_id = self_roles_verify_id
        if verify_message_id == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == 'Checkbox':
                role = discord.utils.get(guild.roles, name='verified')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await member.add_roles(role)

    # Removed roles
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

        # RedTeam roles
        cyber_teams_message_id = self_roles_cyber_team_id
        if cyber_teams_message_id == payload.message_id:
            guild = await(bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == 'BlueTeam':
                role = discord.utils.get(guild.roles, name='Blue Team')
            elif emoji == 'RedTeam':
                role = discord.utils.get(guild.roles, name='Red Team')
            elif emoji == 'PurpleTeam':
                role = discord.utils.get(guild.roles, name='Purple Team')
            member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)
                print(f"Remove: {role}.")
            else:
                print("Member not found")

        # Helper role
        helper_message_id = self_roles_helper_id
        if helper_message_id == payload.message_id:
            guild = await(bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == 'Helper':
                role = discord.utils.get(guild.roles, name='Helper')
            member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)
                print(f"Remove: {role}.")
            else:
                print("Member not found")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello, I am thecyberbot")

    # @bot.command(pass_context=True)
    # async def self_roles_1(ctx):
    #     embed = discord.Embed(
    #         title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
    #         description="\n\n"
    #                     "**Self service Role Assignment!** \n"
    #                     "------------------------------------- \n\n"
    #                     "<:Student:1027660619287113799> - For **<@&1027661690386522152>** \n\n"
    #                     "<:SystemAdministrator:1027660624295120986> - For **<@&1027661680269861006>** \n\n"
    #                     "<:MalwareAnalyst:1027660606918111312> - For **<@&1023117371700936726>** \n\n"
    #                     "<:PenetrationTester:1027660611275989112> - For **<@&1027661584161574982>** \n\n"
    #                     "<:BugHunter:1027660593232097320> - For **<@&1027661563760480346>** \n\n"
    #                     "<:CTFPlayer:1027660596453331094> - For **<@&1021757268246659102>** \n\n"
    #                     "<:OpenSourceContributor:1027662647589601434> - For **<@&1000649830466584656>** \n\n"
    #                     "------------------------------------- \n"
    #                     "**Represent Who YOU ARE!!!**"
    #                     "",
    #         url="https://www.thecyberhub.org/",
    #         # timestamp=datetime.now(tz=None),
    #         color=0x2ecc71
    #     )
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction("<:Student:1027660619287113799>")
    #     await msg.add_reaction("<:SystemAdministrator:1027660624295120986>")
    #     await msg.add_reaction("<:MalwareAnalyst:1027660606918111312>")
    #     await msg.add_reaction("<:PenetrationTester:1027660611275989112>")
    #     await msg.add_reaction("<:BugHunter:1027660593232097320>")
    #     await msg.add_reaction("<:CTFPlayer:1027660596453331094>")
    #     await msg.add_reaction("<:OpenSourceContributor:1027662647589601434>")
    #
    #     await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")

    # @bot.command(pass_context=True)
    # async def self_roles_cyber_teams(ctx):
    #     embed = discord.Embed(
    #         title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
    #         description="\n\n"
    #                     "**Are you Blue Team,Red Team, or a little Both?** \n"
    #                     "**Let us know what Team you Represent by reacting down below!!!** \n"
    #                     "------------------------------------- \n\n"
    #                     "<:BlueTeam:1026898873471471697> - **<@&1028925586292351036>** Defense\n\n"
    #                     "<:RedTeam:1027642650653896724> - **<@&1028925597931540490>** Offense\n\n"
    #                     "<:PurpleTeam:1027642647076151326> - **<@&1028925767742136412>** Both\n\n"
    #                     "------------------------------------- \n"
    #                     "**The best Defense is a good Offense!**"
    #                     "",
    #         url="https://www.thecyberhub.org/",
    #         # timestamp=datetime.now(tz=None),
    #         color=0x7289da
    #     )
    #
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction("<:BlueTeam:1026898873471471697>")
    #     await msg.add_reaction("<:RedTeam:1027642650653896724>")
    #     await msg.add_reaction("<:PurpleTeam:1027642647076151326>")
    #
    #     await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
    #
    # @bot.command(pass_context=True)
    # async def self_roles_cyber_pro(ctx):
    #     embed = discord.Embed(
    #         title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
    #         description="\n\n"
    #                     "**How to earn Special Roles?** \n"
    #                     "------------------------------------- \n\n"
    #                     "<:Volunteer:1031742474269499393> - **<@&1028936957260201994>** will be selected manually based on their contribution and engagement on the server. \n\n"
    #                     "<:Moderator:1027660630620131378> - **<@&843201976418566145>** will be chosen by many variables. Not just from asking!! \n\n"
    #                     "<:Professional:1031742465901875220> - **<@&1028937084033044540>** You Must be a Pro!! will be chosen from helping, activity, ect. Not just from asking!! Also the role can be removed!! \n\n"
    #                     "------------------------------------- \n"
    #                     "**Are you ready?**",
    #         url="https://www.thecyberhub.org/",
    #         # timestamp=datetime.now(tz=None),
    #         color=0xe74c3c
    #     )
    #
    #     msg = await ctx.send(embed=embed)
    #     # await msg.add_reaction("<:BlueTeam:1026898873471471697>")
    #     # await msg.add_reaction("<:RedTeam:1027642650653896724>")
    #     # await msg.add_reaction("<:PurpleTeam:1027642647076151326>")
    #
    #     await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
    #
    # @bot.command(pass_context=True)
    # async def self_roles_helper(ctx):
    #     embed = discord.Embed(
    #         title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
    #         description="\n\n"
    #                     "**How to earn Helper Roles?** \n"
    #                     "------------------------------------- \n\n"
    #                     "<:Helper:1027660602170167317> - <@&1000649273584656414> The Helper role is a special role. Folks within our community can ping this role when they have a specific question. Anyone can choose this role, but please do not take it if you do not want too be pinged for assistance. \n\n"
    #                     "------------------------------------- \n"
    #                     "**Are you ready to help?**",
    #         url="https://www.thecyberhub.org/",
    #         # timestamp=datetime.now(tz=None),
    #         color=0xe67e22
    #     )
    #
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction("<:Helper:1027660602170167317>")
    #
    #     await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
    #
    # @bot.command(pass_context=True)
    # async def self_roles_verify(ctx):
    #     embed = discord.Embed(
    #         title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
    #         description="\n\n"
    #                     "**Verify :white_check_mark:** \n"
    #                     "------------------------------------- \n"
    #                     "**After clicking on the below checkbox you will get the access to this server.** \n"
    #                     "**Make sure to choose your #roles after verifying yourself.** \n",
    #         url="https://www.thecyberhub.org/",
    #         # timestamp=datetime.now(tz=None),
    #         color=0xe67e22
    #     )
    #
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction("<:Checkbox:1059552410516869170>")
    #
    #     await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")

    # on join welcome message
    @bot.event
    async def on_member_join(member):
        channel_id = 799183505808556044
        channel = bot.get_channel(channel_id)
        user_count = len(member.guild.members)
        color = random.choice(colors)
        color = color
        embed = discord.Embed(
            title=f"Thecyberworld Community",
            description=f"Welcome {member.name} ({member.mention}) to the server! \nWe are now **{user_count}** members strong!",
            color=color
        )
        embed.add_field(name="Community Links", value="https://linktr.ee/thecyberworld", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await channel.send(embed=embed)

    # @bot.event
    # async def on_member_ban(member):
    #     channel_id = 1066976296321691658
    #     channel = bot.get_channel(channel_id)
    #     ban_reason = "Violation of the rules"
    #     embed = discord.Embed(
    #         title=f"{member.name} has been banned",
    #         description=f"Reason: {ban_reason}",
    #         color=0xff0000
    #     )
    #     embed.add_field(name="Member", value=f"{member.name} ({member.mention})", inline=False)
    #     await channel.send(embed=embed)
    #
    # @bot.event
    # async def on_member_remove(member):
    #     channel_id = 1066976296321691658
    #     channel = bot.get_channel(channel_id)
    #     kick_reason = "Violation of the rules"
    #     embed = discord.Embed(
    #         title=f"{member.name} has been kicked",
    #         description=f"Reason: {kick_reason}",
    #         color=0xff0000
    #     )
    #     embed.add_field(name="Member", value=f"{member.name} ({member.mention})", inline=False)
    #     embed.set_thumbnail(url=member.avatar.url)
    #     await channel.send(embed=embed)

    # @bot.event
    # async def on_ready():
    #     channel_id = 1066752630333919373
    #     channel = bot.get_channel(channel_id)
    #     vc = await channel.connect()
    #     video = pafy.new("https://www.youtube.com/watch?v=8nXqcugV2Y4")
    #     bestaudio = video.getbestaudio()
    #     playurl = bestaudio.url
    #     await bot.get_channel(1065245064613343313).send(str("music is working"))
    #     while True:
    #         vc.play(discord.FFmpegOpusAudio(playurl))
    #         await asyncio.sleep(1)


    # Remember to run your bot with your personal TOKEN
    bot.run(TOKEN)
