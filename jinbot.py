import discord
from discord.ext import commands
from discord.utils import get


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='*', intents=intents)

welcome = "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>"





@client.event
async def on_ready():
    print('never gonna give you up')


@client.event
async def on_member_join(member):
    print(f'welcome {member}')
    channel = client.get_channel(854247382086189066)
    await channel.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")
    role = get(member.guild.roles, id=833781809128669265)
    await member.add_roles(role)


@client.event
async def on_member_remove(member):
    print(f'goodbye {member}')


@client.command()
async def jin(ctx):
    await ctx.send('<:jinhappy1:835921639551008818>')


@client.command()
async def xbox(ctx):
    await ctx.send('better')


@client.command()
async def playstation(ctx):
    await ctx.send('<:sony:858204031067357195>')


@client.command()
async def rickroll(ctx):
    await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')


@client.command()
async def rule16(ctx):
    await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')


@client.command()
async def welcome(ctx):
    await ctx.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")



client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.LyGuLuvwZuRiPuzf25n1kBOh4hQ')
