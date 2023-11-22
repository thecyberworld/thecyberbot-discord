import discord

async def self_role_pro(ctx):
    embed = discord.Embed(
            title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
            description="\n\n"
                        "**How to earn Special Roles?** \n"
                        "------------------------------------- \n\n"
                        "<:Volunteer:1031742474269499393> - **<@&1028936957260201994>** will be selected manually based on their contribution and engagement on the server. \n\n"
                        "<:Moderator:1027660630620131378> - **<@&843201976418566145>** will be chosen by many variables. Not just from asking!! \n\n"
                        "<:Professional:1031742465901875220> - **<@&1028937084033044540>** You Must be a Pro!! will be chosen from helping, activity, ect. Not just from asking!! Also the role can be removed!! \n\n"
                        "------------------------------------- \n"
                        "**Are you ready?**",
            url="https://www.thecyberhub.org/",
            # timestamp=datetime.now(tz=None),
            color=0xe74c3c
        )

    msg = await ctx.send(embed=embed)
    # await msg.add_reaction("<:BlueTeam:1026898873471471697>")
    # await msg.add_reaction("<:RedTeam:1027642650653896724>")
    # await msg.add_reaction("<:PurpleTeam:1027642647076151326>")

    await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
