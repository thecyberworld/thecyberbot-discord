import discord


async def self_role_team(ctx):
    embed = discord.Embed(
        title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
        description="\n\n"
                    "**Are you Blue Team,Red Team, or a little Both?** \n"
                    "**Let us know what Team you Represent by reacting down below!!!** \n"
                    "------------------------------------- \n\n"
                    "<:BlueTeam:1026898873471471697> - **<@&1028925586292351036>** Defense\n\n"
                    "<:RedTeam:1027642650653896724> - **<@&1028925597931540490>** Offense\n\n"
                    "<:PurpleTeam:1027642647076151326> - **<@&1028925767742136412>** Both\n\n"
                    "------------------------------------- \n"
                    "**The best Defense is a good Offense!**"
                    "",
        url="https://www.thecyberhub.org/",
        # timestamp=datetime.now(tz=None),
        color=0x7289da
    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("<:BlueTeam:1026898873471471697>")
    await msg.add_reaction("<:RedTeam:1027642650653896724>")
    await msg.add_reaction("<:PurpleTeam:1027642647076151326>")

    await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
