
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
