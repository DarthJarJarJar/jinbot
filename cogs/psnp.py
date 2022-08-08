import asyncio
import json
import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
import aiohttp

guild_id = 826766972204744764
MY_GUILD_ID = discord.Object(guild_id)


async def get_data(username, page):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://peaceful-river-36217.herokuapp.com/user/trophies/{username}/{page}") as resp:
            print(await resp.read())
            content = json.loads(await resp.read())
            print(content)
            return content


async def get_trophy_count(username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://peaceful-river-36217.herokuapp.com/user/trophies/{username}/0") as resp:
            content = json.loads(await resp.read())
            print(content)
            return content


def make_bold(string):
    initial = "**"
    middle = initial + str(string)
    final = middle + initial
    return final


def get_trophy_value_string(earnedTrophies):
    emojis = Emojis()
    space = emojis.blank + emojis.blank + emojis.blank
    trophy_details = f"{emojis.gold} {make_bold(earnedTrophies['bronze'])}{space}{emojis.silver} {make_bold(earnedTrophies['silver'])}{space}{emojis.gold} {make_bold(earnedTrophies['gold'])}{space}{emojis.platinum} {make_bold(earnedTrophies['platinum'])} "
    return trophy_details


def make_trophy_embed(username, gameobject, page, count):
    embed = discord.Embed(title=f"`{username}`'s Trophies", colour=discord.Color.green())
    for game in gameobject:
        trophy_details = get_trophy_value_string(game['earnedTrophies'])
        embed.add_field(name=f"{game['trophyTitleName']} ({game['trophyTitlePlatform']})", value=trophy_details,
                        inline=False)
        embed.set_footer(text=f"Page {page}/{count}")
    return embed


class Emojis:
    def __init__(self):
        self.bronze = "<:bronze:1003401053401796788>"
        self.silver = "<:silver:1003401877016297562>"
        self.gold = "<:gold:1003401075979726980>"
        self.platinum = "<:plat:1003401209585078363>"
        self.blank = "<:blank:1003408619376742441>"
        self.bronze1PROFILE = "<:b1:1003434859362005052>"
        self.bronze2PROFILE = "<:b2:1003434879373017129>"
        self.bronze3PROFILE = "<:b3:1003434893893709855>"
        self.silver1PROFILE = "<:s1:1003434996637380628>"
        self.silver2PROFILE = "<:s2:1003435020939165776>"
        self.silver3PROFILE = "<:s3:1003435049456242760>"
        self.gold1PROFILE = "<:g1:1003434915146252418>"
        self.gold2PROFILE = "<:g2:1003434934037397576>"
        self.gold3PROFILE = "<:g3:1003434968984338558>"
        self.platinumPROFILE = "<:p_:1003435077159620629>"
        self.loading = "<a:loading:920845271892643861>"


class Counter(discord.ui.View):
    def __init__(self, username: str, max: int):
        super().__init__()
        self.page = 1
        self.max = max
        self.username = username

    @discord.ui.button(label="<<", style=discord.ButtonStyle.green, disabled=True)
    async def backward(self, interaction: discord.Interaction, button: discord.ui.Button):

        self.page -= 1
        if self.page == 1:
            self.backward.disabled = True
        if self.page < 10:
            self.forward.disabled = False
        data = await get_data(self.username, self.page)
        embed = make_trophy_embed(self.username, data, self.page, self.max)
        await interaction.response.edit_message(view=self, embed=embed)

    @discord.ui.button(label=">>", style=discord.ButtonStyle.green)
    async def forward(self, interaction: discord.Interaction, button: discord.ui.Button):

        self.page += 1
        if self.page > 1:
            self.backward.disabled = False
        if self.page == self.max:
            self.forward.disabled = True
        data = await get_data(self.username, self.page)
        embed = make_trophy_embed(self.username, data, self.page, self.max)
        await interaction.response.edit_message(view=self, embed=embed)


class psnp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna make you cry')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def getpsn(self, ctx: commands.Context, username):
        message = await ctx.send(Emojis().loading)
        data = await get_data(username, 1)
        count = await get_trophy_count(username)
        embed = make_trophy_embed(username, data, 1, ((int(count["count"])) // 10) + 1)
        await message.edit(content=None, embed=embed, view=Counter(username, ((int(count["count"])) // 10) + 1))

    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(psnp(client))
