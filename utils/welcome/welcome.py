def welcome_message(bot, random, member, discord, colors):
    channel_id = 920989002054656042
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

    return embed, channel