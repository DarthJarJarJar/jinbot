import asyncio
from distutils.log import error
import discord
from discord.ext import commands
from discord.utils import get
from cogs import cog, tagdb, psn, gamble, levelsys
import os

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True,
                          message_content=True, )
client = commands.Bot(command_prefix='*', intents=intents, case_insensitive=True, )
guild_id = os.environ["GUILD_ID"]

TOKEN = os.environ["TOKEN"]
MY_GUILD_ID = discord.Object(guild_id)
cogs = [cog, tagdb, psn, levelsys, gamble]
tree = client.tree


async def cogscogs():
    for i in range(len(cogs)):
        await cogs[i].setup(client)
        print("e")

asyncio.run(cogscogs())



@client.event
async def on_ready():
    print("Ready!")
    await client.change_presence(activity=discord.Game(name="Jin of Jinshima"))
    # await tree.sync(guild=MY_GUILD_ID)


async def setup_hook() -> None:
    client.add_view(cog.PersistentView())
    


asyncio.run(setup_hook())


@client.command()
@commands.is_owner()
async def sync(ctx):
    await tree.sync(guild=MY_GUILD_ID)
    await ctx.send('synced commands')

@client.command()
async def checkenv(ctx):
    item = os.environ["GUILD_ID"]
    await ctx.send(item)


@client.event
async def on_member_join(member: discord.Member):
    if member.guild.name == "Jincord":
        channel = client.get_channel(854247382086189066)
        jinchain = client.get_channel(834406006351462420)
        jinrules = client.get_channel(893929998614925322)
        await channel.send(
            "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")
        embed1 = discord.Embed(title=f"Welcome {member}!",
                               description=f"Contribute to {jinchain.mention} and check out {jinrules.mention} to get started! Remember to flame on and on and on and on")
        embed1.set_image(url="https://media.discordapp.net/attachments/826766972204744767/885951474109149274/tumblr_ovbx1zq11b1vo889bo8_400.gifv.gif")
        await channel.send(content=member.mention, embed=embed1)
        role = get(member.guild.roles, id=833781809128669265)
        await member.add_roles(role)


client.run(TOKEN)
