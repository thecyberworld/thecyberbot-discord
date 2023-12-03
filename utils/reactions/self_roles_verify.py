import discord


async def self_role_verify(ctx):
    embed = discord.Embed(
        title="**<:thecyberworld:1027642656614006874> Thecyberworld's Discord Server Roles!**",
        description="\n\n"
                    "**Verify :white_check_mark:** \n"
                    "------------------------------------- \n"
                    "**After clicking on the below checkbox you will get the access to this server.** \n"
                    "**Make sure to choose your #roles after verifying yourself.** \n",
        url="https://www.thecyberhub.org/",
        # timestamp=datetime.now(tz=None),
        color=0xe67e22
    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("<:Checkbox:1059552410516869170>")

    await ctx.message.add_reaction("<:thecyberworldbg:1027660630620131378>")
