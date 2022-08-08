import asyncio
from dis import dis
from distutils.log import error
from typing import List
import discord
from discord.ext import commands
from discord.utils import get
from cogs import cog, psn, tagdb, gamble, levelsys
import os
import io
import traceback
import aiohttp
import sys
from discord import app_commands


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True,
                          message_content=True, )
client = commands.Bot(command_prefix='*', intents=intents, case_insensitive=True, )
bot = client
guild_id = os.environ["GUILD_ID"]

TOKEN = os.environ["TOKEN"]
MY_GUILD_ID = discord.Object(guild_id)
cogs = [cog, tagdb, levelsys, gamble, psn]
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



async def try_hastebin(content):
    """Upload to Hastebin, if possible."""
    payload = content.encode('utf-8')
    async with aiohttp.ClientSession(raise_for_status=True) as cs:
        async with cs.post('https://hastebin.com/documents', data=payload) as res:
            post = await res.json()
    uri = post['key']
    return f'https://hastebin/{uri}'

async def send_to_owner(content, string):
    """Send content to owner. If content is small enough, send directly.
    Otherwise, try Hastebin first, then upload as a File."""
    channel = bot.get_channel(872335733287956500)
    if len(content) < 1990:
        await channel.send(f'{(await bot.fetch_user(749901028832575558)).mention} {string}\n```python\n{content}\n```')
    else:
        try:
            await channel.send(await try_hastebin(content))
        except aiohttp.ClientResponseError:
            await channel.send(content=string, file=discord.File(io.StringIO(content), filename='traceback.txt'))

@bot.event
async def on_error(event, *args, **kwargs):
    """Error handler for all events."""
    s = traceback.format_exc()
    content = f'Ignoring exception in {event}\n{s}'
    print(content, file=sys.stderr)
    string = "An error occured"
    await send_to_owner(content, string)

async def handle_command_error(ctx: commands.Context, exc: Exception):
    """Handle specific exceptions separately here"""
    pass

@bot.event
async def on_command_error(ctx: commands.Context, exc: Exception):
    """Error handler for commands"""

    # Log the error and bug the owner.
    exc = getattr(exc, 'original', exc)
    lines = ''.join(traceback.format_exception(exc.__class__, exc, exc.__traceback__))
    lines = f'Ignoring exception in command {ctx.command}:\n{lines}'
    print(lines)
    channel = bot.get_channel(872335733287956500)
    string = f"Error in the command called in message {ctx.message.jump_url}"
    await send_to_owner(lines, string)

@client.command()
@commands.is_owner()
async def sync(ctx):
    await tree.sync(guild=MY_GUILD_ID)
    await ctx.send('synced commands')
    
async def fruit_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
        app_commands.Choice(name=fruit, value=fruit)
        for fruit in fruits if current.lower() in fruit.lower()
    ]

@app_commands.command()
@app_commands.guilds(MY_GUILD_ID)
@app_commands.autocomplete(fruit=fruit_autocomplete)
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')
@client.command()
async def checkenv(ctx):
    item = os.environ["GUILD_ID"]
    await ctx.send(item)

@client.command()
async def check(ctx):
    member = ctx.author
    if (discord.utils.utcnow() - member.created_at).days < 5:
            await ctx.send("Less than 5 days")
    else:
        await ctx.send("More than 5 days")


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
