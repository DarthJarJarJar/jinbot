from pymongo import MongoClient
import json
import random
import urllib.parse
from pathlib import Path
import discord
from discord import app_commands
from discord.ext import commands


script_dir = Path(__file__).parent

guild_id = 826766972204744764
MY_GUILD_ID = discord.Object(guild_id)

username = urllib.parse.quote_plus('darthjarjar')
password = urllib.parse.quote_plus('A@yaan12')

cluster = MongoClient(
    'mongodb+srv://%s:%s@cluster0.u6uh4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority' % (username, password))

guilds = [826766972204744764]

levelling = cluster["discord"]["levelling"]

'''
contribution by yogurt#6767
'''

# These are the lists where the possible outcomes are stored.
posibilities = []
weights = []


# This function simply loads the json file. You shouldn't need to use it outside of this program.
def load_odds_json():
    # Opens the 'odds.json' file.
    odds_file = (script_dir / "odds.json").open()
    # Loads it into a JSON object.
    data = json.load(odds_file)

    # For every entry in the JSON file...
    for x in data:
        # Add the properties to their respective list.
        posibilities.append(x["multiplier"])
        weights.append(x["weight"])

    print("Odds loaded successfully!")


# This function handles the mathmatics of the gambling here. Returns a tuplet containing the the new amount, the multiplier, and the original amount.
def gamble(n):
    multiplier = random.choices(posibilities, weights)[0]

    return (n * multiplier, multiplier, n)


load_odds_json()
'''
###################################
'''


class gambling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna run around')

    @commands.Cog.listener()
    async def on_message(self, message):
        stats = levelling.find_one({"id": message.author.id})
        if not message.author.bot:
            if stats is None:
                newuser = {"id": message.author.id, "xp": 0, "credit": 0}
                levelling.insert_one(newuser)
            else:

                socialcredit = 10
                jinlist = ['<:jinhappy1:835921639551008818>',
                           '<:jintroll:887239493856423947>',
                           '<:jintrol:900420574893981698>',
                           '<:jinhollow:887994492903383080',
                           'jinwolloh:890624462561624144>'
                    , '<:jinhype:883393914143387699>'
                    , '<:jincool:854229962088251424>'
                    , '<:Jingrief:886952606168133732>'
                    , '<:jtl:900422440482635857>',
                           '<:Jinwide2:856038550738698250>',
                           '<:jinchad:888109451872174091>']
                for emoji in jinlist:
                    if emoji in message.content:
                        socialcredit = 20
                        break

                credwords = {
                    'jai hind': 20,
                    'jai jind': 20,
                    'jin sucks': -100,
                    'wah wah': 20,
                    'something happened in jinanmen square in 1989': -60000000,
                    'fish': -100000
                }
                for word in credwords:
                    if word in message.content.lower():
                        socialcredit = credwords[word]

                credit = stats["credit"] + socialcredit

                levelling.update_one({"id": message.author.id}, {"$set": {"credit": credit}})

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def gift(self, ctx, user: discord.User, num: int):

        stats = levelling.find_one({"id": ctx.author.id})
        if num > stats["credit"]:
            await ctx.channel.send("You can't gift more credits than what you have")
        if num < 0:
            await ctx.send("You can't gift negative credits")
        else:
            giftercredit = stats["credit"] - int(num)
            levelling.update_one({"id": ctx.author.id}, {"$set": {"credit": giftercredit}})
            stats2 = levelling.find_one({"id": user.id})
            gifteecredit = stats2["credit"] + int(num)
            levelling.update_one({"id": user.id}, {"$set": {"credit": gifteecredit}})
            await ctx.send(f"Gifted {num:,} jincord social credits to {user.name}")

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def credit(self, ctx):
        stats = levelling.find_one({"id": ctx.author.id})
        credit = stats["credit"]
        await ctx.send(f'Your jincord social credit is {int(credit):,}')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def creditboard(self, ctx, num=1):
        message : discord.Message = await ctx.send("Please wait...")
        if num == 1:
            rankings = levelling.find().sort("credit", -1)
            i = 1
            embed = discord.Embed(title="Jincord Credits Leaderboard", color=discord.Color.green())
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["credit"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"{int(tempxp):,}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
                await message.edit(content=None, embed=embed)
        elif num == 2:
            rankings = levelling.find().sort("credit", -1)
            i = 11
            embed = discord.Embed(title="Jincord Credits Leaderboard", color=discord.Color.green())
            for x in rankings[10:]:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["credit"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"{int(tempxp):,}", inline=False)
                    i += 1
                except:
                    pass
                if i == 21:
                    break
            await message.edit(content=None, embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def gamble(self, ctx, amount: str):
        stats = levelling.find_one({"id": ctx.author.id})
        if amount == 'all':
            number = stats["credit"]
        elif amount == 'half':
            number = int(stats["credit"] / 2)
        else:
            number = int(amount)

        if number > stats['credit']:
            await ctx.send("You cannot gamble more than what you have")
        elif stats["credit"] < 0:
            await ctx.send("You cannot gamble if your credits are negative")
        elif number < 0:
            await ctx.send("You cannot gamble negative credits")
        else:

            gambleTuple = gamble(number)
            tempcredit = stats["credit"] - number
            newcredit = tempcredit + gambleTuple[0]
            levelling.update_one({"id": ctx.author.id}, {"$set": {"credit": newcredit}})
            newAmount = gambleTuple[0]
            multiplier = gambleTuple[1]
            originalAmount = gambleTuple[2]
            change = newAmount - originalAmount
            if change > 0:
                gainorlose = "Gained"
                embedcolor = discord.Color.green()
            elif change < 0:
                gainorlose = "Lost"
                embedcolor = discord.Color.red()

            else:
                gainorlose = "gained"
            embed = discord.Embed(title=f"{gainorlose} {int(abs(change)):,} credits", color=embedcolor)
            embed.add_field(name="**Multiplier: **", value=multiplier, inline=True)
            embed.add_field(name="**New amount: ** ", value=f"{int(newAmount):,}", inline=True)
            embed.add_field(name="**Gambler: ** ", value=ctx.author.mention, inline=True)
            embed.add_field(name="**Total Social Credits: **", value=f"{int(newcredit):,}", inline=True)
            # await ctx.send(f"New total: {int(gambleTuple[0])}\nMultiplier: {gambleTuple[1]}\nOriginal amount: {int(gambleTuple[2])}\nYou {gainorlose} {int(abs((change)))} credits. Your new social credits total is {int(newcredit)}")
            await ctx.send(embed=embed)

    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(gambling(client))
