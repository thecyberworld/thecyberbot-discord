import discord

async def self_role_helper(ctx):
    embed = discord.Embed(
            title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
            description="\n\n"
                        "**How to earn Helper Roles?** \n"
                        "------------------------------------- \n\n"
                        "<:Helper:1027660602170167317> - <@&1000649273584656414> The Helper role is a special role. Folks within our community can ping this role when they have a specific question. Anyone can choose this role, but please do not take it if you do not want too be pinged for assistance. \n\n"
                        "------------------------------------- \n"
                        "**Are you ready to help?**",
            url="https://www.thecyberhub.org/",
            # timestamp=datetime.now(tz=None),
            color=0xe67e22
        )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("<:Helper:1027660602170167317>")

    await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
